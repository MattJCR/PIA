'''
PANDAS - Preparing dataset
'''
# python -m pip install --upgrade numpy pandas scipy
import numpy as np
import pandas as pd

'''
PANDAS - Preparing dataset
'''

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Change all column names to lowercase
df.columns = map(str.lower, df.columns)

# Convert the column ‘TotalCharges’ to a numeric format, coercing errors if necessary
df['totalcharges'] = pd.to_numeric(df['totalcharges'],errors='coerce')
df.fillna(0, inplace = True)

# For string values change spaces to an underscore symbol
df= df.applymap(lambda s:s.lower().strip().replace(' ','_') if type(s) == str else s)

# Convert the column ‘churn’ to integer format (no - 0, yes - 1).
df['churn'] = df['churn'].replace(to_replace=['no', 'yes'], value=[0, 1])

# Delete the column ‘customerid’ from the dataset.
df.drop('customerid', axis=1, inplace = True)
cat = [
    'gender','multiplelines','internetservice','onlinesecurity',
    'onlinebackup','deviceprotection','techsupport','streamingtv',
    'streamingmovies','contract','paymentmethod'
    ]
# Check for categorical columns how many different values   they have
for x in cat:
    print('#'*3,x,'#'*3)
    print(df[x].value_counts())
df.to_csv('WA_Fn-UseC_-Telco-Customer-Churn_CLEAN.csv')