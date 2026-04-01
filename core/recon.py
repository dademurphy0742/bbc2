from core.utils import run_command
import tempfile
import os

def subdomain_enum(domain):
    print("[*] Subdomain enumeration...")
    cmd = f"subfinder -silent -d {domain}"
    output = run_command(cmd, timeout=60)
    return list(set(output.splitlines())) if output else []

def resolve_domains(subdomains):
    print(f"[*] Resolving {len(subdomains)} domains...")
    if not subdomains:
        return []

    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
        tmp.write("\n".join(subdomains))
        path = tmp.name

    cmd = f"dnsx -silent -l {path}"
    output = run_command(cmd, timeout=60)

    os.remove(path)
    return output.splitlines() if output else []

def check_live_hosts(domains):
    print(f"[*] Probing {len(domains)} hosts...")
    if not domains:
        return []

    with tempfile.NamedTemporaryFile(delete=False, mode='w') as tmp:
        tmp.write("\n".join(domains))
        path = tmp.name

    cmd = (
        f"httpx -silent -l {path} "
        f"-status-code -title -tech-detect "
        f"-threads 50 -timeout 5 -retries 1"
    )

    output = run_command(cmd, timeout=120)

    os.remove(path)
    return output.splitlines() if output else []

def run_recon(domain):
    subs = subdomain_enum(domain)
    print(f"[+] {len(subs)} subdomains found")

    resolved = resolve_domains(subs)
    print(f"[+] {len(resolved)} valid domains")

    live = check_live_hosts(resolved)
    print(f"[+] {len(live)} live hosts")

    return {
        "subdomains": resolved,
        "live_hosts": live
    }
