# Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

# Bob only ever answers one of five things:

# "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
# "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
# "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
# "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
# "Whatever." This is what he answers to anything else.

def response(hey_bob):
    dialogue = hey_bob.strip()
    if dialogue.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if dialogue.endswith("?"):
        return "Sure."
    if hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!"
    return "Whatever."