# Anpassen der Klassen bei falscher Klassen-Annotierung
```
# code to adapt classes of labelled files

from google.colab import drive
import os
from tqdm import tqdm

drive.mount('/content/drive')

# folders
base_folder = "/content/drive/MyDrive/ColabDatasets/YOLO"
subfolders = ["Train", "Valid", "Test"]

for sub in subfolders:
    # path to labelled txt files
    label_folder = os.path.join(base_folder, sub, "Labels")

    # target folder
    fixed_folder = os.path.join(os.path.dirname(label_folder), "labels_fixed")
    # creates folder if not exists
    os.makedirs(fixed_folder, exist_ok=True)
    # lists .txt files
    txt_files = [f for f in os.listdir(label_folder) if f.lower().endswith(".txt")]

    for filename in txt_files:
        # original file path
        old_path = os.path.join(label_folder, filename)
        # new file path
        new_path = os.path.join(fixed_folder, filename)

        with open(old_path, "r", encoding="utf-8") as f:
            # reads content of file
            lines = f.readlines()

        new_lines = []
        for line in lines:
            # removes whitespace
            line = line.strip()
            # skips empty lines
            if line == "":
                continue  
            parts = line.split()
            parts[0] = "2"  # set class to "2"
            new_lines.append(" ".join(parts))

        # writes 
        with open(new_path, "w", encoding="utf-8", newline="\n") as f:
            if new_lines:
                # writes lines
                f.write("\n".join(new_lines) + "\n")
            else:
                # creates empty file if nothing left
                f.write("")  
```
