#!/usr/bin/env python3
import re
import operator
import csv

from pip._vendor.distlib.compat import raw_input

logFile = "syslog.log"
with open(logFile) as file:
    lines = file.readlines()
    erDict = {}
    for line in lines:
        pattern = "ERROR: ([\w ]*)"
        result = re.findall(pattern, line)
        if result:
            if result[0] not in erDict:
                erDict[result[0]] = 1
            else:
                erDict[result[0]] = erDict[result[0]] + 1
    # print(sorted(erDict.items(), key = operator.itemgetter(1), reverse=True))

sortified = sorted(erDict.items(), key=operator.itemgetter(1), reverse=True)
last_modified = dict(sortified)
# print(last_modified)
#Csv header
f = open("dict_csv_1.csv", "w")
writer = csv.DictWriter(
    f, fieldnames=["Error", "Count"])
writer.writeheader()
f.close()
#Csv body
csv_file = "dict_csv_1.csv"
a_file = open("dict_csv_1.csv", "a+")
writer = csv.writer(a_file)
for key, value in last_modified.items():
    writer.writerow([key, value])
a_file.close()

