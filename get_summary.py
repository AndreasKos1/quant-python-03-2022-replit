
import pandas as pd
#load data file and assign it
surveys_df = pd.read_csv("surveys.csv")
#describe weight column
desc_weight = surveys_df["weight"].describe()
#print out summary stats for weight 
print(desc_weight)