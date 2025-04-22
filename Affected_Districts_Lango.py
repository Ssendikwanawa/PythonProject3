import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from matplotlib.patches import Polygon
import math
import random

# Load the shapefile
shapefile_path = "C:\\Users\\Administrator\\Desktop\\uganda_districts.shp"  # Replace with actual path
districts = gpd.read_file(shapefile_path)

# Define the Lango region districts
lango_districts = [
    "LIRA CITY", "APAC", "OTUKE", "DOKOLO", "OYAM", "KWANIA",
    "LIRA", "AMOLATAR", "KOLE", "ALEBTONG"
]

# Filter the GeoDataFrame for just Lango region districts
lango_region = districts[districts['District'].str.upper().isin([d.upper() for d in lango_districts])]

# Reproject to Web Mercator (EPSG:3857) for compatibility with basemaps
lango_region = lango_region.to_crs(epsg=3857)

# Generate a unique color for each district
colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(len(lango_region))]
lango_region["color"] = colors


# Function to add a star-shaped compass (North Arrow)
def add_star_shape(ax, center, size):
    """Add a star-shaped north arrow at a given position."""
    # Generate star points
    num_points = 10  # Number of points for the star
    radius_outer = size  # Outer radius of the star
    radius_inner = size / 2  # Inner radius (half of outer radius)
    x_center, y_center = center

    points = []  # List to store star coordinates
    for i in range(num_points * 2):
        angle = i * math.pi / num_points  # Angle in radians
        r = radius_outer if i % 2 == 0 else radius_inner  # Alternate between outer and inner radii
        x = x_center + r * math.cos(angle)
        y = y_center + r * math.sin(angle)
        points.append((x, y))

    # Create a star using Polygon patch
    star = Polygon(points, color="grey")
    ax.add_patch(star)

    # Add "N" label above the star
    ax.text(x_center, y_center + size * 1.6, "N", fontsize=14, ha="center", color="black")

# Plot the GeoDataFrame
fig, ax = plt.subplots(figsize=(14, 10))
lango_region.plot(ax=ax, color=lango_region["color"], edgecolor="black")

# Add labels for each district without bbox
for x, y, label in zip(
        lango_region.geometry.centroid.x,
        lango_region.geometry.centroid.y,
        lango_region["District"]
):
    ax.text(x, y, label, fontsize=11, ha="center", color="black", fontweight="bold")

# Add the basemap (ESRI Satellite) without attribution
ctx.add_basemap(ax, source=ctx.providers.Esri.WorldImagery, attribution=False)

# Get map extents
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()

# Add a scale bar (in meters, for a 50-kilometer bar)
scale_bar_length = 50000  # 50 km in meters
scale_bar_pos_x = x_min + 0.05 * (x_max - x_min)  # Horizontal margin (left edge)
scale_bar_pos_y = y_min + 0.05 * (y_max - y_min)  # Vertical margin (bottom edge)

# Draw the scale bar
ax.plot(
    [scale_bar_pos_x, scale_bar_pos_x + scale_bar_length],
    [scale_bar_pos_y, scale_bar_pos_y],
    color="grey", linewidth=8
)

# Add scale bar label
ax.text(
    scale_bar_pos_x + scale_bar_length / 1.3,  # Center label
    scale_bar_pos_y + 0.01 * (y_max - y_min),  # Slightly above scale bar
    "25 km", fontsize=12, ha="center", color="black"
)

# Add a north arrow (compass) using the star shape
compass_center = (x_max - 0.1 * (x_max - x_min), y_min + 0.5 * (y_max - y_min))  # Position (top-right)
compass_size = 4000  # Adjust for size of compass (meters)
add_star_shape(ax, compass_center, compass_size)  # Add star for the arrow

# Map title
ax.set_title("Lango Region Districts", fontsize=16)

# Disable axes for clean visualization
ax.set_axis_off()

# Show the map
plt.show()
