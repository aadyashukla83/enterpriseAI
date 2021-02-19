
import re
import csv
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

fh=open(os.path.join(BASE,"dataset.csv"))


reader = csv.reader(fh, delimiter='+')


dataset={}
#{lable 1:No. of records that are labeled 1}


no_of_items={}
#{word:{label1: count of the occurence of word with label 1}}


feature_set={}


for row in reader:

	no_of_items.setdefault(row[1],0)

	no_of_items[row[1]]+=1

	dataset.setdefault(row[1],{})

	split_data=re.split('[^a-zA-Z\']',row[0])

	for i in split_data:

		if len(i) > 2:

			dataset[row[1]].setdefault(i.lower(),0)

			dataset[row[1]][i.lower()]+=1

			feature_set.setdefault(i.lower(),{})

			feature_set[i.lower()].setdefault(row[1],0)

			feature_set[i.lower()][row[1]]+=1

	


