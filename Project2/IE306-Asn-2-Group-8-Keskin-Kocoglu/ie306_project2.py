# in part 1, we decided that the random number generation process is exponential. 

import random
import math
import openpyxl
import os

random.seed(123456)

mean = 243
limit = 10 * 24 * 60 * 60
current_time = 0

interarrival_times = []
interarrival_times.append("Generated Interarival Times")

while current_time < limit:
    interarrival_time = -mean * math.log(1 - random.uniform(0, 1))
    interarrival_times.append(interarrival_time)
    current_time += interarrival_time


'''
filename = "ie306_project2.xlsx"
path = os.getcwd()

workbook = openpyxl.load_workbook(os.path.join(path, filename))
worksheet = workbook['8']

for i in range(len(interarrival_times)):
    cell = worksheet.cell(row=i+1, column=1)
    cell.value = interarrival_times[i]

workbook.save(os.path.join(path, filename))
'''

