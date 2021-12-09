import pandas as pd
import csv
import argparse

default_output_file = "output.csv"

file_attached = "see attached file"
replied_email = "re :"
forward_email = "fw :"

csv_arg_message = "csv file to write output to (default is output.csv)"
spam_arg_message = "choose a value for spam (0 for not spam, 1 for spam)"
attachment_arg_message = "filter based on whether email contains attachment (0 for no attachments, 1 for attachment included"
reply_arg_message = "filter based on whether email is a reply (0 for not reply, 1 for reply)"
forward_arg_message = "filter based on whether email is forwarded (0 for not forwarded, 1 for forwarded)"
subject_arg_message = "filter based on keywords contained in subject"
body_arg_message = "filter based on keywords contained in e-mail body"


def cleanData():
    df = pd.read_csv('original_dataset.csv', encoding='utf-8')

    subjects = []
    bodies = []
    attachment = []
    reply = []
    forward = []

    for row in df.itertuples():
        text = row.text
        loc = text.find("\n")

        subject_text = text[0:loc]
        body_text = text[loc:]
        subjects.append(subject_text)
        bodies.append(body_text)

        attachment.append(int(file_attached in body_text))
        reply.append(int(replied_email in subject_text))
        forward.append(int(forward_email in subject_text or "forwarded by" in body_text))


    df['subject'] = subjects
    df['body'] = bodies
    df['attachment'] = attachment
    df['reply'] = reply
    df['forward'] = forward

    df.drop(['label', 'text'], axis=1, inplace=True)
    df.rename(columns = {'label_num':'spam'}, inplace=True)

    return df

def filter(df, args):
    for arg in args:
        if args[arg] and arg != "csv":
            if type(args[arg]) == int:
                df = df[df[arg] == args[arg]]
            elif type(args[arg] == str):
                df = df[df[arg].str.contains(args[arg])]
    return df


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--csv', type=str, help=csv_arg_message, default=default_output_file)
    parser.add_argument('--spam', type=int, help=spam_arg_message, default=None)
    parser.add_argument('--attachment', type=int, help=attachment_arg_message, default=None)
    parser.add_argument('--reply', type=int, help=reply_arg_message, default=None)
    parser.add_argument('--forward', type=int, help=forward_arg_message, default=None)
    parser.add_argument('--subject', type=str, help=subject_arg_message, default=None)
    parser.add_argument('--body', type=str, help=body_arg_message, default=None)
    args = vars(parser.parse_args())

    cleaned_df = cleanData()
    output = filter(cleaned_df, args)

    output.to_csv(args['csv'], index = False)

if __name__ == "__main__":
    main()