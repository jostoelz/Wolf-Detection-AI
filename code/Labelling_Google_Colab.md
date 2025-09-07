# Bilder annotieren in Google Colab
```
# preparations
!pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
!git clone https://github.com/luca-medeiros/lang-segment-anything.git
%cd lang-segment-anything
!pip install -e .
!pip install pillow
``` 
```
# code to execute once

import matplotlib.pyplot as plt
import random
from PIL import Image
import numpy as np
from lang_sam import LangSAM
import os
from google.colab import files
import cv2
from google.colab import drive
import ipywidgets as widgets
from IPython.display import display

# paths
drive.mount('/content/drive')
input_image_folder = '/content/drive/MyDrive/ColabDatasets/Images_original/'
input_check = '/content/drive/MyDrive/ColabDatasets/Check'
output_valid_folder = '/content/drive/MyDrive/ColabDatasets/YOLO/Valid/'
output_train_folder = '/content/drive/MyDrive/ColabDatasets/YOLO/Train/'
output_test_folder = '/content/drive/MyDrive/ColabDatasets/YOLO/Test/'
output_hand_labeling_folder = '/content/drive/MyDrive/ColabDatasets/Images_hand_labeling/' # needs to be hand-labeled

# initializes Language Segment-Anything
model = LangSAM()

# variables
confidence_threshold = 0.2
``` 
``` 
# code to label + show every image (bounding boxes are created from masks)

# function to iterate over each image
def iteration_images(folder):
    entries = sorted(os.scandir(folder), key=lambda e: e.name.lower())
    for entry in entries:
        if entry.is_file() and entry.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            # returns image for image
            yield entry.path

for image_path in iteration_images(input_check):
  image_filename = os.path.basename(image_path)
  # loads an image
  image = cv2.imread(image_path)
  # converts into a PIL-image
  image_pil = Image.open(image_path).convert("RGB")
  # changes the type of image to jpg
  jpg_filename = os.path.splitext(image_filename)[0] + ".jpg"
  folders = [output_train_folder, output_valid_folder, output_test_folder]
  probabilities = [0.8, 0.1, 0.1]
  # chooses between train, valid, test
  choice_folder = random.choices(folders, weights=probabilities, k=1)[0]
  images_folder = os.path.join(choice_folder, "Images")
  jpg_output_path = os.path.join(images_folder, jpg_filename)
  # saves the image
  image_pil.save(jpg_output_path, "JPEG")
  # applies Language Segment-Anything
  text_prompt = "wolves."
  results = model.predict([image_pil], [text_prompt])
  # returns size of image
  image_width, image_height = image_pil.size
  # returns the masks & scores
  scores = results[0]['scores']
  masks = results[0]['masks']
  # creates a matplotlib figure
  fig, ax = plt.subplots()
  # shows the image
  ax.imshow(image_pil)
  # creates a button for each image
  button = widgets.Button(description=f"wrong: {image_filename}")

  # creates the txt file
  txt_filename = os.path.splitext(image_filename)[0] + ".txt"
  txt_folder = os.path.join(choice_folder, "Labels")
  txt_output_path = os.path.join(txt_folder, txt_filename)
  with open(txt_output_path, "w") as f:
    for mask, score in zip(masks, scores):
      if score < confidence_threshold:
        continue
      y_coords, x_coord = np.where(mask)
      if x_coord.size == 0 or y_coords.size == 0:
        continue
      # calculates the data needed for the txt files & bounding boxes
      y_coords, x_coord = np.where(mask)
      x_min, x_max = np.min(x_coord), np.max(x_coord)
      y_min, y_max = np.min(y_coords), np.max(y_coords)
      width = x_max - x_min
      height = y_max - y_min
      x_center = (x_max + x_min) / 2 / image_width
      y_center = (y_max + y_min) / 2 / image_height
      width_normalized = width / image_width
      height_normalized = height / image_height
      # adds the rectangle to the image
      rectangle = plt.Rectangle((x_min, y_min), width, height, linewidth=2, edgecolor='red', facecolor='none')
      ax.add_patch(rectangle)
      text = f"0 {x_center:.6f} {y_center:.6f} {width_normalized:.6f} {height_normalized:.6f}"
      # writes the data into the file
      f.write(text + "\n")

  # removes the image from the origin folder
  jpg_input_path = os.path.join(input_check, image_filename)
  if os.path.exists(jpg_input_path):
    os.remove(jpg_input_path)

  plt.axis('off')
  plt.show()

  def on_button_clicked(b,
                    image_filename=image_filename,
                    image_pil=image_pil,
                    jpg_filename=jpg_filename,
                    images_folder=images_folder,
                    txt_folder=txt_folder):

    jpg_hand_label_path = os.path.join(output_hand_labeling_folder, jpg_filename)
    # saves the image
    image_pil.save(jpg_hand_label_path, "JPEG")
    # deletes incorrect images from folder
    jpg_output_path = os.path.join(images_folder, jpg_filename)
    if os.path.exists(jpg_output_path):
      os.remove(jpg_output_path)
    txt_output_path = os.path.join(txt_folder, os.path.splitext(image_filename)[0] + ".txt")
    if os.path.exists(txt_output_path):
      os.remove(txt_output_path)

  button.on_click(on_button_clicked)
  display(button)
``` 
