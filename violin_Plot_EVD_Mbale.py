# Re-import libraries after kernel reset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare the data
data = {
    "Time": list(range(1, 12)),
    "ACS_Alerts": [2.416667, 2.333333, 2.25, 2.166667, 2.083333, 2.0, 1.916667, 1.833333, 1.75, 1.666667, 1.583333],
    "Early_Alerts": [5.643443, 5.180328, 4.717213, 4.254098, 3.790984, 3.327869, 2.864754, 2.401639, 1.938525, 1.47541, 1.012295],
    "Ring_Alerts": [1.392857, 1.928571, 2.464286, 3.0, 3.535714, 4.071429, 4.607143, 5.142857, 5.678571, 6.214286, 6.75]
}

df = pd.DataFrame(data)

# Melt data into long format
long_df = df.melt(id_vars=["Time"], var_name="Intervention", value_name="Alerts")
long_df["Intervention"] = long_df["Intervention"].replace({
    "ACS_Alerts": "ACS",
    "Early_Alerts": "Early Response",
    "Ring_Alerts": "Ring Sweep"
})

# Custom color mapping
color_map = {
    "Early Response": "#ADD8E6",  # light blue
    "Ring Sweep": "#C8E6C9",      # very light green
    "ACS": "#F4C2C2"              # light red/tan
}

# Plot
plt.figure(figsize=(8, 4))
sns.violinplot(data=long_df, x="Intervention", y="Alerts", hue="Intervention",
               palette=color_map, inner="box", linewidth=1.2)
sns.stripplot(data=long_df, x="Intervention", y="Alerts", color='black', jitter=0.2, size=5, alpha=0.6)

plt.title("Variance Check: Violin Plot of Alerts by Intervention", fontsize=18)
plt.xlabel("Intervention Type", fontsize=14)
plt.ylabel("Number of Alerts", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.tight_layout()

plt.show()
