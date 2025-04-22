import os
import base64
import io
import pandas as pd
import plotly.graph_objects as go

# Data preparation
data = {
    "District": ["Alebtong", "Amolatar", "Apac"],
    "Percentage_Tested": [22, 100, 100],  # Ensure these are numeric
    "Percentage_Pos_Treated": [90, 100, 100],  # Ensure these are numeric
    "Completeness": [65, 18, 29],
    "Timeliness": [30, 12, 26],
    "MSB": [1, 1, 0],  # Macerated Still Births
    "FSB": [0, 3, 1],  # Fresh Still Births
    "END": [2, 0, 2],  # Early Neonatal Deaths
}

# Create a DataFrame
df = pd.DataFrame(data)


# Define the function to create Base64-encoded charts
def create_base64_charts(row):
    """
    Generate individual charts for each row and encode them as Base64.
    """
    try:
        district = row["District"]
        completeness = row["Completeness"]
        timeliness = row["Timeliness"]

        # Pie Chart for Perinatal Deaths
        pie_chart = go.Figure(data=[go.Pie(
            labels=["MSB", "FSB", "END"],  # Death labels
            values=[row["MSB"], row["FSB"], row["END"]],  # Death values
            marker=dict(colors=["#ff9999", "#66b3ff", "#99ff99"])
        )])
        pie_chart.update_layout(
            width=200,
            height=200,
            title_text=f"{district} - Perinatal Deaths"
        )

        # Convert Pie Chart to Base64
        with io.BytesIO() as pie_image:
            pie_chart.write_image(pie_image, format="png")
            pie_base64 = base64.b64encode(pie_image.getvalue()).decode()

        # Bar Chart for Completeness and Timeliness
        bar_chart = go.Figure()
        bar_chart.add_trace(go.Bar(
            x=["Completeness", "Timeliness"],
            y=[completeness, timeliness],
            marker=dict(color=["#008080", "#FFA07A"])
        ))
        bar_chart.update_layout(
            width=300,
            height=200,
            title_text=f"{district} - Reporting Rates"
        )

        # Convert Bar Chart to Base64
        with io.BytesIO() as bar_image:
            bar_chart.write_image(bar_image, format="png")
            bar_base64 = base64.b64encode(bar_image.getvalue()).decode()

        # Return Base64 data for both charts
        return {
            "Pie Chart": pie_base64,
            "Bar Chart": bar_base64,
        }
    except Exception as e:
        print(f"Error creating charts for {row['District']}: {e}")
        return {
            "Pie Chart": None,
            "Bar Chart": None,
        }


# Generate visuals for each row in the DataFrame
print("Generating visuals for each district...")
visuals = df.apply(create_base64_charts, axis=1)
print("Visuals created successfully.")


# Create the Plotly table with embedded visuals
def create_plotly_table_with_visuals(df, visuals):
    """
    Create a Plotly table embedding Base64 charts dynamically.
    """
    try:
        table_data = go.Figure(data=[go.Table(
            columnwidth=[1, 3, 2, 3],  # Column widths
            header=dict(
                values=[
                    "District", "Charts", "Percentage_Tested", "Percentage_Pos_Treated"
                ],
                fill_color="lightblue",
                align="center",
                font=dict(color="black", size=12)
            ),
            cells=dict(
                values=[
                    df["District"],  # District names
                    [
                        f'<div style="text-align:center">'
                        f'<img src="data:image/png;base64,{visual["Pie Chart"]}" style="width:100px;height:100px;"><br>'
                        f'<img src="data:image/png;base64,{visual["Bar Chart"]}" style="width:150px;height:100px;">'
                        f'</div>' if visual["Pie Chart"] and visual["Bar Chart"] else "Error in chart generation"
                        for visual in visuals
                    ],  # Embedded Pie and Bar Charts
                    df["Percentage_Tested"],  # Percentage Tested
                    df["Percentage_Pos_Treated"],  # Percentage Positive Treated
                ],
                align="center",
                font=dict(color="black", size=11),
                fill_color="white",
                height=100
            )
        )])

        table_data.update_layout(
            title_text="District Reporting Data with Embedded Charts",
            height=800,
            width=1000
        )
        return table_data

    except Exception as e:
        print(f"Error generating table: {e}")
        return None


# Generate the table
print("Generating the table...")
table_data = create_plotly_table_with_visuals(df, visuals)

if table_data:
    print("Table created successfully.")

    # Save the table as an HTML file and open it automatically
    output_file = "output.html"
    print(f"Saving the HTML file to {output_file}...")
    table_data.write_html(output_file, auto_open=True)
    print("HTML file saved successfully.")
else:
    print("Could not create the table.")

# Print working directory
print(f"Current working directory: {os.getcwd()}")
