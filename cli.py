import argparse
from datetime import datetime
import os
import subnet_engine

def main():
    parser = argparse.ArgumentParser(description="Enterprise Network Automation Subnet Calculator")
    parser.add_argument("cidr", help="Target CIDR block (e.g., 172.16.0.0/16)")
    parser.add_argument("--check", help="Single IP address to verify inside the network boundaries")
    parser.add_argument("--file", help="Path to a text file containing a list of IPs to scan in bulk")
    
    args = parser.parse_args()
    
    # Run the core network engine calculations
    result = subnet_engine.calculate_subnet_details(args.cidr)
    
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return
        
    print("\n--- SUBNET CALCULATION REPORT ---")
    print(f"Network ID:        {result['network_id']}")
    print(f"Subnet Mask:       {result['subnet_mask']}")
    print(f"Broadcast Address: {result['broadcast_address']}")
    print(f"Usable Host Slots: {result['usable_hosts']}")
    
    # Track items we want to log permanently
    ips_to_check = []
    
    # Scenario A: User passed a single IP via --check
    if args.check:
        ips_to_check.append(args.check)
        
    # Scenario B: User passed a text file via --file
    if args.file:
        if not os.path.exists(args.file):
            print(f"❌ Error: The file '{args.file}' could not be found.")
            return
        
        # Read lines from the inventory file, strip out extra spaces/newlines
        with open(args.file, "r") as f:
            for line in f:
                cleaned_line = line.strip()
                if cleaned_line:  # Ignore empty lines
                    ips_to_check.append(cleaned_line)

    # Process and log the target IP checklist
    if ips_to_check:
        print("\n--- BULK IP VERIFICATION SCAN ---")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Open our permanent system log vault
        with open("subnet_audit.txt", "a") as log_file:
            log_file.write(f"\n=== BULK AUDIT LOG ({timestamp}) ===\n")
            log_file.write(f"Target Network: {args.cidr}\n")
            log_file.write("-" * 50 + "\n")
            
            # The Automation Engine Loop
            for target_ip in ips_to_check:
                status = subnet_engine.verify_ip_in_subnet(result["obj"], target_ip)
                
                # Format output indicators dynamically
                if status == "VALID":
                    display_line = f"🟢 VALID: {target_ip}"
                elif "BOUNDARIES MISMATCH" in status:
                    display_line = f"🟡 {status}: {target_ip}"
                elif status == "MISMATCH":
                    display_line = f"🔴 MISMATCH: {target_ip}"
                else:
                    display_line = f"⚠️ INVALID FORMAT: '{target_ip}'"
                
                # Print to terminal screen and write to hard drive log file simultaneously
                print(display_line)
                log_file.write(f"{display_line}\n")
                
            log_file.write("=" * 50 + "\n")
            
        print(f"\n💾 Bulk Scan complete! System Report permanently saved to 'subnet_audit.txt'")

if __name__ == "__main__":
    main()