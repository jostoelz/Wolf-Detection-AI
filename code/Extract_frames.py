import cv2
import os

video_path = "Test_extract_frames.mp4"  
output_folder = "frames"  
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))

frame_count = 0
saved_frame = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break  

    if frame_count % fps == 0:
        frame_filename = os.path.join(output_folder, f"frame_{saved_frame:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved {frame_filename}")
        saved_frame += 1

    frame_count += 1

cap.release()
print("Frame extraction complete.")
