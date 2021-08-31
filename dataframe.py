import pandas as pd
import os

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

# if df.Race_Price.str.endswith("F"):
#     df.Race_Price.rstrip(df.Race_Price[-1])

m = df.Race_Price.str.endswith("F")
df.loc[m] = df.loc[m].str[:-1]

path = os.path.join(output_dir, file2)


df.to_excel(path_out, index=False)
