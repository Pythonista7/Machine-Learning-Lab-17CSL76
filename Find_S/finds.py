"""
Implement and demonstrate the FIND-S algorithm for finding the most specific hypothesis based on a given set of training data samples
Read the training data from a .CSV file

"""

import pandas as pd 

# load the csv
df = pd.read_csv("enjoysport.csv")

# save shape
rows = df.shape[0]
cols = df.shape[1]

# init most general and most specific hyporthesis
general = ["?"]*(cols-1)
h = ["0"]*(cols-1)

# init postive and negative classes
positive=[]
negative=[]

# loop over each row and bucket them into one of the above classes
for i in range(rows):
    if df["enjoy_sport"][i]=="yes":
        positive.append(df.iloc[i])
    else:
        negative.append(df.iloc[i])

# loop over all positive examples and generalize each attribute appropriately
for i in range(len(positive)):
    for j in range(cols-1):
        if h[j]=="0":
            h[j]=positive[i][j]
        elif h[j]!=positive[i][j]:
            h[j]="?"
        else:
            h[j]=positive[i][j]
    
    print(f"Step {i}:",h)

print("result :",h)
