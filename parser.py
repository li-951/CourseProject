import pandas as pd
import csv

def separateSubject():
    df = pd.read_csv('original_dataset.csv', encoding='utf-8')

    subjects = []
    bodies = []

    for row in df.itertuples():
        text = row.text
        loc = text.find("\n")
        subjects.append(text[0:loc])
        bodies.append(text[loc:])

    df['subject'] = subjects
    df['body'] = bodies
    df.to_csv("data.csv")


def parse(output_file):
    with open('data.csv','r') as csvinput:
        with open(output_file, 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            for row in csv.reader(csvinput):
                if row[2] == "label":
                    writer.writerow(row + ["contains attachment"] + ["reply"] + ["forwarded"])
                else:
                    att = int("see attached file" in row[3])
                    rep = int("Subject: fw :" in row[3])
                    fw = int("Subject: re :" in row[3])
                    writer.writerow(row + [att] + [rep] + [fw])


def main():
    separateSubject()
    text = raw_input("CSV file to place data in: ") 
    parse(text)

if __name__ == "__main__":
    main()