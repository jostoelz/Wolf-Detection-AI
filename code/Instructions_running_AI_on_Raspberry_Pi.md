# Anleitung, um eigene KI auf dem Raspberry Pi laufen zu lassen:
1) Lade best.pt Datei in den yolo-Ordner
2) Öffne yolo-Ordner im Terminal
3) tippe: source venv/bin/activate
4) tippe: python yolo_detect.py --model=best.pt --source images
5) um Geschwindigkeit zu messen, tippe: python3 speed_test.py
