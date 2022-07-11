import re
import html
import string


def remove_urls(text):
    # https://regex101.com/r/hG9t0Q/1
    # https://regexr.com/3e6m0
    # https://regexr.com/37i6s
    pattern = re.compile("(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
    return re.sub(pattern, "", text)


def remove_starting_space(text):
    # \s = space including, eg \n \t
    pattern = re.compile("^\s*")
    return re.sub(pattern, "", text)


def remove_ending_space(text):
    pattern = re.compile("\s*$")
    return re.sub(pattern, "", text)


def unescape_html(text):
    return html.unescape(text)


def remove_punctuations(text):
    return text.translate(str.maketrans("", "", string.punctuation))
