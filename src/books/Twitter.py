def send_to_twitter():
    msg = "I am a message that will be sent to twitter!"
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "http://twitter.com/statuses", "Bermec42", "bermec")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_handler)
    page_opener = urllib.request.build_opener(page_opener)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( ('status': msg) )
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()