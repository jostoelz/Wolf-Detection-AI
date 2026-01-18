# Training a YOLO model in Google Colab with your own dataset
``` 
!pip install ultralytics
from ultralytics import YOLO
``` 

``` 
# code to train the model

from google.colab import drive
from ultralytics import YOLO
from google.colab import files

# paths
drive.mount('/content/drive')

# loads model
model = YOLO("yolov8m.pt")

# starts training
model.train(data='/content/drive/MyDrive/ColabDatasets/Training/data.yaml', epochs=100, imgsz=640, batch=32)

# creates folder and saves the model there
!mkdir /content/my_model
!cp /content/runs/detect/train/weights/best.pt /content/my_model/my_model.pt
!cp -r /content/runs/detect/train /content/my_model

# downloads folder as a zip file
%cd /content/my_model
!zip /content/my_model.zip my_model.pt
!zip -r /content/my_model.zip train
%cd /content
files.download('/content/my_model.zip')
``` 

``` 
# code to test the trained model

from ultralytics import YOLO
from IPython.display import Image, display
import os

# paths
drive.mount('/content/drive')
img_folder = "/content/drive/MyDrive/ColabDatasets/Training/Neu/"

# loads model
model = YOLO("runs/detect/train2/weights/best.pt")

# applies the model + saves the results
results = model.predict(source=img_folder, save=True)
output_folder = results[0].save_dir

# shows the results
for img_file in os.listdir(output_folder):
    display(Image(filename=os.path.join(output_folder, img_file)))
``` 
