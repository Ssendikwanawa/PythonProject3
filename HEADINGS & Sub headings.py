from PIL import Image, ImageDraw, ImageFont

# Define size, font, and colors
width, height = 585, 90
background_color = "#1d9bbf"  # Background fill color
text_color = "white"  # Main text color
shadow_color = "gray"  # Shadow color for 3D effect
font_size = 49
corner_radius = 20  # Radius for rounded corners

# Create a blank image (transparent background for flexible editing)
image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Draw the rounded rectangle with background and shadow
draw = ImageDraw.Draw(image)

# Draw shadow rectangle (slightly offset)
shadow_offset = (5, 5)  # Shadow offset in (x, y)
shadow_rectangle = [shadow_offset[0], shadow_offset[1], width - shadow_offset[0], height - shadow_offset[1]]
draw.rounded_rectangle(shadow_rectangle, radius=corner_radius, fill=shadow_color)

# Draw main background rectangle
main_rectangle = [0, 0, width, height]
draw.rounded_rectangle(main_rectangle, radius=corner_radius, fill=background_color)

# Load a font (ensure you have a valid TTF file path or use ImageFont.load_default())
font = ImageFont.truetype("arial.ttf", font_size)  # Replace with a valid .ttf font path

# Define the text to draw
text = "Event Based Surveillance"

# Calculate the position to center the text
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]  # Width and height of text
text_x = (width - text_width) // 1.5
text_y = (height - text_height) // 1.5

# Draw the shadow text (slightly offset)
draw.text((text_x + 2, text_y + 2), text, fill=shadow_color, font=font)

# Draw the main text
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save or display the final image
image.show()  # Display in the default image viewer
image.save("styled_text_with_shadow.png")  # Save as a file

from PIL import Image, ImageDraw, ImageFont
import io
import tkinter as tk  # Tkinter for clipboard access

# Your existing image generation code...

# After saving the image, copy it to the clipboard
# (Replacing "image.save" with clipboard functionality)
output = io.BytesIO()
image.save(output, format="PNG")
clipboard_image = output.getvalue()

# Use Tkinter to copy the image to the clipboard
root = tk.Tk()
root.withdraw()  # Hide the main Tkinter window
root.clipboard_clear()
root.clipboard_append(clipboard_image)
root.update()  # Puts image in clipboard
root.destroy()  # Clean up