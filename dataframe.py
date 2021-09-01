import pandas as pd
import os
import re

data = r"C:\Users\PC_User\OneDrive\Racing\Datasource"
output_dir = r"C:\Users\PC_User\OneDrive\Racing\RacingData"
file = "NSW2021_August.xlsx"
file2 = "NSW2021_PD.xlsx"
file3 = "NSW2021_PD_mod.xlsx"

path_in = os.path.join(output_dir, file2)
path_out = os.path.join(output_dir, file3)
data_in = pd.read_excel(path_in, sheet_name="Sheet1")

data_in.dropna(subset=["Horse"], inplace=True)
data_in["Position"] = pd.to_numeric(data_in.Position)
df = data_in.drop(data_in[data_in.Position == 0].index)
# data_in[data_in.Position != 0]
df[["Sect", "Sect_Time"]] = df.Race_Sectional_Time.str.split("/", expand=True)
try:
    df["Sect_Time"] = pd.to_numeric(df.Sect_Time)
except:
    pass

df["Race_Price"] = df["Race_Price"].str.replace(r"^\$|F$", "", regex=True)
try:
    df["Race_Price"] = pd.to_numeric(df.Race_Price)
except:
    pass

path = os.path.join(output_dir, file2)


df.to_excel(path_out, index=False)
