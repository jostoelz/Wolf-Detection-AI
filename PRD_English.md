# Abstract
In this project, I am developing an Artificial Intelligence that recognizes wolves from a bird's-eye view and can return the position of the wolf on the image. The AI should be able to run independently on a Raspberry Pi.

# Program Description
## Work Steps
### Dataset Creation
The first step is to collect wolf footage. For this, I must collaborate with a zoo that owns wolves. I also need to record sheep footage so the AI becomes more reliable in distinguishing between wolves and sheep. Once I have the footage, I load the video material into a Python file in VS Code. Using OpenCV, this file extracts the current frame every half second, for example, and saves it as a new image. In this way, several thousand photos can be created from just a few video files. Afterward, the resolution of the images may need to be reduced so that the AI does not become too large and can later function on a Raspberry Pi. OpenCV in VS Code can also be used for this. The next step is to label the images with the position of the wolf/sheep. Finally, the dataset is completed with an equal amount of image material, but this time with non-wolf/sheep images, and labeled as "something else."

#### Zoo Selection
Zoos already contacted include Tierpark Dählhölzli Bern, Wilhelma Tierpark in Stuttgart, Wildnispark Zürich Langenberg, Wildpark Bruderhaus in Winterthur, Tierpark Goldau, Tierpark Lange Erlen in Basel, Sikypark in Crémines, Juraparc Vallorbe, Parc Animalier de Sainte-Croix in France, Zoo la Garenne in Vaud, Alpenzoo in Innsbruck, Wildpark Feldkirch, and the Alternative Wolf and Bear Park in the Black Forest.

Last update on 05.03.25: Tierpark Dählhölzli in Bern offered that a zookeeper would take 30 minutes of footage for me using his drone. Most recently, I sent them a description of exactly what I would need. On 06.03., I mailed the package with the microSD card for the recordings. The zookeeper will now record the videos and send the microSD card back to me. <br> 
Last update on 06.04.25: Due to technical problems with the drone's takeoff, Tierpark Dählhölzli is unable to record video material with a drone after all. I have now accepted their offer to try the recordings with a stationary device. They will now return the recordings with the microSD card. In return, I am allowed to visit Tierpark Lange Erlen in Basel on 10.04.25 to carry out the recordings with my own drone.

#### Recording Wolf Image Material
In principle, there are two approaches for recording the image material.
One possibility would be to fly a drone at a greater height over the wolves. Alternatively, a stationary camera could be installed at an elevated point for a limited period to film the wolves from above. For both options, I need about 1.5 hours of video material in which the wolf is visible from a bird's-eye view. It does not matter how many individual videos the recordings are distributed across – it is only important that the drone / the wolf (in the case of a stationary device) does not stay in one place but is in motion to capture different situations and viewing angles. I leave the height of the recordings to the local conditions, as wolf enclosures are often heavily forested, which, for example, severely limits drone flight. The wolf should simply be clearly recognizable in the recordings.
<br>
<br>
Insights from recordings at Tierpark Lange Erlen:<br>
Everything went exceptionally well, and I was able to make a few, but very good recordings. We observed the wolf enclosure continuously from 10:30 AM to shortly before 6:00 PM. However, the wolves hardly showed themselves from midday onwards, as they mostly retreated under the trees to sleep. In the morning, on the other hand, they were significantly more active.
It was a bit of a shame that I did not receive enough video material for my project. On the other hand, the quality of the existing video material is optimal for my work. The following <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EtW27rpb1ZlBpWLmhlBq-AABzyn67NjPXbQeZUokLfIz_g?e=WHIiu2">link</a> shows the recordings in Tierpark Lange Erlen.
<br>
<br>
Insights from recordings at Wildpark Feldkirch:<br>
To supplement my video material, I visited Wildpark Feldkirch. The wolf enclosure was heavily forested, which somewhat restricted the flights. However, the behavior of the wolves was very different from that in Tierpark Lange Erlen. The two wolves moved and showed themselves continuously. The visibility conditions were also different from those already collected, which is why they help me further. I would be allowed to visit both Tierpark Lange Erlen and Wildpark Feldkirch again if necessary. The following <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EoVr0IEm8wtJmrYriqSY3oIBNzjmjKQcn4gmxEIL_Skm_Q?e=1lfLn1">link</a> shows the recordings in Wildpark Feldkirch.

