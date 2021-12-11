# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

## Table of contents

- [Team info](#team-info)
- [Requirements](#requirements)
- [Installation](#installation)
- [Overview](#overview)
- [Software documentation](#software-documentation)
- [Software usage documentation](#software-usage-documentation)
- [Contribution](#contribution)

## Team info

Team name: kms

Team members: Kim Li (kimli2), Kevin Tzeng (ktzeng2), Shreyas Chandrashekaran (svc3)

## Requirements

- Python3 version 3.X (tested on 3.8.2)
- Packages included in [project/requirements.txt](project/requirements.txt)

## Installation

From the project directory, run the following command to install requirements:

```bash
$ pip install requirements.txt
```

## Overview

The function `cleanData()` is used to clean the raw e-mail text in [project/original_dataset.csv](project/original_dataset.csv) so that the e-mail subject and e-mail body are separated into separate columns. The function returns a pandas dataframe with columns `spam, subject, body, attachment, reply, forward`.

The function `filter(df, args)` takes in the cleaned dataframe and user-passed arguments to further filter the e-mail dataset and returns the filtered dataframe. 

## Software documentation

The following (optional) arguments can be passed in the terminal to filter the dataset:


| Arguments          | Type             | Description   |	
| :----------------- |:----------------:| :-------------|
| --csv 	         | string           | csv file to write output to (default is output.csv)
| --spam             | integer          | choose a value for spam (0 for not spam, 1 for spam)
| --attachment       | integer          | filter based on whether email contains attachment (0 for no attachments, 1 for attachment included
| --reply  	         | integer          | filter based on whether email is a reply (0 for not reply, 1 for reply)
| --forward          | integer          | filter based on whether email is forwarded (0 for not forwarded, 1 for forwarded)
| --subject          | string           | filter based on keywords contained in subject
| --body             | string           | filter based on keywords contained in e-mail body


## Software usage documentation

The data can be simply cleaned and returned by running the following:
```bash
$ python parser.py
```

To use the filtering flags, 
For example, [project/sample.csv](project/sample.csv) was created using the following filters:
```bash
$ python parser.py --csv 'sample.csv' --attachment 1 --reply 1
```

and contains a list of all e-mails that include an attachment and are a reply to a previous e-mail. 


## Contribution

- Kim: filtering dataset 
- Kevin: filtering dataset
- Shreyas: cleaning dataset
