from core.utils import run_command

def subdomain_enum(domain):
    print("[*] Running subdomain enumeration...")
    cmd = f"subfinder -silent -d {domain}"
    output = run_command(cmd)
    return output.splitlines() if output else []


def check_live_hosts(subdomains):
    print("[*] Checking live hosts...")
    live_hosts = []

    for sub in subdomains:
        cmd = f"httpx -silent -status-code -title -u https://{sub}"
        result = run_command(cmd)
        if result:
            live_hosts.append(result)

    return live_hosts


def port_scan(domain):
    print("[*] Running basic port scan...")
    cmd = f"nmap -F {domain}"
    return run_command(cmd)


def run_recon(domain):
    results = {}

    subdomains = subdomain_enum(domain)
    results["subdomains"] = subdomains

    live_hosts = check_live_hosts(subdomains)
    results["live_hosts"] = live_hosts

    port_results = port_scan(domain)
    results["ports"] = port_results

    return results