#### Recording Sheep Image Material
Recording the sheep image material is somewhat easier to organize. Here, it is possible to ask a farmer if I may fly a drone over his flock of sheep. There are sheep, for example, near Roggwil, near Stachen, near Güttingen and between Frasnacht and Egnach, or outside St. Gallen. The following <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EnGPDY773H9CoM7qOfZ7IPQBbDPL26Ft6byjb68ZGkBGcA?e=Y3YVEi">link</a> shows the recording of the sheep.

#### Labeling the Image Material
To label the image material, it can be automatically loaded into ChatGPT, for example, via an API. Then, a prompt can be given for the position of the wolf, and the result can subsequently be assigned to the image in a large dataset. However, this process is only carried out with 80% of the image material. The other 20% of the image material will be needed later for testing the AI.
Alternatives to ChatGPT are <a href="https://labelbox.com/">Labelbox</a>, <a href="https://roboflow.com/annotate">Roboflow</a>, LabelImg, <a href="https://labelstud.io/">Labelstudio</a>, <a href="https://www.cvat.ai/">CVAT</a>, and <a href="https://www.makesense.ai/">Makesense.Ai</a>. Ultimately, the labels should be in the following <a href="https://docs.ultralytics.com/de/datasets/detect/">format</a>, split into "images" and "labels."
<br>
##### Labeling the Test Dataset
When I created a test dataset, I followed the following <a href="https://www.youtube.com/watch?v=SDV6Gz0suAk">video</a>, which shows automated labeling of image material using Roboflow. The dataset can be downloaded directly in a desired format. Various classes can be defined and adjusted independently in case of incorrect/inaccurate labels. Likewise, the size of the Train, Valid, and Test sets can be adjusted. The image size is also freely selectable, and augmentation can be added. However, the free use of Roboflow is limited.

##### Labeling the Final Dataset
To receive support in labeling the dataset, I use <a href="https://github.com/luca-medeiros/lang-segment-anything">Language Segment-Anything</a>. This allows me to pass text input to the model. It then recognizes (ideally) the objects in the image and can provide the exact coordinates. My experience shows that this works with high-contrast images where the object is clearly recognizable. For images where it does not correctly detect the object, I upload them to Roboflow. There, I labeled them by hand in this <a href="https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6InZNaVZaYXJJQ3doektaNjd6RzBUUGVjMUZGYjIiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoiam9oYW5uZXNAc3RvZWx6bGUuY2giLCJpYXQiOjE3NTcxNDI5Njd9.w-96dd0NI6Ibx1FXdsql3DxaohJ1o-sxa0B4HMuUH80">project</a>. Once I have labeled all images, I upload the preliminary dataset to Roboflow again to have it augmented. This is the <a href="https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6Ik1QcGVSd05DZ3hVdkZkbWllRXlJS2o5WGh4dDIiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoiam9oYW5uZXNAc3RvZWx6bGUuY2giLCJpYXQiOjE3NjA5NTg1MjZ9.zZHbh1AH8llGCRMbs-j2LtNB5tj9BL5wadROcMWHjiQ">project</a> for that. For the <a href="https://blog.roboflow.com/object-detection-augmentation/">augmentation</a>, I use the following settings:
* Flip: Horizontal
* Crop: 0% Minimum Zoom, 25% Maximum Zoom
* Rotation: Between -15° and +15°
* Hue: Between -15° and +15°
* Saturation: Between -28% and +28%
* Brightness: Between -20% and +20%
* Exposure: Between -15% and +15%
* Blur: Up to 2.5px
* Noise: Up to 0.06% of pixels

Afterward, I download the dataset from Roboflow and can use it for training. The final dataset is accessible under this <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EmrC34QCeMNMh5nsG0g5v4YBju3Qs9Egffm7CIumSYiHmQ?e=mAljjI">link</a>.

### Installation of a YOLO Model
The following <a href="https://www.youtube.com/watch?v=_WKS4E9SmkA">video</a> shows that the YOLO11n model is the best variant for real-time object detection on the Raspberry Pi 5 (the dataset used for this has 750 images and was exported in NCNN format). <br>
I take inspiration for the training procedure from these instructions: <a href="https://www.youtube.com/watch?v=LNwODJXcvt4">Video</a>, <a href="https://www.ultralytics.com/de/blog/training-custom-datasets-with-ultralytics-yolov8-in-google-colab">Blog</a>, <a href="https://www.youtube.com/watch?v=r0RspiLG260">Video</a>, <a href="https://colab.research.google.com/github/roboflow/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb">Google Colab</a>.

