import pandas as pd
from datetime import datetime

dataframe = pd.read_csv("data.csv")
newDataframe = pd.DataFrame()

for index, row in dataframe.iterrows():
    if "waistcoat" in row[1]:
        newDataframe = newDataframe.append(row, ignore_index=True)
    
count = int(0)
countList = []
for indexOuter, eachOuter in newDataframe.iterrows():
    myLikes = eachOuter[2]
    for indexInner, eachInner in newDataframe.iterrows():
        if eachInner[2] == myLikes:
            count = count + 1
    countList.append(str(count))
    count = 0

newDataframe["Count"] = countList

now = datetime.now()
filename = now.strftime("%d_%m_%Y-%H_%M_%S") + ".csv"
newDataframe.to_csv(filename)
