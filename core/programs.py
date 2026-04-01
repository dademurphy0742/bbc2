import requests

def fetch_programs():
    try:
        r = requests.get("https://hackerone.com/programs.json", timeout=10)
        data = r.json()

        programs = []
        for p in data[:20]:
            programs.append({
                "name": p.get("name"),
                "url": f"https://hackerone.com/{p.get('handle')}"
            })

        return programs

    except Exception as e:
        print(f"[!] API error: {e}")
        return []

def register_helper(url):
    print(f"\n[→] Open and register: {url}")
    input("Press ENTER after registering...")
