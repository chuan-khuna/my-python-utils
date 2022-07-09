import re
import emoji

# https://gist.github.com/Alex-Just/e86110836f3f93fe7932290526529cd1?permalink_comment_id=3208085#gistcomment-3208085
emoji_pattern = re.compile("["
                           "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "\U0001F300-\U0001F5FF"  # symbols & pictographs
                           "\U0001F600-\U0001F64F"  # emoticons
                           "\U0001F680-\U0001F6FF"  # transport & map symbols
                           "\U0001F700-\U0001F77F"  # alchemical symbols
                           "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           "\U0001FA00-\U0001FA6F"  # Chess Symbols
                           "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           "\U00002702-\U000027B0"  # Dingbats
                           "\U000024C2-\U0001F251"
                           "]+")


def remove_emoji(text):
    demojized_text = emoji.demojize(text)
    emoji_re = re.compile("(:[!_\-\w]+:)")
    return re.sub(emoji_re, "", demojized_text)