# Training eines YOLO-Modells in Google Colab mit eigenem Datenset

Zuest habe ich ein neues Notebook in Google Colab erstellt. Es muss unter "Laufzeit", "Laufzeittyp" eine GPU ausgewählt werden. Dann habe ich den folgenden Code ausgeführt, um das YOLO-Modell von ultralytics zu importieren. 
``` 
!pip install ultralytics  
from ultralytics import YOLO
```
Anschliessend wurde das eigene Datenset von Roboflow importiert:
``` 
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="QXXXsRtDxBQKaOoHIeU1")
project = rf.workspace("wolfdetectionai").project("test-0kjud")
version = project.version(1)
dataset = version.download("yolov8")
```
Danach war es möglich, das YOLO-Modell mit dem eigenen Datensatz zu trainieren:
```
import os

dataset = version.download("yolov8")
dataset_dir = dataset.location  # Assuming 'dataset' has an attribute 'location' for the download path
data_yaml_path = os.path.join(dataset_dir, "data.yaml")
model = YOLO("yolov8n.pt")  # YOLOv8 Nano als Basis
model.train(data=data_yaml_path, epochs=50, batch=16, imgsz=640)
```
Mit dem nachfolgenden Code kann das trainierte Modell validiert werden:
```
model.val()
```
Um ein externes Bild hereinzuladen, kann der folgende Code ausgeführt werden:
```
from google.colab import files
uploaded = files.upload()
```
Nun kann das Modell auf dem importierten Bild laufen gelassen werden, um auch die Robustheit des Modells zu ermitteln:
```
model.predict("/content/{Name_Bild}.png", save=True, conf=0.5)
```
Schlussendlich kann das Bild inkl. den Bounding Boxen heruntergeladen werden:
```
import os
from google.colab import files

result_folder = '/content/runs/detect/train43'
os.listdir(result_folder)
files.download(f"{result_folder}/{Name_Bild}.jpg")
```
