import pandas as pd
df = pd.read_csv('spam_ham_dataset.csv', encoding='utf-8')

subjects = []
# bodies = []

for row in df.itertuples():
    text = row.text
    loc = text.find("\n")
    subjects.append(text[0:loc])
    # bodies.append(text[loc:]

df['subject'] = subjects
# df['body'] = bodies
df.to_csv("data.csv")