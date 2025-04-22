import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from adjustText import adjust_text  # For preventing label overlapping

# Load District Shapefile
districts = gpd.read_file("C:\\Users\\Administrator\\Desktop\\uganda_districts.shp")

# Define districts in the Lango region
lango_districts = [
    "LIRA CITY", "APAC", "OTUKE", "DOKOLO", "OYAM", "KWANIA", "LIRA", "AMOLATAR", "KOLE", "ALEBTONG"
]

# Define Case Data for Affected Districts
case_data_districts = pd.DataFrame({
    "District": ["LIRA CITY", "APAC", "OTUKE", "DOKOLO", "OYAM"],
    "Cases": [7, 1, 4, 3, 4]  # Number of cases per district
})

# Assign 0 cases to non-affected districts
non_affected_districts = set(lango_districts) - set(case_data_districts["District"])
non_affected_data = pd.DataFrame({"District": list(non_affected_districts), "Cases": 0})

# Combine affected and non-affected district data
all_district_cases = pd.concat([case_data_districts, non_affected_data], ignore_index=True)

# Filter Lango districts from the shapefile
lango_geo = districts[districts["District"].isin(lango_districts)]

# Merge district-level case data with geospatial data
lango_geo = lango_geo.merge(all_district_cases, on="District", how="left")

# Add Labels for the Districts (District Name + Case Count)
lango_geo["Label"] = lango_geo["District"] + " (" + lango_geo["Cases"].astype(str) + ")"

# Calculate Centroids for Annotation
lango_geo["centroid"] = lango_geo.geometry.centroid

# Define a custom colormap explicitly with the desired colors
from matplotlib.colors import ListedColormap

custom_colors = ListedColormap(["#199bda", "#1d9bbf", "#20a4d8"])
color_bins = [0, 2, 4, 8]  # Define bins to classify case loads
lango_geo["ColorBin"] = pd.cut(lango_geo["Cases"], bins=color_bins, labels=False, include_lowest=True)

# Plot the Map
fig, ax = plt.subplots(1, 1, figsize=(18, 14))

# Plot Districts with the custom colormap
lango_geo.plot(
    column="ColorBin",
    cmap=custom_colors,  # Use the custom colormap
    linewidth=0.5,
    edgecolor="black",  # Keep district boundaries black
    legend=False,  # Disable automatic legend for manual handling
    ax=ax
)

# Annotate Districts with Labels (Only Non-Zero Cases)
district_texts = []
for _, row in lango_geo.iterrows():
    if row["Cases"] > 0:  # Only label districts with cases
        district_texts.append(
            ax.text(
                x=row.centroid.x,
                y=row.centroid.y,
                s=row["Label"],
                fontsize=16,  # Ensure proper font size
                color="black",  # Keep labels black
                fontweight="bold",
                ha="center",
                va="center"
            )
        )

# Adjust text positions to avoid overlaps
adjust_text(district_texts, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

# Add District Boundaries with a Faint Grey Line
lango_geo.boundary.plot(ax=ax, color="black", linewidth=1.0, alpha=0.7)

# Add Title and Remove Axes for a Cleaner Look
ax.set_title(f"Map of Lango Districts", fontsize=25, fontweight="bold", color="black")
ax.axis("off")  # Remove axes for a cleaner look
plt.tight_layout()

# Add Basemap (CartoDB.Positron for Better Visuals)
ctx.add_basemap(ax, crs=lango_geo.crs.to_string(), source=ctx.providers.CartoDB.Positron)

# Show the Map
plt.show()
