import cv2
import torch
from depth_anything_v2.dpt import DepthAnythingV2
import matplotlib.pyplot as plt
import time
import os

# --- Konfiguration ---
input_image_path = 'frame_17946.png' # Passen Sie dies an Ihren Bildpfad an
checkpoint_path = 'checkpoints/depth_anything_v2_metric_vkitti_vits.pth'

model_configs = {
    'vits': {'encoder': 'vits', 'features': 64, 'out_channels': [48, 96, 192, 384]},
}

encoder = 'vits' 
dataset = 'vkitti' 
max_depth = 80 
# --- Ende Konfiguration ---

if not os.path.exists(input_image_path):
    print(f"Fehler: Bilddatei nicht gefunden unter {input_image_path}")
    exit()
if not os.path.exists(checkpoint_path):
    print(f"Fehler: Checkpoint-Datei nicht gefunden unter {checkpoint_path}")
    exit()

print("1. Modell laden...")
# Das Modell wird explizit auf die CPU gemappt, was auf dem Pi die einzige Option ist
model = DepthAnythingV2(**{**model_configs[encoder], 'max_depth': max_depth})
model.load_state_dict(torch.load(checkpoint_path, map_location='cpu'))
model.eval()

print("2. Bild laden und Inferenz starten...")
raw_img = cv2.imread(input_image_path)
if raw_img is None:
    print("Fehler: Bild konnte nicht geladen werden.")
    exit()

start_time = time.time()

# --- Die eigentliche Inferenz ---
with torch.no_grad():
    depth = model.infer_image(raw_img) # HxW Tiefenkarte in Metern in numpy
# -----------------------------

end_time = time.time()
inference_time = end_time - start_time

print(f"3. Inferenz abgeschlossen in {inference_time:.2f} Sekunden.")

# 4. Ergebnis anzeigen (optional, kann auf dem Pi langsam sein)
plt.imshow(depth, cmap="plasma")
plt.colorbar(label="Tiefe (m)")
plt.title(f"Depth-Anything-V2 (vits) auf Raspberry Pi\nZeit: {inference_time:.2f}s")
plt.savefig("depth_output_pi.png")
print("4. Tiefenkarte als depth_output_pi.png gespeichert.")
# plt.show() # Kann die Grafikumgebung des Pi überfordern
