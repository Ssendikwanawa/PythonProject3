import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from adjustText import adjust_text
import contextily as ctx
import matplotlib.colors as mcolors
from matplotlib import cm, colors
import matplotlib.pyplot as plt
import numpy as np
from sympy import false
import matplotlib.patches as mpatches  # For creating custom legend boxes

############### Recommended Red Colors:Deep Red**: Strong and attention-catching
 #### #E63946`
### Bright and Vibrant Red**: Bold and stands out
### #FF4B5C`
####Muted/Soft Red**: Softer for a professional look
### #DC5C5C`
##### Rich Burgundy Red**: Elegant and deep
#### #A11B34`
#### #Crimson Red**: Balanced intensity
#### #D72638`

# Load District Shapefile
districts = gpd.read_file("C:\\Users\\Administrator\\Desktop\\uganda_districts.shp")
print(districts.head())  # Check the first few rows of the GeoDataFrame
print(districts.columns)  # Ensure "District" is present as a column

# Ensure District names match exactly in both datasets
districts["District"] = districts["District"].str.strip().str.upper()

# Define Lango Districts in the Region
Elgon_districts = [
    "MBALE CITY", "MBALE", "MANAFA", "BULAMBULI", "BUDUDA", "TORORO",
    "NAMISINDWA", "BUSIA", "BUDAKA", "PALLISA", "BUTALEJA", "KAPCHORWA",
    "KWEEN", "SIRONKO", "BUTEBO", ""
]

# Define Case Data for Affected Districts
case_data_districts = pd.DataFrame({
    "District": ["MBALE CITY", "MBALE"],  # Affected districts
    "Cases": [1, 1]  # Corresponding case counts
})

# Assign 0 cases to non-affected districts
non_affected_districts = set(Elgon_districts) - set(case_data_districts["District"])
non_affected_data = pd.DataFrame({"District": list(non_affected_districts), "Cases": 0})

# Combine affected and non-affected district data
all_district_cases = pd.concat([case_data_districts, non_affected_data], ignore_index=True)

# Ensure District names match exactly in case data
all_district_cases["District"] = all_district_cases["District"].str.strip().str.upper()

# Filter Elgon districts from the shapefile
Elgon_geo = districts[districts["District"].isin(Elgon_districts)]

# Merge district-level case data with geospatial data
Elgon_geo = Elgon_geo.merge(all_district_cases, on="District", how="left")

# Fix invalid or missing geometries
Elgon_geo["geometry"] = Elgon_geo["geometry"].buffer(0)

# Add Labels for the Districts
Elgon_geo["Label"] = Elgon_geo["District"]

# Calculate Centroids for District Label Placement
Elgon_geo["centroid"] = Elgon_geo.geometry.centroid

# Create Ranges (Bins) for 2 Levels: "Low" and "High"
bins = [-1, 0, 1]  # Corrected bins to ensure proper assignment
labels = ["Other Districts", "Districts in Active Transmission"]  # Labels for the levels
Elgon_geo["CaseCategory"] = pd.cut(Elgon_geo["Cases"], bins=bins, labels=labels, include_lowest=True)

# Define a Custom Colormap for the Bins (Two Colors)
cmap = mcolors.ListedColormap(["#FFFFFF", "#FF0000"])  # Light red for Low, Dark red for High
norm = mcolors.BoundaryNorm(bins, cmap.N)

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Generate the Map Plot
Elgon_geo.plot(
    column="CaseCategory",  # Use the categorized column
    cmap=cmap,  # Apply the custom colormap
    linewidth=0.5,
    edgecolor="red",
    ax=ax
)

# Add District Labels (Name with Cases)
district_texts = []
for _, row in Elgon_geo.iterrows():
    district_texts.append(
        ax.text(
            x=row.geometry.centroid.x,
            y=row.geometry.centroid.y,
            s=row["Label"] if row["Cases"] > 0 else "",  # Only label districts with cases
            fontsize=11,
            color="black",
            fontweight="bold",
            ha="center",
            va="center"
        )
    )

# Add Title and Adjust Aesthetics
ax.set_title("Ebola Hot spot districts in Elgon Region, 02/Feb/25",
             fontsize=15, color="#FF0000")
ax.axis("off")  # Remove axes for a cleaner look
plt.tight_layout()

# Add the Basemap for Context
ctx.add_basemap(ax, crs=Elgon_geo.crs.to_string(),
                source=ctx.providers.CartoDB.Positron)

# Create Custom Legend (Replace built-in legend)
categories = Elgon_geo["CaseCategory"].unique()  # Get unique categories from 'CaseCategory'
colors = [cmap(i / len(categories))
          for i in range(len(categories))]  # Assign colors from colormap
# Create legend patches with black borders
legend_handles = [
    mpatches.Patch(facecolor=colors[i],
                   edgecolor="red", linewidth=0.5,
                   label=cat)
    for i, cat in enumerate(categories)
]

# Add the custom Legend to the Plot
ax.legend(
    handles=legend_handles,
    title="Legend",  # Legend tittle
    title_fontsize=12,  # Tittle fontsize
    fontsize=10,  # Label font size
    loc="lower right",  # Place the legend near the lower right inside the map boundary
    frameon=False  # Add optional box around the legend
)
# Show the Final Map
plt.show()
