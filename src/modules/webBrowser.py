import webbrowser

# webbrowser.open("http://www.python.org")

chrome = webbrowser.get("google-chrome")
print(chrome.name)
chrome.open("http://www.python.org")
