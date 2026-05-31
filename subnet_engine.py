import ipaddress

def calculate_subnet_details(cidr_network):
    """Calculates core network parameters using ipaddress module."""
    try:
        network = ipaddress.IPv4Network(cidr_network, strict=False)
        return {
            "network_id": str(network.network_address),
            "subnet_mask": str(network.netmask),
            "broadcast_address": str(network.broadcast_address),
            "usable_hosts": network.num_addresses - 2 if network.num_addresses > 2 else 0,
            "obj": network
        }
    except ValueError as e:
        return {"error": f"Invalid CIDR block format: {e}"}

def verify_ip_in_subnet(network_obj, check_ip):
    """Verifies if a target IP address falls within the calculated network limits."""
    try:
        ip = ipaddress.IPv4Address(check_ip)
        
        # Check if it matches system boundaries
        if ip == network_obj.network_address:
            return "BOUNDARIES MISMATCH (Network ID Address)"
        if ip == network_obj.broadcast_address:
            return "BOUNDARIES MISMATCH (Broadcast Address)"
            
        if ip in network_obj:
            return "VALID"
        else:
            return "MISMATCH"
    except ValueError:
        return "INVALID FORMAT"
