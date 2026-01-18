# Instructions for running your own AI on the Raspberry Pi:
1) Load the best.pt file into the yolo folder
2) Open the yolo folder in the terminal
3) Open the virtual environment:
```
source venv/bin/activate
```
4) Run the model on a folder containing images:
```
python yolo_detect.py --model=Final/best.pt --source images
```
6) To measure the speed of the model, type:
```
python3 speed_test.py
```
 
