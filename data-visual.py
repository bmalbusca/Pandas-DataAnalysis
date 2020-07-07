import sys
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

filename =""
df=None
    
print(sys.argv)
if len(sys.argv) > 1: 
    filename= sys.argv[1]
    print(filename)
try:
    df = pd.read_csv(filename)
except Exception as err:
    print(err.args)
    exit(0)


print(df.head(), "\n") #first 5 rows 
print("Dataset Rows: ",df.shape[0]," Columns: " ,df.shape[1]) 
print(df.columns, "\n")

# change datatype for example bool to a int   
#df['column'] = df['column'].astype('int64')

#classes = df.iloc[:,-1] #all rows : against last column 
''' select subsets
classes = df[['Rank', 'Status', 'Age']]
classes2 = df.iloc[:,[0,df.columns.get_loc("Status"),11]]
print(classes) 
print(classes2)
print(classes2.iloc[:,classes2.columns.get_loc("Rank")].value_counts())
'''

# Fill all Nan
df.fillna(0, inplace=True)#inplace=True 
#print(df2['Study Documents'])

# Check if invalid data 
comp= df.drop_duplicates()
compare2 = df.iloc[:, :df.shape[1]-1].drop_duplicates()
print(compare2)
print(comp)

''' add new column 
df['protected']= list(range(0, 2529))
print(df[['Rank','protected']])
'''

df.plot(subplots=True,figsize=(20,10));
df.plot.scatter(x='Rank', y='Enrollment')
'''
#Using Pearson Correlation
plt.figure(figsize=(12,10))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
'''
plt.show()
