# %%
import pandas as pd

filename = r"data\complete\NESP_D3_Tier3_nationalscale_reef.csv"

df = pd.read_csv(filename, delimiter=",")
# %%
df.columns
# Index(['FID', 'NATIVE_CL', 'IMAS_CL', 'DATASET', 'CUSTODIAN', 'REGION',\\
# 'TIER_ID', 'OBJNAM', 'WATLEV', 'geom'], dtype='object')
# %%
df.shape
# (14590, 10)
# %%
df["CUSTODIAN"].unique()
# array(['Great Barrier Reef Marine Park', 'Australian Hydrographic Office'],dtype=object)

# %%
# creating df only for Great Barrier Reef Marine Park
df_gbr = df[df["CUSTODIAN"] == "Great Barrier Reef Marine Park"]

# %%
df_gbr.shape
# (3862, 10)


df_gbr["NATIVE_CL"].unique()
# array(['Reef'], dtype=object)
# as there is only one NATIVE_CL, dropping this column
df_gbr = df_gbr.drop("NATIVE_CL", axis=1)

df_gbr["IMAS_CL"].unique()
# array(['Reef'], dtype=object)
# as there is only one IMAS_CL, dropping this column
df_gbr = df_gbr.drop("IMAS_CL", axis=1)

df_gbr["DATASET"].unique()
# array(['gbr_reefs.shp'], dtype=object)
# as there is only one DATASET, dropping this column
df_gbr = df_gbr.drop("DATASET", axis=1)

# dropping CUSTODIAN

df_gbr["REGION"].unique()
# array(['QLD'], dtype=object)
# as there is only one REGION, dropping this column
df_gbr = df_gbr.drop("REGION", axis=1)

df_gbr["TIER_ID"].unique()
# array([3], dtype=int64)
# as there is only one DATASET, dropping this column
df_gbr = df_gbr.drop("TIER_ID", axis=1)

df_gbr["OBJNAM"].value_counts()
df_gbr["OBJNAM"].nunique()  # 1579


df_gbr[df_gbr["WATLEV"].notnull()]
# all the values are NaN


# %%

import pandas as pd

filename = r"data\complete\NESP_D3_Tier3_nationalscale_reef.csv"

df = pd.read_csv(filename, delimiter=",")
