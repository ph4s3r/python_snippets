"""
https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27

Average Words Length

# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

"""


sentence1 = "Hi all, my name is Tom... I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

# Replace non alphanumerics with ''s

nonalnum = "!?',;."

for p in nonalnum:
    sentence1 = sentence1.replace(p, '')
    sentence2 = sentence2.replace(p, '')

# making a list of words by splitting by the default delimiter space

words1 = sentence1.split()
words2 = sentence2.split()

words = words1 + words2

# avg is the sum of all chars divided by the number of words

numwords = len(words)

total_len = 0

for word in words:
    total_len += len(word)

print(f"the avg len of all words here is {round(total_len/numwords, 2)}")
