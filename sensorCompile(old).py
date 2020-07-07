#compile script
import os
import datetime
import pandas as pd

files = os.listdir("./data")
#files.remove("sensorCompile.py")
print(files)
names = ["SN","MCU","X","Y","Z","T"]
columnNames = ["DateTime", "X1", "Y1", "Z1", "T1", "X2", "Y2", "Z2", "T2", "X3", "Y3", "Z3", "T3"]

def convertToDateTime(f):
    year, month, day, hour, minute  = f[2:6],f[7:9],f[10:12],f[13:15],f[15:17]
    x = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    return x

def createSample(a,b,c):
    sampleData = [a[0],a[3],a[4],a[5],a[6],b[3],b[4],b[5],b[6],c[3],c[4],c[5],c[6]]
    return sampleData

#print(files[0])
#convertToDateTime(files[0])

df = []

#Appending all the files to dataframe in the form [dataframe, filename]
for f in files:
    df.append([pd.read_csv(("data/" +f),names=names),f])


samples = []
#Inserts DateTime to all dataframes
for x, y in enumerate(df):
    y[0].insert(0,'DateTime',convertToDateTime(y[1]))
    #df0 = y[0].query('SN == 0')
    #df1 = y[0].query('SN == 1')
    #df2 = y[0].query('SN == 2')
    #for i,j in enumerate(df0):

    #sample.append()


#df0 = df[0][0].query('SN == 0')
#df1 = df[0][0].query('SN == 1')
#df2 = df[0][0].query('SN == 2')
#print("DF0")
#print(df0)
#for i in range(len(df0)):
#    samples.append(createSample(df0.iloc[i],df1.iloc[i],df2.iloc[i]))

for x,y in enumerate(df):
    df0 = y[0].query('SN == 0')
    df1 = y[0].query('SN == 1')
    df2 = y[0].query('SN == 2')
    #k is the minimum amount of samples
    k = min(len(df0),len(df1),len(df2))
    for i in range(k):
        samples.append(createSample(df0.iloc[i],df1.iloc[i],df2.iloc[i]))
        #print("df0: " + str(len(df0)))
        #print("df1: " + str(len(df1)))
        #print("df2: " + str(len(df2)))
        #print("\n")

print("SAMPLES HERE:")
print(samples)
sampledf2 = pd.DataFrame(data = samples, columns = columnNames)
print(sampledf2)
sampledf2.to_csv("output.csv")


#sample = createSample(df0.iloc[0],df1.iloc[0],df2.iloc[0])
#print(sample)
#sampledf = pd.DataFrame(data = sample, columns = columnNames)

#df.append(pd.read_csv(files[0]))
#df[0].to_excel("output.xlsx")

#print(sampledf)
