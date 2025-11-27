# Anleitung, um eigene KI auf dem Raspberry Pi laufen zu lassen:
1) Lade best.pt Datei in den yolo-Ordner
2) Öffne yolo-Ordner im Terminal
3) Öffne das virtual environment:
``` 
source venv/bin/activate
``` 
4) Lasse das Modell auf einen Ordner mit Bildern laufen:
``` 
python yolo_detect.py --model=Final/best.pt --source images
``` 
6) Um die Geschwindigkeit des Modells zu messen, tippe:
```
python3 speed_test.py
``` 
