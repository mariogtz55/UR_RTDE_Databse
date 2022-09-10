import csv
from insertion import *
import time
from DBHelper import db
from DBHelper.Models import datos_robot
import pandas as pd


with open('robot_data.csv', 'r') as file:
    lines = file.readlines() 
comparador=lines[1]
arr=[]
for i in lines:
    if i != comparador:
        arr.append(i)
longitud=len(arr)
for i in range(longitud):
    a=arr[i]
    a=a.replace(' ',',')
    arr[i]=a
newarr=[]
for i in range(longitud):
     x=arr[i].split(',')
     newarr.append(x)

with open('mid.csv', 'w',encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    for i in range(longitud):
        x=newarr[i]
        x= map(lambda s: s.strip(),x)
        writer.writerow(x)

with open('historic.csv', 'r') as file:
    lines = file.readlines() 
leng=len(lines)
if leng>0:
    df=pd.read_csv('historic.csv')
    df2=pd.read_csv('mid.csv')
    dfinal=pd.concat([df, df2], axis=0)
else:
    dfinal=pd.read_csv('mid.csv')

dfinal.to_csv("historic.csv",index=False)

dfinal['actual_digital_input_bits']=dfinal['actual_digital_input_bits'].astype(float)

dfinal=dfinal.reset_index()

db.session.execute("TRUNCATE TABLE datos_robot")
db.session.commit()

mapped_rows = prepare_for_insertion(dfinal, 'datos_robot')


# Paso 3.2.1 inserción en tabla obras_procesado
db.session.bulk_insert_mappings(datos_robot, mapped_rows)
db.session.commit()



