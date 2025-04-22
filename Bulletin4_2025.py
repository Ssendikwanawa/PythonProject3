import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from textwrap import fill

# Load and display the image
img = mpimg.imread('C:\\Users\\Administrator\\JAN282025_epicurve.png')  # Replace with your image path

fig, ax = plt.subplots(figsize=(8, 10))  # Adjust the figure size if needed
ax.imshow(img, extent=[30, 380, 200, 480])  # Adjust the position and size of the image

# Define the text
text = ("The recent spikes from late-December suggests increased cases"
        " due to high transmission.")

# Break the text into multiple lines using textwrap
wrapped_text = fill(text, width=68)  # Automatically wrap text to fit ~60 characters per line

# Add text closer to the image
plt.text(35, 152, wrapped_text, fontsize=12,
         color="#20a4d8")  # Adjust x and y to reposition text as needed for better alignment

# Save or display the result
plt.savefig("output.png", bbox_inches='tight', dpi=80, pad_inches=0.2)  # Reduce bbox cuts with pad_inches
plt.show()