### Training the YOLO Model with Custom Dataset
#### Execution with a Test Dataset
I performed the training of a YOLO model in Google Colab with a test dataset. The procedure was documented in "Train_Google_Colab." The test dataset contained 10 wolf images from a bird's-eye view. This is the reason why the model only achieved a precision of 0.42 and a mAP50 of 0.74. The YOLOv8 model was trained with 50 epochs, an image size of 640x640, and a batch size of 16. When I tried the model with three test images, the model did not mark any bounding boxes on the images.
<br>
In the second attempt, the dataset received 500 training images (1 class). The YOLOv8s model was trained with 50 epochs, an image size of 640 pixels, and a batch size of 16. It achieved a precision of 0.94, a recall of 0.96, a mAP50 of 0.98, and a mAP50-95 of 0.8.
<br>
The third attempt, with the same dataset and 70 epochs, 640 pixels, 32 batches, and the YOLOv8n model, yielded the following results: Precision = 0.99, Recall = 0.96, mAP50 = 0.99, mAP50-95 = 0.76. On images very similar to those in the training set, the model works very well. However, it reacts relatively poorly to completely new images. For example, it partially recognizes sheep as wolves, and it recognizes no wolves from new perspectives.
<br>
The next test was again trained with the same dataset at 100 epochs, 640 pixels, 32 batches, and the YOLOv8m model. It achieved the following results: Precision = 0.99, Recall = 0.91, mAP50 = 0.98, mAP50-95 = 0.82.

#### Execution with the Final Dataset
Version 1: I followed the same procedure as with the test dataset. The model achieved the following results with YOLOv8m model training at 100 epochs, 640 pixels, and 32 batches: Precision = 0.96, Recall = 0.94, mAP50 = 0.96, mAP50-95 = 0.79. The trained model ("pt" file) can be downloaded <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/IgBqwt-EAnjDTIeZ7BtIOb-GASMAimKNZHBWZ0xQ00VmqZM?e=FzGYXP">here</a>.
<br>
Final Version: The model achieved the following results with YOLOv8s model training at 70 epochs, 640 pixels, and 64 batches: Precision = 0.96, Recall = 0.93, mAP50 = 0.96, mAP50-95 = 0.77, preprocess = 0.1ms, inference = 0.5ms, loss = 0.0ms, postprocess per image = 0.8ms. The training of 70 epochs was completed in 5.57 hours. The trained model ("pt" file) can be downloaded <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/IgBqwt-EAnjDTIeZ7BtIOb-GASMAimKNZHBWZ0xQ00VmqZM?e=FzGYXP">here</a>. It comprises a total of 2384 test images, 67398 train images, and 3275 valid images. I would have a further 9867 wolf images that I could add to the dataset for better results. However, these would have to be labeled by hand, which was no longer possible due to time constraints.

#### Alternative Execution
As an alternative, an already existing model can be further trained. This has the advantage that I can improve a model specifically for my application without having to train everything from scratch myself. Options would be, for example, <a href="https://github.com/google/cameratrapai">SpeciesNet</a>, which is specialized for wildlife, or <a href="https://huggingface.co/StephanST/unidrone">Unidrone</a>, which was trained on images from a bird's-eye view.

### Verifying the Success Rate of the AI
To determine the <a href="https://labelyourdata.com/articles/object-detection-metrics">success rate</a> of the AI, the remaining 20% of the image material is loaded into the AI. If you want to know how well an AI works at recognizing objects, you have to compare its results with reality. This real data is called Ground Truth. These are images or videos in which humans have marked the objects by hand. The AI also tries to recognize these objects, and you then check how well its predictions match the Ground Truth.<br>
In the evaluation, different cases are distinguished:

