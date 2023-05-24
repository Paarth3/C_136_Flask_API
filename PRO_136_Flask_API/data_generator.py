import pandas as pd

df = pd.read_csv('Gravity_Dist_Support.csv')
df_list = df.values.tolist()

data = []
for row in df_list:
    temp_dict = {
        "Name" : str(row[0]),
        "Distance": float(row[1]), 
        "Mass": float(row[2]),
        "Radius": float(row[3]),
        "Gravity": float(row[4])
    }
    data.append(temp_dict)