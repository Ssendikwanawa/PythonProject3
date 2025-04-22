import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Create a sample dataset
data = {
    "District": [
        "Amolatar", "Apac", "Alebtong", "Dokolo", "Kole",
        "Lira City", "Lira District", "Oyam", "Otuke", "Kwania"
    ],
    "Completeness (%)": [95, 90, 88, 85, 92, 89, 91, 87, 86, 93],
    "Timeliness (%)": [90, 85, 80, 82, 87, 88, 86, 81, 84, 83],
    "TB Screened": [1200, 1500, 1300, 1100, 1400, 1250, 1350, 1150, 1180, 1220],
    "MTB Detected": [15, 18, 12, 10, 17, 14, 16, 11, 13, 15],
}

df = pd.DataFrame(data)


# Function for sleek gradient bar charts
def create_gradient_bar(value, max_value, color_start="#4CAF50", color_end="#81C784"):
    fig, ax = plt.subplots(figsize=(0.8, 0.15), dpi=120)  # Smaller size
    ax.barh([0], [value], color=[color_start], edgecolor="black", height=0.4)
    ax.set_xlim([0, max_value])
    ax.axis("off")
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", transparent=True)
    buf.seek(0)
    plt.close(fig)
    return f'<img src="data:image/png;base64,{base64.b64encode(buf.read()).decode("utf-8")}" />'


# Function for small pie charts (optimized size)
def create_pie_chart(value, total, color="#FFC107"):
    fig, ax = plt.subplots(figsize=(0.3, 0.3), dpi=120)  # Smaller pie
    ax.pie(
        [value, total - value],
        colors=[color, "#E0E0E0"],
        startangle=90,
        radius=0.25,
        wedgeprops={"linewidth": 0.5, "edgecolor": "#fff"}
    )
    ax.axis("equal")
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", transparent=True)
    buf.seek(0)
    plt.close(fig)
    return f'<img src="data:image/png;base64,{base64.b64encode(buf.read()).decode("utf-8")}" />'


# Add bar visuals for `Completeness` and `Timeliness`
df["Completeness Visual"] = df["Completeness (%)"].apply(lambda x: create_gradient_bar(x, 100))
df["Timeliness Visual"] = df["Timeliness (%)"].apply(
    lambda x: create_gradient_bar(x, 100, "#2196F3", "#64B5F6")
)

# Add pie visuals for TB Screened and MTB Detected
df["TB Screened Visual"] = df["TB Screened"].apply(lambda x: create_pie_chart(x, max(df["TB Screened"])))
df["MTB Detected Visual"] = df["MTB Detected"].apply(lambda x: create_pie_chart(x, max(df["MTB Detected"]), "#FF7043"))

# Select and arrange final columns for the table
df_visual = df[[
    "District", "Completeness (%)", "Completeness Visual",
    "Timeliness (%)", "Timeliness Visual",
    "TB Screened", "TB Screened Visual",
    "MTB Detected", "MTB Detected Visual"
]]

# Add custom CSS for small and compact design
table_styles = """
<style>
    body {
        font-family: "Arial", sans-serif;
        margin: 10px;
    }
    table.dataframe {
        border-collapse: collapse;
        width: 85%;  /* Reduced width for small spaces (PPT-friendly) */
        margin: 10px auto;
        border: 1px solid #ddd;
        font-size: 11px;  /* Smaller font for compact table */
    }
    table.dataframe th {
        background: #4CAF50;
        color: white;
        text-transform: uppercase;
        font-weight: bold;
        padding: 4px;  /* Compact header padding */
        text-align: center;
    }
    table.dataframe td {
        border: 1px solid #ddd;
        text-align: center;
        vertical-align: middle;
        padding: 2px;  /* Reduced cell padding */
        line-height: 1.2;  /* Compact row height */
    }
    table.dataframe td img {
        display: block;
        margin: 0 auto;
        height: 15px;  /* Limit height of visual cells */
    }
    table.dataframe tr:nth-child(even) {
        background-color: #f9f9f9;  /* Alternating row colors */
    }
    table.dataframe tr:hover {
        background-color: #f1f1f1;  /* Highlighted hover */
    }
    /* Table spanners */
    .spanner-completeness {
        background: aliceblue;
        font-size: 11px;
        font-weight: bold;
        text-align: center;
    }
    .spanner-screened {
        background: papayawhip;
        font-size: 11px;
        font-weight: bold;
        text-align: center;
    }
</style>
"""

# Add grouped headers manually for spanners
header_part = """
<tr>
    <th rowspan="2">District</th>
    <th colspan="2" class="spanner-completeness">Completeness</th>
    <th colspan="2" class="spanner-completeness">Timeliness</th>
    <th colspan="2" class="spanner-screened">TB Screened</th>
    <th colspan="2" class="spanner-screened">MTB Detected</th>
</tr>
<tr>
    <th>%</th><th>Visual</th>
    <th>%</th><th>Visual</th>
    <th>Count</th><th>Visual</th>
    <th>Count</th><th>Visual</th>
</tr>
"""

# Generate the HTML table
html_table = (
        table_styles +
        df_visual.style
        .hide(axis="index")  # Remove row indices for cleaner look
        .set_table_attributes('class="dataframe"')  # Apply CSS
        .to_html(escape=False)  # Insert rendered HTML within table
)

# Add the headers with grouped spanners
html_table = html_table.replace('<thead>', f'<thead>{header_part}')

# Save compact table to an HTML file
output_file = "compact_district_table.html"
with open(output_file, "w") as f:
    f.write(html_table)

print(f"Compact table created and saved as {output_file}.")


