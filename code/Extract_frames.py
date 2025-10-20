# code to extract frames from videos

import cv2
import os

video_path = "DJI_0050.mp4"
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

frame_interval = int(fps / 3)  # 3 frames per second

frame_count = 0
saved_frame = 4593

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_folder, f"frame_{saved_frame:04d}.png")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved {frame_filename}")
        saved_frame += 1

    frame_count += 1

cap.release()
print("Frame extraction completed.")

