import pandas as pd
import numpy as np


"""
Roadblocks / TO Fix
- Choose better fields!  Dioxins seems to be 0 in this dataset?  


Demonstrate
# - merge / aggregate by company name
# - explore the data

"""

def reset_pandas_fmt():
    pd.reset_option('display.max_rows|display.max_columns|display.width')

def widen_pandas():
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 150)

widen_pandas();

# explaination of all codes and variables.
DATA_DICTIONARY = "https://www.epa.gov/sites/production/files/2021-05/documents/file_type_1a_0.pdf"

# assuming a successful download.  
# Should have guards.  
# Tab delimited
# US_1a_${YYYY}.txt
# index_col = False, or you will get off by one on the column names

df_orig = pd.read_table("./downloads/US_2019/US_1a_2019.txt", index_col=False)

"""
Strong assumptions for EXERCISE

SUPPORT ONE QUERY:
- total dioxin release per OWNER, by STATE by YEAR

OWNER  1:8  FACILITY
FACILITY 8:8 POLLUTION

71. owner 
- owns multiple facilities

9. Facility
- can only be owned by one OWNER
- produces multiple kinds of 

"""

DIOXIN_FIELDS = [
 '85. DIOXIN DISTRIBUTION 1',
 '86. DIOXIN DISTRIBUTION 2',
 '87. DIOXIN DISTRIBUTION 3',
 '88. DIOXIN DISTRIBUTION 4',
 '89. DIOXIN DISTRIBUTION 5',
 '90. DIOXIN DISTRIBUTION 6',
 '91. DIOXIN DISTRIBUTION 7',
 '92. DIOXIN DISTRIBUTION 8',
 '93. DIOXIN DISTRIBUTION 9',
 '94. DIOXIN DISTRIBUTION 10',
 '95. DIOXIN DISTRIBUTION 11',
 '96. DIOXIN DISTRIBUTION 12',
 '97. DIOXIN DISTRIBUTION 13',
 '98. DIOXIN DISTRIBUTION 14',
 '99. DIOXIN DISTRIBUTION 15',
 '100. DIOXIN DISTRIBUTION 16',
 '101. DIOXIN DISTRIBUTION 17']

FACILITY_FIELDS = [
 '9. TRIFD',
 '10. FACILITY NAME',
 '11. FACILITY STREET',
 '12. FACILITY CITY',
 '13. FACILITY COUNTY',
 '14. FACILITY STATE',
 '15. FACILITY ZIP CODE',
 '30. PUBLIC CONTACT NAME',
 '31. PUBLIC CONTACT PHONE',
 '32. PUBLIC CONTACT PHONE EXT',
 '33. PUBLIC CONTACT EMAIL',
]

OWNER_FIELDS = [
 '71. PARENT COMPANY NAME',
 '72. PARENT COMPANY D and B NR',
 '73. STANDARDIZED PARENT COMPANY NAME',
]

df = df_orig[FACILITY_FIELDS + OWNER_FIELDS + DIOXIN_FIELDS]

# might be good point to csv

# make a fact table
facts = df.melt(id_vars=FACILITY_FIELDS + OWNER_FIELDS, value_vars=DIOXIN_FIELDS)

# pivot table for  company, stat, toxic totals by state
pivot = facts.pivot_table(
    values="value", 
    index=['73. STANDARDIZED PARENT COMPANY NAME', '14. FACILITY STATE'], columns=['variable'], 
    aggfunc=np.sum)
    
pivot.to_csv(open('./artifacts/2019_US_DIOXINS.csv','w'))

