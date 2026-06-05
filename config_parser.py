# Temporary variables to store data as we read line-by-line
current_interface = None
current_description = "No Description"
current_ip = "No IP Address"

print("--- STARTING CISCO CONFIGURATION PARSER ---")

with open("running_config.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()

        # 1. When we hit a NEW interface, print the OLD one first, then reset
        if cleaned_line.startswith("interface"):
            if current_interface:
                # Print the fully assembled data from the previous block
                print(f"{current_interface} | {current_description} | {current_ip}")
            
            # Reset our storage variables for the new interface
            current_interface = cleaned_line
            current_description = "No Description"
            current_ip = "No IP Address"

        # 2. Capture description if it exists for the current interface
        elif cleaned_line.startswith("description"):
            current_description = cleaned_line

        # 3. Capture IP address if it exists for the current interface
        elif cleaned_line.startswith("ip address"):
            current_ip = cleaned_line

    # 4. Print the very last interface block after the loop finishes
    if current_interface:
        print(f"{current_interface} | {current_description} | {current_ip}")