#compile script
import os
import datetime
import pandas as pd

files = os.listdir("./data")
names = ["SN","MCU","X","Y","Z","T"]
columnNames = ["DateTime", "X1", "Y1", "Z1", "T1", "X2", "Y2", "Z2", "T2", "X3", "Y3", "Z3", "T3"]

def convertToDateTime(f):
    year, month, day, hour, minute  = f[2:6],f[7:9],f[10:12],f[13:15],f[15:17]
    x = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    return x

def createSample(a,b,c):
    sampleData = [a[0],a[3],a[4],a[5],a[6],b[3],b[4],b[5],b[6],c[3],c[4],c[5],c[6]]
    return sampleData

def adjustTime(df):
    df = df.reset_index(drop=True)
    df = df.reset_index()
    df['index'] = df['index'] * 250
    df['index'] = pd.to_timedelta(df['index'],'milli')
    df['DateTime'] = df['DateTime'] + df['index']
    df = df.drop(columns=['index'])
    return df

df = []

#Appending all the files to dataframe in the form [dataframe, filename]
for f in files:
    df.append([pd.read_csv(("data/" +f),names=names),f])


samples = []
#Inserts DateTime to all dataframes
for x, y in enumerate(df):
    y[0].insert(0,'DateTime',convertToDateTime(y[1]))

for x,y in enumerate(df):
    #query seperates the sensors based on their SN
    df0 = y[0].query('SN == 0')
    df1 = y[0].query('SN == 1')
    df2 = y[0].query('SN == 2')
    df0 = adjustTime(df0)
    df1 = adjustTime(df1)
    df2 = adjustTime(df2)
    #k is the minimum amount of samples
    k = min(len(df0),len(df1),len(df2))
    for i in range(k):
        samples.append(createSample(df0.iloc[i],df1.iloc[i],df2.iloc[i]))

sampledf2 = pd.DataFrame(data = samples, columns = columnNames)
print(sampledf2)
sampledf2.to_csv("output.csv")


