import csv
import datetime as dt
import numpy as np

c = 0
with open("./raw_2022_09_01.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    if c>0:
        time = row[-2]
       
        time2 = dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        time3 = time2
        print((time3.timetuple()))
    c+=1
    
    
    
    if c==2:
        break
        
  