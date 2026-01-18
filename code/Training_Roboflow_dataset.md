# Training a YOLO model in Google Colab with a dataset from Roboflow

First, I created a new notebook in Google Colab. A GPU must be selected under ‘Runtime’, ‘Runtime type’. Then I ran the following code to import the YOLO model from ultralytics.
``` 
!pip install ultralytics  
from ultralytics import YOLO
```
Then, Roboflow's own data set was imported:
``` 
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="QXXXsRtDxBQKaOoHIeU1")
project = rf.workspace("wolfdetectionai").project("test-0kjud")
version = project.version(1)
dataset = version.download("yolov8")
```
After that, it was possible to train the YOLO model with our own data set:
```
import os

dataset = version.download("yolov8")
dataset_dir = dataset.location
data_yaml_path = os.path.join(dataset_dir, "data.yaml")
model = YOLO("yolov8n.pt")
model.train(data=data_yaml_path, epochs=50, batch=16, imgsz=640)
```
The trained model can be validated using the following code:
```
model.val()
```
To load an external image, the following code can be executed:
```
from google.colab import files
uploaded = files.upload()
```
Now the model can be run on the imported image to determine the robustness of the model:
```
model.predict("/content/{Name_Bild}.png", save=True, conf=0.5)
```
Finally, the image including the bounding boxes can be downloaded:
```
import os
from google.colab import files

result_folder = '/content/runs/detect/train43'
os.listdir(result_folder)
files.download(f"{result_folder}/{Name_Bild}.jpg")
```
