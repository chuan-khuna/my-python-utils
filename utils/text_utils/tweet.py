import re

def remove_user(text)
    # replace user name
    pattern = re.compile("\@[a-zA-Z0-9_+=]{3,}")
    return re.sub(pattern, "", text)

def remove_RT_user(text):
    pattern = re.compile("^RT\s\@[a-zA-Z0-9_+=]{3,}:\s")
    return re.sub(pattern, "", text)