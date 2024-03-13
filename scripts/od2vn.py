import matplotlib.pyplot as plt
import numpy as np
import pygame
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import os
import argparse


# Adding argument parser
parser = argparse.ArgumentParser(description='Object detection with YOLO')
parser.add_argument('--image', type=str, help='Path to input image')
parser.add_argument('--model', type=str, help='Path to YOLO model')
args = parser.parse_args()

# Check if the paths are provided, otherwise, use default paths
image_path = args.image if args.image else 'data/images/dog_bike_car.jpg'
model_path = args.model if args.model else 'models/yolov8n.pt'

model = YOLO(model_path)  # Load the model using provided or default path

# Output directories
output_image_dir = "outputs/images"
output_voice_dir = "outputs/voices"
output_diagrams_dir = "outputs/diagrams"
output_videos_dir = "outputs/videos"

# Perform object detection on an image
results = model(image_path)

# Load the image
image = Image.open(image_path)
W, H = image.size  # Get the width and height of the image

# Image storage path with detected objects
# Create the directory if it does not exist
os.makedirs(output_image_dir, exist_ok=True)

# Extracting input file name without extension
input_file_name = os.path.splitext(os.path.basename(image_path))[0]

# Defining the output image path
output_image_path = os.path.join(
    output_image_dir, f"detected_{input_file_name}.jpg")

# # Defining the output videos path
# output_videos_path = os.path.join(
#     output_videos_dir, f"detected_{input_file_name}.???")

result = results[0]     # Get the first result
len(result.boxes)       # Number of detected objects
box = result.boxes[0]   # Get the first detected object


# **************************************************************
# Iterate over detected objects, extract class ID, coordinates, and confidence
# **************************************************************
# for box in result.boxes:
#   class_id = result.names[box.cls[0].item()]
#   cords = box.xyxy[0].tolist()
#   cords = [round(x) for x in cords]
#   conf = round(box.conf[0].item(), 2)
#   print("Object type:", class_id)
#   print("Coordinates:", cords)
#   print("Probability:", conf)
#   print("---")


# **************************************************************
#   Determining the relative position of the object in the image
# **************************************************************
# Define a function to determine the relative position of the object in the image
def get_position(cords, W, H):
    centerX, centerY = (cords[0] + cords[2]) / 2, (cords[1] + cords[3]) / 2
    if centerX < W / 3:
        x_pos = "left"
    elif centerX < 2 * W / 3:
        x_pos = "center"
    else:
        x_pos = "right"

    if centerY < H / 3:
        y_pos = "top"
    elif centerY < 2 * H / 3:
        y_pos = "mid"
    else:
        y_pos = "bottom"

    return f"{y_pos} {x_pos}"


# **************************************************************
#                   Generate a list of objects,
#       their relative positions and detection probability
# **************************************************************
detected_objects = []
for box in result.boxes:
    class_id = result.names[box.cls[0].item()]
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    conf = round(box.conf[0].item(), 2)  # Probability of diagnosis
    position = get_position(cords, W, H)
    detected_objects.append(
        f"{class_id} with probability {conf} on the {position}")

# Convert the diagnosis list to a text string
description = ', '.join(detected_objects)
# print(description)


# **************************************************************
#           Generate an audio file from the description
# **************************************************************
myobj = gTTS(text=description, lang='en', slow=False)
os.makedirs(output_voice_dir, exist_ok=True)
audio_file = os.path.join(output_voice_dir, "detected_objects.mp3")
myobj.save(audio_file)

# pygame initialization
pygame.mixer.init()

# Load and play the audio file
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

# A loop to wait for the music to end
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


# **************************************************************
#           Save image with bounding boxes
# **************************************************************

# Display the image with bounding boxes in a py file
# plt.imshow(result.plot(), interpolation='nearest')
# plt.show()

# plot the image with bounding boxes in ipython file
# Image.fromarray(result.plot()[:, :, ::-1])

# Assuming `result.plot()` returns an RGB image as a NumPy array
# If the result is BGR (like in OpenCV), you might need to convert it using `[:,:,::-1]`
img_array = result.plot()

# Convert the NumPy array to a PIL Image object
img = Image.fromarray(img_array)
img.show()
img.save(output_image_path)

print(f"Image saved to {output_image_path}")
