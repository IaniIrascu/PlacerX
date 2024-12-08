import numpy as np
import cv2

# Load the image
image_path = "Harta_NYC.png"  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define HSV range for blue
lower_blue = np.array([100, 150, 50])  # Adjust as needed
upper_blue = np.array([140, 255, 255])  # Adjust as needed

# Create a mask for blue colors
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

matrix = []

if image is not None:
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define HSV range for blue
    lower_blue = np.array([90, 215, 110])    # Lower bound of blue (light and dark blues)
    upper_blue = np.array([150, 255, 190])

    # Create a mask for blue colors
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Iterate through the mask and print "blue" for each blue pixel
    for y in range(blue_mask.shape[0]):
        matrix.append([])  # Rows
        for x in range(blue_mask.shape[1]):  # Columns
            if blue_mask[y, x] > 0:
                matrix[y].append(1)  # If the pixel is blue in the mask
            else:
                matrix[y].append(0)

coords = [[40.5, 41], [-74.2, -73.6]]
np.savetxt('matrix.csv', matrix, delimiter=',', fmt='%d')

def is_on_water(lat, long, bounds = coords, matrix = matrix):
    dif_lat = bounds[0][1] - bounds[0][0]
    dif_long = bounds[1][1] - bounds[1][0]
    lat_pixel = len(matrix)
    long_pixel = len(matrix[0])
    point_y = (lat - bounds[0][0]) * lat_pixel / dif_lat
    point_x = (long - bounds[1][0]) * long_pixel / dif_long
    if not matrix[int(point_y)][int(point_x)]:
        return False
    return True

