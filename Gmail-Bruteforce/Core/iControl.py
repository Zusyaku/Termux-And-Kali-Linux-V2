def CheckTheInternet(url='https://www.google.com/', timeout=3):
    import requests
    try:
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        return False