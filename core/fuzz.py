from core.utils import run_command

def run_directory_fuzz(target):
    print(f"[*] Dir fuzz: {target}")
    cmd = (
        f"ffuf -u {target}/FUZZ "
        f"-w wordlists/common.txt "
        f"-mc 200,204,301,302,403 "
        f"-t 40 -timeout 5"
    )
    return run_command(cmd, timeout=120)

def run_param_fuzz(target):
    print(f"[*] Param fuzz: {target}")
    params = ["id", "user", "account"]

    results = []
    for p in params:
        cmd = f'ffuf -u "{target}?{p}=FUZZ" -w wordlists/common.txt -mc 200,403 -t 30'
        output = run_command(cmd, timeout=60)
        results.append((p, output))

    return results
