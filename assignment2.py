import urllib2
import csv
from datetime import datetime
import logging
import random
import argparse
from pprint import pprint


def  downloadData(url=''):
    response = urllib2.urlopen(url)
    cr = csv.reader(response)
    csvData = 'save file here'
    processData(cr)


def processData(data):
    newdata = {}
    format_str = '%d/%m/%Y'
    datetime_obj = None
    for row in data:
        id = row[0]
        if datetime_obj != format_str:
            try:
                datetime_obj = datetime.strptime(row[2], format_str).date()
            except Exception:
                continue
            newdata[int(row[0])] = (row[1], datetime_obj)
    id = 14
    displayPerson(id, newdata)


def displayPerson(id=0, personData={}):
    print(id)
    print(personData)
    for key in personData.items():
        print(key, 'key')
        if key == id:
            print(key)
    print('No user found with that id')
    pass

def main():
    pass

downloadData('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
