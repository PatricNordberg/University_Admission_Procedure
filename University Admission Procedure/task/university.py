import re
import pandas as pd

def Extract(lst):
    return [[item[0],item[1]] for item in lst]

info_list = []
sorted_list = []

numb_app = int(input())

file_list = [ x.split() for x in open('applicants.txt').read().split('\n') if x != '' ]


numb_acc_app = int(input())

for apps in range(numb_app):
    app_info = input()
    info_list.append(re.split("\s", app_info))
info_list.sort()

for i in range(0, len(info_list)):
    info_list[i][2] = float(info_list[i][2])

sorted_list = sorted(info_list, reverse=True, key=lambda x: (x[2]))
sorted_list_top = sorted_list[:numb_acc_app]
acc_student_list = Extract(sorted_list_top)

print("Successful applicants:")

for acc_student in acc_student_list:
    print(" ".join(map(str, acc_student)))