* True Positive (TP): The AI recognizes an object correctly – it is really there and in the right place.
* False Positive (FP): The AI recognizes something that is not a real object at all, i.e., a false alarm.
* False Negative (FN): An object is in the image, but the AI overlooks it.
* True Negative (TN): Hardly used in object detection because it is about finding objects – not confirming their absence.
<br>
A very important measurement is the Intersection over Union, or IoU for short.
It shows how much the box that the AI draws around an object overlaps with the real box.
If the two boxes overlap well, the IoU is high – this means the AI has localized the object very accurately.
If they hardly overlap, the IoU is low.
Usually, a threshold value is set, for example 0.5. Then a detection from an IoU of 0.5 counts as correct.
<br>
To evaluate how precisely and how completely the AI works, two further values are used: Precision and Recall.
Precision shows how many of the recognized objects were really correct.
If the AI recognizes ten things and eight of them are correct, the precision is 0.8 (i.e., 80%).
High precision means: few false alarms (few False Positives).
Recall shows how many of the actually existing objects the AI found.
If ten objects are in the image and the AI only recognizes eight, the recall is 80%.
High recall means: the AI overlooks almost nothing (few False Negatives).
It is often difficult to get both perfect at the same time – if you set the AI very cautiously, you get fewer false reports (high precision), but perhaps overlook some objects (low recall).
<br>
To find a good compromise between precision and recall, the F1 Score is used.
It is the harmonic mean of the two values and shows how balanced the model works between accuracy and completeness.
A high F1 Score means that the AI neither makes too many mistakes nor overlooks too many objects.
<br>
If the AI is supposed to recognize multiple object types (for example cars, people, and bicycles), you need a metric that considers all classes.
For this, Average Precision (AP) is used. It summarizes precision across various recall levels into a single value.
Since an AP is calculated for each object class, the average across all classes is then taken – this is called Mean Average Precision (mAP).
The mAP is the most important overall value for object detection.
A high mAP means that the AI works reliably and precisely across all classes.
<br>
Each detection by the AI also has a so-called Confidence Score. This is the value that indicates how sure the AI is that a recognized object actually exists.
A threshold value can be set, from which score a detection counts as "valid."
A higher threshold ensures fewer false alarms (higher precision), a lower threshold ensures that fewer objects are overlooked (higher recall).
<br>
In addition to accuracy, the speed of the model also plays a role.
This is measured in Frames per Second (FPS) and shows how many images per second the AI can process.
This is particularly important for applications that must function in real time, for example in autonomous driving or video surveillance.

### Installation of the AI on a Raspberry Pi
This <a href="https://roboflow.com/how-to-deploy/deploy-yolov8-to-the-raspberry-pi">tutorial</a> shows that the AI can now be copied over to the Raspberry Pi (e.g., in TensorFlow Lite format). To do this, the Raspberry Pi only needs to be connected to the computer via SSH. Then the AI can be copied over to the Raspberry Pi. To ensure that recognition also works smoothly with the Raspberry Pi camera, the resolution and image format must be adapted to the image material used for training the AI. Therefore, the camera images must be adjusted slightly after acquisition before being input into the AI. Likewise, an image may only be passed to the AI every half second, for example, to prevent the Raspberry Pi from being overstrained.

#### Final Execution on the Raspberry Pi
I follow the following <a href="https://www.youtube.com/watch?v=z70ZrSZNi-8">instructions</a> to run a YOLO model on the Raspberry Pi. In this way, the AI can either iterate over the live camera or over selected images. The bounding boxes are drawn directly onto the camera image.
Version 1 of the AI achieves an average speed of 0.45 FPS and an average inference time of 2245.98 ms on the Raspberry Pi 5.
The final version of the AI achieves an average speed of 1.12 FPS and an average inference time of 889.97 ms on the Raspberry Pi 5.

#### Prerequisites
To be able to run a neural network on a Raspberry Pi, I need a Raspberry Pi AI accelerator and a cooler. Likewise, the Raspberry Pi must be equipped with a camera.

#### Installation of Materials on a Drone
The scope of this project also includes the installation of the Raspberry Pi AI accelerator, the cooler, etc., on a drone. For this, customized screws must be manufactured using a 3D printer, among other things. The electronic wiring of the new components also belongs to this step.

## Optional Features
* Since I cannot take the wolf images with a thermal camera (as of 24.02.25), but want to recognize the wolf in darkness as well, I could apply a thermal image filter over the image material. I could then retrain the AI and test how well the system now recognizes wolves at night.
* Another optional feature would be trying out different YOLO models and training parameters to find the best possible AI for a Raspberry Pi. This involves weighing accuracy against speed. (completed)
* Another expansion is that the coordinates of the wolf on the image can be output. (completed)
* Likewise, it can be investigated whether the self-created AI performs better than, e.g., ChatGPT API requests or other open-source object detection models.
* I could also replace the external YOLO model and write my own code for the AI.

# Problems
* One problem for the project could be recording the wolf images. I would need permission from a zoo to fly a drone over the wolves or to be allowed to set up a stationary device for several weeks.
* Another difficulty of the topic could be the training of the AI, which requires a powerful computer or GPU.
* A further problem is the storage of the several thousand / tens of thousands / hundreds of thousands of images.
* Likewise, I would have to ask myself, if I were to use a stationary device for recording, how I would filter wolf images from non-wolf images. I should only store the wolf images to avoid receiving mostly erroneous images.

