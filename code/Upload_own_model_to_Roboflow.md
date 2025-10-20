# Upload des eigenes YOLO-Modells nach Roboflow, um dort Hilfe beim Annotieren von Hand zu erhalten
Dies ist die <a href="https://docs.roboflow.com/deploy/upload-custom-weights">Anleitung</a> dazu. 
```
# preparations
!pip install roboflow
!pip install ultralytics==8.0.196
from roboflow import Roboflow
from google.colab import drive

# paths
drive.mount('/content/drive')

rf = Roboflow(api_key="QXXXsRtDxBQKaOoHIeU1")
workspace = rf.workspace("wolfdetectionai")

workspace.deploy_model(
  model_type="yolov8",
  model_path="/content/drive/MyDrive/ColabDatasets/Training/Results",
  project_ids=["test-0kjud"],
  model_name="YOLO-Modell-Test"
)
```
