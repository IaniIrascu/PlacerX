# Python program to get a google map 
# image of specified location using 
# Google Static Maps API

def is_on_water(lat, long, bounds, matrix):
    dif_lat = bounds[0][1] - bounds[0][0]
    dif_long = bounds[1][1] - bounds[1][0]
    lat_pixel = len(matrix)
    long_pixel = len(matrix[0])
    print(lat_pixel)
    print(long_pixel)
    point_y = (lat - bounds[0][0]) * lat_pixel / dif_lat
    point_x = (long - bounds[1][0]) * long_pixel / dif_long
    print(point_y)
    print(point_x)
    if not matrix[int(point_y)][int(point_x)]:
        return True
    return False
# Example usage:
# importing required modules
import numpy as np
import cv2

# Load the image
image_path = "Untitled.png"  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define HSV range for blue
lower_blue = np.array([100, 150, 50])  # Adjust as needed
upper_blue = np.array([140, 255, 255])  # Adjust as needed

# Create a mask for blue colors
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Check if any blue pixels exist
if cv2.countNonZero(blue_mask) > 0:
    print("The image contains some kind of blue.")
else:
    print("No blue detected in the image.")

matrix = []

if image is not None:
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define HSV range for blue
    lower_blue = np.array([90, 50, 50])    # Lower bound of blue (light and dark blues)
    upper_blue = np.array([180, 255, 255])

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
else:
    print("Failed to load the image. Please check the file path.")

coords = [[40.6, 40.9], [-74.1, -73.7]]

np.savetxt('matrix.csv', matrix, delimiter=',', fmt='%d')