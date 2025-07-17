import pyreadstat
import pandas as pd
import matplotlib.pyplot as plt

# Read raw data files for Iron (Fe), Manganese (Mn), and Glycated Hemoglobin (HbA1c)
fe_data, _ = pyreadstat.read_xport("FETIB_J.XPT")    # Iron: LBDTIBSI
mn_data, _ = pyreadstat.read_xport("PBCD_J.XPT")     # Manganese: LBDBMNSI
hbA1c_data, _ = pyreadstat.read_xport("GHB_J.XPT")   # HbA1c: LBXGH

# Merge datasets on the participant sequence number (SEQN)
df = fe_data.merge(mn_data, on="SEQN").merge(hbA1c_data, on="SEQN")

# Select required columns and drop rows with missing values
df = df[["LBDTIBSI", "LBDBMNSI", "LBXGH"]].dropna()

# Filter out invalid zero or negative values for Fe and Mn
df = df[(df["LBDTIBSI"] > 0) & (df["LBDBMNSI"] > 0)]

# Calculate the Iron to Manganese ratio (Fe/Mn)
df["Fe_Mn_Ratio"] = df["LBDTIBSI"] / df["LBDBMNSI"]

# Define diabetes status based on HbA1c threshold (≥ 6.5%)
df["Diabetes"] = df["LBXGH"] >= 6.5

# Bin Fe/Mn ratio into 10 intervals
df["FeMn_bin"] = pd.cut(df["Fe_Mn_Ratio"], bins=10)

# Calculate diabetes prevalence within each Fe/Mn ratio bin
rate_df = df.groupby("FeMn_bin")["Diabetes"].mean().reset_index()

# Extract midpoints of each bin for plotting
rate_df["FeMn_mid"] = rate_df["FeMn_bin"].apply(lambda x: x.mid)

# Plot the relationship between Fe/Mn ratio and diabetes prevalence
plt.figure(figsize=(10, 6))
plt.plot(rate_df["FeMn_mid"], rate_df["Diabetes"], marker="o")
plt.xlabel("Fe / Mn Ratio")
plt.ylabel("Diabetes Prevalence")
plt.title("Fe / Mn Ratio vs Diabetes Prevalence")
plt.grid(True)
plt.tight_layout()
plt.show()
