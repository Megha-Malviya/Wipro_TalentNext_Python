import re
import requests

# 1. Check if a string has only octal digits (0-7)
#    Given list: ['789', '123', '004']

strings = ['789', '123', '004']
print("1) Checking if strings have only octal digits:")
for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s} -> Only octal digits")
    else:
        print(f"{s} -> Not octal digits")


# 2. Extract the user id, domain name and suffix from the given email addresses
# Emails:
# zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = re.compile(r'(\w+)@(\w+)\.(\w+)')
print("\n2) Extracting parts from email addresses:")
for email in emails.splitlines():
    match = pattern.match(email)
    if match:
        user, domain, suffix = match.groups()
        print(f"Email: {email} -> User: {user}, Domain: {domain}, Suffix: {suffix}")


# 3. Split the following irregular sentence into proper words
# sentence = """A, very   very; irregular_sentence"""
# Expected output: A very very irregular sentence

sentence = """A, very   very; irregular_sentence"""
cleaned = re.sub(r'[^A-Za-z]+', ' ', sentence)
final_sentence = ' '.join(cleaned.split())
print("\n3) Properly split sentence:")
print(final_sentence)


# 4. Clean up the tweet so that it contains only the user’s message.
# Remove URLs, hashtags, mentions, punctuations, RTs and CCs.

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

text = re.sub(r'\bRT\b|\bcc\b', '', tweet)
text = re.sub(r'http\S+', '', text)
text = re.sub(r'[@#]\w+', '', text)
text = re.sub(r'[^\w\s]', '', text)
final_tweet = ' '.join(text.split())

print("\n4) Cleaned tweet:")
print(final_tweet)


# 5. Extract all the text portions between the tags from the HTML page:
# https://raw.githubusercontent.com/selva86/datasets/master/sample.html

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
texts = re.findall(r'>([^<>]+)<', html)
clean_texts = [t.strip() for t in texts if t.strip()]

print("\n5) Extracted text from HTML:")
print(clean_texts)


# 6. Given list of words, identify the words that begin and end with the same character.
# Words: ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']

print("Words that begin and end with the same character:")
for word in words:
    if word[0].lower() == word[-1].lower():
        print(word)
