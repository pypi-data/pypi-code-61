try:
    import requests
except ImportError:
    sys.exit("""You need requests module
                install via "pip install requests" """)

def slack_msg(msg, url='https://hooks.slack.com/services/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'):
    data = {"text": msg }
    headers = {"Content-Type": "application/json"}
    return requests.post(url, data=str(data), headers=headers)