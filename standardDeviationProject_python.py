import csv
import pandas as pd
import plotly.express as px
import math

with open("/Users/Kartik/Downloads/std_deviation-master/data.csv", newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
#file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i]
    #[1]
    new_data.append(n_num)

print(new_data)

def mean(data):
    n=len(new_data)
    total=0
    for x in new_data:
        total+=int(x)
    mean=total/n
    return mean

#Squaring and getting the values
squared_list=[]
for number in new_data:
    a=int(number)-mean(new_data)
    a=a**2
    squared_list.append(a)
#getting a sum
sum=0
for i in squared_list:
    sum=sum+i
    
result=sum/(len(new_data)-1)

#getting the deviation by taking the square root of the result
std_dev=math.sqrt(result)

print(std_dev)
    
    

    
