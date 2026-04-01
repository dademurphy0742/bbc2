from pathlib import Path

def create_workspace(name):
    safe = name.replace(" ", "_").lower()
    base = Path("hunts") / safe
    base.mkdir(parents=True, exist_ok=True)

    for f in ["subs.txt", "live.txt", "fuzz.txt", "payloads.txt", "notes.md"]:
        (base / f).touch()

    print(f"[+] Workspace: {base}")
    return base
