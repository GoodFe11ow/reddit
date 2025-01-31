import praw
import re
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
)
subreddit_name = 'learnpython'
words = {}

for submission in reddit.subreddit("learnpython").hot(limit=5):
    submission.comments.replace_more(limit=0)
    
    for comment in submission.comments:
        for word in comment.body.split():
            word = re.sub('^[^a-zA-Z]*|[^a-zA-Z]*$', '', word).lower()
            
            if word and word in words:
                words[word] += 1
            elif word:
                words[word] = 1

sortedWords = sorted(words, key=words.get, reverse=True)
sortedWords = sortedWords[:15]

sizes = []
labels = []


for w in sortedWords:
    sizes.append(words[w])
    labels.append(w)

plt.title('Top comments: r/' + subreddit_name)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.show()