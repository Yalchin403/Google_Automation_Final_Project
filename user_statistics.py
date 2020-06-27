#!/usr/bin/env python3
import re
import operator
import csv
from pip._vendor.distlib.compat import raw_input
logFile = "syslog.log"
with open(logFile) as file:
    lines = file.readlines()
# empty list for usernames_error
usernames_error = []
for line in lines:
    pattern = r"ERROR: [\w ]*\((\w+)\)"
    result = re.findall(pattern, line)
    if result:
        usernames_error.append(result[0])
#error empty dictionary
error = {}
for i in range(0, len(usernames_error)):
    count = 0
    for j in range(0, len(usernames_error)):
        if usernames_error[i] == usernames_error[j]:
            count += 1
        error[usernames_error[i]] = count
error = dict(sorted(error.items(), key=operator.itemgetter(1), reverse=True))
# print(error)
# error dictionary end

#info dic starting
logFile = "syslog.log"
with open(logFile) as file:
    lines = file.readlines()
# empty list for usernames_info
usernames_info = []
for line in lines:
    pattern = r"INFO: [\w ]*\[[0-9]+\] \((\w+)\)"
    result = re.findall(pattern, line)
    if result:
        usernames_info.append(result[0])
# empty dictionary for userNameInfo
info = {}
for i in range(0, len(usernames_info)):
    count = 0
    for j in range(0, len(usernames_info)):
        if usernames_info[i] == usernames_info[j]:
            count += 1
    info[usernames_info[i]] = count
info = dict(sorted(info.items(), key=operator.itemgetter(1), reverse=True))
# print(info)
# info dictionary ending




combination = []
for key, item in error.items():
    if key in info.keys():
        combination.append({"Username": key, "INFO": info[key], "ERROR": error[key]})
print(combination)

#ending of final list to feed csv

csv_file = "dict_csv_2.csv"
csv_columns = ["Username", "INFO", "ERROR"]
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in combination:
        writer.writerow(data)