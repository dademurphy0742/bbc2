HIGH_VALUE = ["api", "admin", "dev", "stage", "auth", "login"]

def score_target(host):
    score = 0
    h = host.lower()

    for k in HIGH_VALUE:
        if k in h:
            score += 2

    if "200" in h:
        score += 3
    elif "403" in h:
        score += 2

    return score

def prioritize_targets(hosts):
    scored = [(h, score_target(h)) for h in hosts]
    return sorted(scored, key=lambda x: x[1], reverse=True)

def suggest_attacks(host):
    h = host.lower()
    out = []

    if "api" in h:
        out += ["Test IDOR (?id=)", "Fuzz /v1 /debug"]

    if "login" in h or "auth" in h:
        out += ["Test auth bypass", "Check weak JWT"]

    if "admin" in h:
        out += ["403 bypass", "Privilege escalation"]

    return out or ["Test XSS, SSRF, redirects"]
