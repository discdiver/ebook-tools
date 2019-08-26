import emoji
import re


def strip_emoji(text):
    print(emoji.emoji_count(text))
    new_text = re.sub(emoji.get_emoji_regexp(), r"", text)

    return new_text


with open("memorable_docker.md", "r") as file:
    old_text = file.read()

nt = strip_emoji(old_text)


with open("file.md", "w+") as new_file:
    new_file.write(nt)
