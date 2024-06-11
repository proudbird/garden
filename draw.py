from PIL import Image, ImageDraw

# Function to draw perspective grid
def draw_perspective_grid(image, horizon_y, vp_left_x, vp_right_x):
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Draw horizon line
    draw.line((0, horizon_y, width, horizon_y), fill="black")

    # Draw perspective lines from left vanishing point
    for y in range(0, height, 20):
        draw.line((vp_left_x, horizon_y, 0, y), fill="black")
        draw.line((vp_right_x, horizon_y, width, y), fill="black")

    return image

# Function to draw a cube in perspective
def draw_cube(draw, vp_left, vp_right, start_point, size):
    sx, sy = start_point
    left_vp_x, horizon_y = vp_left
    right_vp_x, _ = vp_right

    # Front face (rectangle)
    front_top_right = (sx + size, sy)
    front_bottom_left = (sx, sy + size)
    front_bottom_right = (sx + size, sy + size)

    draw.polygon([start_point, front_top_right, front_bottom_right, front_bottom_left], outline="blue")

    # Perspective lines to vanishing points
    back_top_left = (left_vp_x, horizon_y)
    back_top_right = (right_vp_x, horizon_y)

    back_bottom_left = (left_vp_x, horizon_y + size)
    back_bottom_right = (right_vp_x, horizon_y + size)

    # Connect front face to back face
    draw.line([start_point, back_top_left], fill="red")
    draw.line([front_top_right, back_top_right], fill="red")
    draw.line([front_bottom_left, back_bottom_left], fill="red")
    draw.line([front_bottom_right, back_bottom_right], fill="red")

    # Draw back face (rectangle)
    draw.polygon([back_top_left, back_top_right, back_bottom_right, back_bottom_left], outline="green")

# Create an image
image = Image.new("RGB", (800, 600), "white")
horizon_y = 300
vp_left_x = 200
vp_right_x = 600

# Draw the grid
image = draw_perspective_grid(image, horizon_y, vp_left_x, vp_right_x)

# Initialize drawing
draw = ImageDraw.Draw(image)

# Draw a cube in perspective
draw_cube(draw, (vp_left_x, horizon_y), (vp_right_x, horizon_y), (400, 200), 100)

# Save and display the image
image.save("perspective_drawing.png")
image.show()
