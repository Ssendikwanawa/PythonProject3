import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import file, bring file path
file_path = "D:\\Ssendi\\Week7\\EpidemicpronesWK6.xlsx"

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(file_path)

# Transpose the DataFrame to swap rows and columns
df = df.set_index("District").transpose()

 # #### Pure Blue Variants:    "Blues" → Light to dark blue gradient,  "cool" → Cyan to blue,  "winter" → Blue to greenish-blue
# ####### Blue Mixed with Other Colors:  "ocean" → Deep blue to green,  "PuBu" → Purple to Blue,  "YlGnBu" → Yellow-Green to Blue,
# ##### # Diverging Blue Themes (Good for Comparisons):  "coolwarm" → Blue to red (useful for contrasts),  "RdBu" → Red to Blue, centered at white,  "bwr" → Blue-White-Red

# Set default Seaborn style with a white background
sns.set_style("white")  # This removes the dark theme and sets background to white

# Create the heatmap
plt.figure(figsize=(12, 8))  # No black background
ax = sns.heatmap(
    df,
    annot=True,
    fmt="d",
    cmap="cubehelix_r",
    cbar=False,
    linewidths=1.3,
    annot_kws={"size": 18, "color": "black"},  # Change annotation color to black
)

# Customize the title for readability
plt.title("Epidemic Prone Diseases, Wk6.", fontsize=29, weight="bold", color="black")

# Set x-axis and y-axis labels (keep empty but styled)
plt.xlabel("", fontsize=12, weight="bold", color="black")
plt.ylabel("", fontsize=12, weight="bold", color="black")

# Adjust tick colors for better readability
plt.tick_params(axis="x", labelsize=23, colors="black")  # X-axis tick labels in black
plt.tick_params(axis="y", labelsize=23, colors="black")  # Y-axis tick labels in black

# Rotate the X-axis labels for better alignment
plt.xticks(rotation=-72, ha="right", color="black")  # Rotate with alignment
plt.yticks(color="black")  # Ensure Y-axis tick labels are black

# Adjust layout to make space for caption
plt.subplots_adjust(bottom=0.3)

# Show the plot
plt.show()