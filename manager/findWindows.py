def findWindowsByTitleString(titleString, windows):
    return list(filter(lambda window: titleString.lower() in window.title.lower(), windows))