# Potential for Optimization
* Potential for improvement lies in the use of <a href="https://www.researchgate.net/publication/370194602_Day-to-night_image_translation_via_transfer_learning_to_keep_semantic_information_for_driving_simulator">Transfer Learning</a> to convert daytime images into nighttime images or summer images into winter images, for example, and thus improve the robustness of the model. Alternatively, a thermal camera could be used. Then, however, recording the images would be significantly more time-consuming.

# Instructions for Use
This <a href="https://colab.research.google.com/drive/1o5hgyjbkZwoVnYPL-1KSa5cvSLf4A5k9?usp=sharing">Google Colab Notebook</a> contains the code necessary for training and using the AI. If you do not wish to retrain, the path for the "pt" file should be adjusted. In the <a href="https://colab.research.google.com/drive/1DJzyPceMakVeashy7c20rP2ksB7nRpF7?usp=sharing">labeling process</a>, you can also experiment. Here too, the paths should be changed.

# Material List
<table>
  <thead>
    <tr>
      <th>Product</th>
      <th>Cost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Raspberry Pi Fan (not used):<br>
        https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_luefter_fuer_raspberry_pi_5-360116?q=%2Fapi%2Fuser%2FcountrySelect%2Fde%2Fhttps%3A%2F%2Fwww.reichelt.de%2Fde%2Fde%2Fshop%2Fprodukt%2Fraspberry_pi_-_luefter_fuer_raspberry_pi_5-360116 </td>
      <td>5.47 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi AI Accelerator (not used):<br>
        https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_shield_-_ai_ki_26_tops_raspberry_pi_5-390448 </td>
      <td>106.86 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi Camera (not used):<br>
      https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_kamera_12mp_120_v3-339260</td>
      <td>34 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi Ribbon Cable for Camera (not used):<br>
     https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_flachbandkabel_fuer_kamera_20_cm-360118</td>
      <td>1.20 Fr.</td>
    </tr>
        <tr>
      <td>microSD card for short-term storage of drone videos: <br>
        https://www.digitec.ch/de/s1/product/sandisk-extreme-microsdxc-sd-s-microsdxc-256-gb-u3-uhs-i-speicherkarte-20932251?supplier=406802&utm_source=google&utm_medium=cpc&utm_campaign=PROD_CH_PMAX_M6_C4&campaignid=21028347765&adgroupid=&adid=&dgCidg=Cj0KCQiA8q--BhDiARIsAP9tKI3RNmOl8y-l3OyqPT_JXIeHUGtxVwzwmUXusCfflVr4PLTbQIVooJAaAhv_EALw_wcB&gad_source=1&gclid=Cj0KCQiA8q--BhDiARIsAP9tKI3RNmOl8y-l3OyqPT_JXIeHUGtxVwzwmUXusCfflVr4PLTbQIVooJAaAhv_EALw_wcB&gclsrc=aw.ds </td>
      <td>28.60 Fr.</td>
    </tr>
    </tr>
        <tr>
      <td>Shipping costs for Tierpark Dählhölzli (for microSD card so the zoo can record)
      <td>10.50 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi 5, on which my AI runs:<br>
      https://www.digitec.ch/de/s1/product/raspberry-pi-5-8gb-entwicklungsboard-kit-38955607</td>
      <td>88.90 Fr.</td>
    </tr>
    <tr>
      <td>Stick for data storage:<br>
      https://www.galaxus.ch/de/s1/product/samsung-flash-drive-type-c-512-gb-usb-c-usb-31-usb-stick-44685411?supplier=406802&utm_source=google&utm_medium=cpc&utm_campaign=PMax:+PROD_CH_SSC_Cluster_0.3(C)&campaignid=20975956292&adgroupid=&adid=&dgCidg=CjwKCAjwzMi_BhACEiwAX4YZUIyccBdJ3BmYM50i18C6lFZ4XaK05ULealtZP998f3yWRfcvFZrlhRoCWsQQAvD_BwE&gad_source=1&gclid=CjwKCAjwzMi_BhACEiwAX4YZUIyccBdJ3BmYM50i18C6lFZ4XaK05ULealtZP998f3yWRfcvFZrlhRoCWsQQAvD_BwE&gclsrc=aw.ds</td>
      <td>49.70 Fr.</td>
    </tr>
  </tbody>
</table>
