# Abstract
In diesem Projekt entwickle ich eine Künstliche Intelligenz, die Wölfe aus der Vogelperspektive erkennt und die Position des Wolfes auf dem Bild zurückgeben kann. Die KI soll auf einem Raspberry Pi eigenständig laufen können. 
# Programmbeschrieb
## Arbeitsschritte
### Erstellung Datenset
Im ersten Arbeitsschritt gilt es, die Wolfs-Aufnahmen zu sammeln. Dafür muss ich mit einem Zoo zusammenarbeiten, der Wölfe in Besitz hat. Ebenso muss ich Schafs-Aufnahmen durchführen, sodass die KI sicherer wird, Wölfe und Schafe zu unterscheiden. Sobald ich über die Aufnahmen verfüge, lade ich das Videomaterial in ein Python-File in VS Code. Dieses extrahiert mithilfe von OpenCV beispielsweise alle halbe Sekunde das aktuelle Frame und speichert dieses als ein neues Bild. Somit können aus wenigen Dateien für die Videos mehrere Tausend Fotos entstehen. Danach müssen die Bilder möglicherweise noch in der Auflösung verkleinert werden, sodass die KI nicht zu gross wird und später auch auf einem Raspberry Pi funktionieren kann. Dafür kann ebenfalls OpenCV in VS Code verwendet werden. Der nächste Schritt ist, die Bilder mit der Position des Wolfes / der Schafe zu beschriften. Zuletzt wird noch das Datenset mit nochmals der gleichen Menge an Bildmaterial, dieses Mal aber mit Nicht-Wolfs-Schaf-Bildern, vervollständigt und als "etwas anderes" beschriftet. 
#### Auswahl Zoo
Bereits angefragte Zoos sind der Tierpark Dählhölzli Bern, der Tierpark Wilhelma in Stuttgart, der Wildnispark Zürich Langenberg, der Wildpark Bruderhaus in Winterthur, der Tierpark Goldau, der Tierpark Lange Erlen in Basel, der Sikypark in Crémines, der Juraparc Vallorbe, der Parc Animalier de Sainte-Croixder in Frankreich, der Zoo la Garenne in Waadt, der Alpenzoo in Innsbruck, der Wildpark Feldkirch und der Alternativer Wolf- und Bärenpark im Schwarzwald.   

Letzte Aktualisierung am 05.03.25: Der Tierpark Dählhölzli in Bern hat mir angeboten, dass ein Tierpfleger des Tierparkes mit seiner Drohne für 30 min. Aufnahmen für mich machen würde. Zuletzt habe ich ihnen dafür eine Beschreibung zugesendet, was ich genau bräuchte. Am 06.03. habe ich das Paket mit der microSD-Karte für die Aufnahmen auf die Post gebracht. Nun wird der Tierpfleger die Videos aufnehmen und mir wieder die microSD-Karte zurücksenden. <br> 
Letzte Aktualisierung am 06.04.25: Durch technische Probleme beim Abheben der Drohne kann der Tierpark Dählhölzli nun doch kein Videomaterial mit einer Drohne aufnehmen. Nun habe ich das Angebot von ihnen angenommen, dass sie die Aufnahmen mit einem stationären Gerät versuchen. Sie werden nun die Aufnahmen mit der microSD-Karte zurückschicken. Im Gegenzug dazu darf ich am 10.04.25 den Tierpark Lange Erlen in Basel besuchen, um mit meiner eigenen Drohne die Aufnahmen durchzuführen. 
#### Aufnahme des Wolf-Bildmaterials 
Prinzipiell gibt es zwei Ansätze für die Aufnahme des Bildmaterials. 
Eine Möglichkeit wäre, eine Drohne in größerer Höhe über die Wölfe fliegen zu lassen. Alternativ könnte eine stationäre Kamera für einen begrenzten Zeitraum an einem erhöhten Punkt installiert werden, um die Wölfe von oben zu filmen. Für beide Optionen brauche ich ungefähr 1,5 Stunden Videomaterial, in dem der Wolf aus der Vogelperspektive sichtbar ist. Es ist egal, auf wie viele Teilvideos die Aufnahmen verteilt sind – wichtig ist nur, dass die Drohne / der Wolf bei einem stationären Gerät nicht an Ort und Stelle bleibt, sondern in Bewegung ist, um verschiedene Situationen und Blickwinkel einzufangen. Die Höhe der Aufnahmen überlasse ich den Gegebenheiten vor Ort, denn oftmals ist das Wolfs-Gehege stark bewaldet, was z.B. einen Drohnenflug stark eingrenzt. Der Wolf sollte auf den Aufnahmen einfach gut erkennbar sein. 
<br>
<br>
Erkenntnisse Aufnahmen Tierpark Lange Erlen:<br>
Alles verlief ausgesprochen gut, und ich konnte einige wenige, dafür jedoch sehr gute Aufnahmen machen. Wir haben das Wolfsgehege durchgehend von 10:30 Uhr bis kurz vor 18:00 Uhr beobachtet. Allerdings haben sich die Wölfe ab Mittag kaum mehr gezeigt, da sie sich meist unter den Bäumen zum Schlafen zurückgezogen haben. Am Vormittag hingegen waren sie deutlich aktiver.
Es war ein wenig schade, dass ich nicht genügend Videomaterial für mein Projekt erhalten habe. Dafür ist die Qualität des vorhandenen Videomaterials optimal für meine Arbeit. Der folgende <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EtW27rpb1ZlBpWLmhlBq-AABzyn67NjPXbQeZUokLfIz_g?e=WHIiu2">Link</a> zeigt die Aufnahmen im Tierpark Lange Erlen.
<br>
<br>
Erkenntnisse Aufnahmen Tierpark Feldkirch:<br>
Um mein Videomaterial zu ergänzen, habe ich den Tierpark Feldkirch besucht. Das Wolfsgehege war stark bewaldet, was die Flüge etwas eingeschränkt haben. Das Verhalten der Wölfe war jedoch sehr unterschiedlich zu demjenigen im Tierpark Lange Erlen. Die zwei Wölfe haben sich durchgängig bewegt und gezeigt. Die Sichtverhältnisse waren ebenfalls unterschiedlich zu den bereits gesammelten, weshalb sie mir gut weiterhelfen. Sowohl im Tierpark Lange Erlen als auch im Tierpark Feldkirch düfte ich bei Bedarf nochmals vorbeikommen. Der folgende <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EoVr0IEm8wtJmrYriqSY3oIBNzjmjKQcn4gmxEIL_Skm_Q?e=1lfLn1">Link</a> zeigt die Aufnahmen im Tierpark Feldkirch.

#### Aufnahme des Schaf-Bildmaterials 
Die Aufnahme des Schaf-Bildmaterials lässt sich etwas einfacher gestalten. Hier ist es möglich, einen Bauer anzufragen, ob ich über seine Schafsherde mit einer Drohne fliegen darf. Schafe hat es beispielsweise bei Roggwil, bei Stachen, bei Güttingen und zwischen Frasnacht und Egnach oder vor St.Gallen. Der folgende <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EnGPDY773H9CoM7qOfZ7IPQBbDPL26Ft6byjb68ZGkBGcA?e=Y3YVEi">Link</a> zeigt die Aufnahme der Schafe.
#### Beschriftung des Bildmaterials
Um das Bildmaterial zu beschriften, kann das Bildmaterial z.B. per API automatisiert in Chat GPT hereingeladen werden. Danach kann ein Prompt für die Position des Wolfes gestellt werden und anschliessend die Rückgabe in einem grossen Datenset dem Bild zugeordnet werden. Jedoch wird dieses Verfahren nur mit 80 % des Bildmaterials durchgeführt. Die anderen 20 % des Bildmaterials werden später für das Testen der KI benötigt. 
Alternativen zu Chat GPT sind <a href="https://labelbox.com/ ">Labelbox</a>, <a href="https://roboflow.com/annotate">Roboflow</a>, Labellmg, <a href="https://labelstud.io/">Labelstudio</a>, <a href="https://www.cvat.ai/">CVAT</a> und <a href="https://www.makesense.ai/ ">Makesense.Ai</a> Schlussendlich sollten die Beschriftungen in dem folgenden <a href="https://docs.ultralytics.com/de/datasets/detect/">Format</a> sein, aufgeteilt in "images" und "labels". 
<br>
##### Beschriftung Test-Datensatz
Als ich ein Test-Datensatz erstellt habe, bin ich dem folgenden <a href="https://www.youtube.com/watch?v=SDV6Gz0suAk">Video</a> gefolgt, das eine automatisierte Beschriftung des Bildmaterials mithilfe von Roboflow zeigt. Das Datenset kann direkt in einer gewünschten Form heruntergeladen werden. Es können verschiedene Klassen festgelegt werden und bei falschen / ungenauen Beschriftungen selbständig angepasst werden. Ebenso kann die Grösse des Train, Valid und Test Set angepasst werden. Aber auch die Bildgrösse ist frei wählbar und Augmentation kann hinzugefügt werden. Die kostenlose Verwendung von Roboflow ist jedoch begrenzt.

##### Beschriftung des finalen Datensatzes
Um Unterstützung bei der Beschriftung des Datensatzes zu erhalten, verwende ich  <a href="https://github.com/luca-medeiros/lang-segment-anything">Language Segment-Anything</a>. Dies erlaubt es mir, einen Text-Input dem Modell zu übergeben. Daraufhin erkennt es (sollte) die Objekte auf dem Bild und kann die genauen Koordinaten wiedergeben. Meine Erfahrung zeigt, dass dies bei kontrastreichen Bildern funktioniert, bei welchen das Objekt gut erkennbar ist. Bei den Bildern, bei denen es das Objekt nicht korrekt entdeckt, lade ich nach Roboflow. Dort habe ich in diesem <a href="https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6InZNaVZaYXJJQ3doektaNjd6RzBUUGVjMUZGYjIiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoiam9oYW5uZXNAc3RvZWx6bGUuY2giLCJpYXQiOjE3NTcxNDI5Njd9.w-96dd0NI6Ibx1FXdsql3DxaohJ1o-sxa0B4HMuUH80
">Projekt</a> per Hand beschriftet. Sobald ich alle Bilder beschriftet habe, lade ich das vorläufige Datenset erneut auf Roboflow, um es augmentieren zu lassen. Dies ist das <a href="https://app.roboflow.com/join/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3b3Jrc3BhY2VJZCI6Ik1QcGVSd05DZ3hVdkZkbWllRXlJS2o5WGh4dDIiLCJyb2xlIjoib3duZXIiLCJpbnZpdGVyIjoiam9oYW5uZXNAc3RvZWx6bGUuY2giLCJpYXQiOjE3NjA5NTg1MjZ9.zZHbh1AH8llGCRMbs-j2LtNB5tj9BL5wadROcMWHjiQ">Projekt</a> dazu. Für die  <a href="https://blog.roboflow.com/object-detection-augmentation/">Augmentation</a> verwende ich die folgenden Einstellungen: 
* Flip: Horizontal
* Crop: 0% Minimum Zoom, 25% Maximum Zoom
* Rotation: Between -15° and +15°
* Hue: Between -15° and +15°
* Saturation: Between -28% and +28%
* Brightness: Between -20% and +20%
* Exposure: Between -15% and +15%
* Blur: Up to 2.5px
* Noise: Up to 0.06% of pixels

Danach lade ich den Datensatz von Roboflow herunter und kann diesen für das Training benutzen. Unter diesem <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/g/personal/jostoelz_ksr_ch/EmrC34QCeMNMh5nsG0g5v4YBju3Qs9Egffm7CIumSYiHmQ?e=mAljjI">Link</a> ist das finale Datenset aufrufbar. 
### Installierung eines YOLO-Models
Das folgende <a href="https://www.youtube.com/watch?v=_WKS4E9SmkA">Video</a> zeigt, dass das YOLO11n Modell die beste Variante für Echtzeit Objekterkennung auf dem Raspberry Pi 5 ist (das dazu verwendete Datenset hat 750 Bildern und wurde im Format NCNN exportiert). <br>
Inspiration für das Trainingsvorgehen entnehme ich von diesen Anleitungen: <a href="https://www.youtube.com/watch?v=LNwODJXcvt4">Video</a>, <a href="https://www.ultralytics.com/de/blog/training-custom-datasets-with-ultralytics-yolov8-in-google-colab">Blog</a>, <a href="https://www.youtube.com/watch?v=r0RspiLG260">Video</a>, <a href="https://colab.research.google.com/github/roboflow/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb">Google Colab</a>.

### Training des YOLO-Models mit eigenem Datenset
#### Durchführung mit einem Test-Datensatz
Ich habe das Training eines YOLO-Modells in Google Colab mit einem Test-Datensatz durchgeführt. Das Vorgehen wurde in "Train_Google_Colab" dokumentiert. Der Test-Datensatz enthielt 10 Wolfs-Bilder aus der Vogelperspektive. Dies ist der Grund, warum das Modell auch nur eine Precision von 0.42 und eine mAP50 von 0.74 erreichte. Das YOLO v8-Modell wurden mit 50 Epochen, mit einer Bildergrösse von 640x640 und einer Batch-Grösse von 16 trainiert. Als ich das Modell mit drei Test-Bilder ausprobiert habe, hat das Modell keine Bounding Boxen auf den Bildern markiert. 
<br>
Beim zweiten Versuch erhielt der Datensatz 500 Trainingsbilder (1 Klasse). Das YOLO v8s-Modell wurde mit 50 Epochen, einer Bildgrösse von 640 Pixeln und einer Batch-Grösse von 16 trainiert. Es erreichte eine Precision von 0.94, ein Recall von 0.96, ein mAP50 von 0.98 und ein mAP50-95 von 0.8. 
<br>
Der dritte Versuch erbrachte mit dem gleichen Datensatz mit 70 Epochen, 640 Pixeln, 32 Batches und dem YOLO v8n-Modell die folgende Resultate: Precision = 0.99, Recall = 0.96, mAP50 = 0.99, mAP50-95 = 0.76. Auf sehr ähnlichen Bildern, wie im Trainingsset, funktioniert das Modell sehr gut. Hingegen auf komplett neuen Bildern reagiert es relativ schlecht. Beispielsweise erkennt es Schafe teilweise als Wölfe, und aus neuen Perspektiven erkennt es keine Wölfe. 
<br>
Der nächste Test wurde wieder mit dem gleichen Datensatz bei 100 Epochen, 640 Pixeln, 32 Batches und dem YOLO v8m-Modell trainiert. Es erreichte die folgende Resultate: Precision = 0.99, Recall = 0.91, mAP50 = 0.98, mAP50-95 = 0.82.
#### Durchführung mit dem finalen Datensatz
Version 1: Ich folge dem gleichen Vorgehen wie mit dem Test-Datensatz durchgeführt. Das Modell erreicht mit einem YOLO v8m-Modell-Training bei 100 Epochen, 640 Pixeln, 32 Batches die folgenden Resultate: Precision = , Recall = , mAP50, mAP50-95 = . Das trainierte Modell ("pt"-Datei) kann <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/r/personal/jostoelz_ksr_ch/Documents/Privat/Maturaarbeit/Wolfs-Erkennung-AI/Data_sharing?csf=1&web=1&e=G6Jn56">hier</a> heruntergeladen werden.
Finale Version: Das Modell erreicht mit einem YOLO v8m-Modell-Training bei 100 Epochen, 640 Pixeln, 32 Batches die folgenden Resultate: Precision = , Recall = , mAP50, mAP50-95 = . Das trainierte Modell ("pt"-Datei) kann <a href="https://kantonsschuleromanshorn-my.sharepoint.com/:f:/r/personal/jostoelz_ksr_ch/Documents/Privat/Maturaarbeit/Wolfs-Erkennung-AI/Data_sharing?csf=1&web=1&e=G6Jn56">hier</a> heruntergeladen werden. Es umfasst insgesamt ... Bilder. 
#### Alternative Durchführung
Als Alternative kann auch ein schon bestehendes Modell weitertrainiert werden. Das hat den Vorteil, dass ich ein Modell spezifisch auf meine Anwendung verbessern kann, aber nicht von Grund auf alles selbst trainieren muss. Optionen wären beispielsweise <a href="https://github.com/google/cameratrapai">SpeciesNet</a>, welches auf Wildtier spezialisiert ist, oder <a href="https://huggingface.co/StephanST/unidrone">Unidrone</a>, welches auf Bilder aus der Vogelperspektive trainiert wurde.
### Überprüfung der Erfolgsquote der KI
Um die <a href="https://labelyourdata.com/articles/object-detection-metrics">Erfolgsquote</a> der KI zu ermitteln, werden die restlichen 20 % des Bildmaterials in die KI geladen. Wenn man wissen will, wie gut eine KI beim Erkennen von Objekten funktioniert, muss man ihre Ergebnisse mit der Realität vergleichen. Diese echten Daten nennt man Ground Truth. Das sind Bilder oder Videos, in denen Menschen die Objekte per Hand markiert haben. Die KI versucht, diese Objekte ebenfalls zu erkennen, und man überprüft dann, wie gut ihre Vorhersagen mit der Ground Truth übereinstimmen.<br>
Bei der Auswertung unterscheidet man verschiedene Fälle:

* True Positive (TP): Die KI erkennt ein Objekt richtig – es ist wirklich da und an der richtigen Stelle.
* False Positive (FP): Die KI erkennt etwas, was gar kein echtes Objekt ist, also ein Fehlalarm.
* False Negative (FN): Ein Objekt ist im Bild, aber die KI übersieht es.
* True Negative (TN): Wird in der Objekterkennung kaum benutzt, weil es hier darum geht, Objekte zu finden – nicht ihre Abwesenheit zu bestätigen.
<br>
Ein sehr wichtiger Messwert ist der Intersection over Union, kurz IoU.
Er zeigt, wie stark sich die Box, die die KI um ein Objekt zeichnet, mit der echten Box überlappt.
Wenn sich die beiden Boxen gut decken, ist der IoU hoch – das heißt, die KI hat das Objekt sehr genau lokalisiert.
Wenn sie sich kaum überschneiden, ist der IoU niedrig.
Meist legt man einen Schwellenwert fest, zum Beispiel 0,5. Dann gilt eine Erkennung ab einem IoU von 0,5 als richtig.
<br>
Um zu bewerten, wie genau und wie vollständig die KI arbeitet, verwendet man zwei weitere Werte: Precision und Recall.
Die Precision zeigt, wie viele der erkannten Objekte wirklich korrekt waren.
Wenn die KI also zehn Dinge erkennt und acht davon richtig sind, beträgt die Precision 0,8 (also 80 %).
Eine hohe Precision bedeutet: wenig Fehlalarme (wenig False Positives).
Der Recall zeigt, wie viele der tatsächlich vorhandenen Objekte die KI gefunden hat.
Wenn zehn Objekte im Bild sind und die KI nur acht erkennt, liegt der Recall bei 80 %.
Ein hoher Recall bedeutet: die KI übersieht kaum etwas (wenig False Negatives).
Oft ist es schwer, beides gleichzeitig perfekt hinzubekommen – wenn man die KI sehr vorsichtig einstellt, bekommt man weniger Falschmeldungen (hohe Precision), aber übersieht vielleicht manche Objekte (niedriger Recall).
<br>
Um einen guten Kompromiss zwischen Precision und Recall zu finden, verwendet man den F1-Score.
Er ist das harmonische Mittel der beiden Werte und zeigt, wie ausgewogen das Modell zwischen Genauigkeit und Vollständigkeit arbeitet.
Ein hoher F1-Score bedeutet, dass die KI weder zu viele Fehler macht noch zu viele Objekte übersieht.
<br>
Wenn die KI mehrere Objektarten erkennen soll (zum Beispiel Autos, Menschen und Fahrräder), braucht man eine Metrik, die alle Klassen berücksichtigt.
Dafür nutzt man den Average Precision (AP). Er fasst die Precision über verschiedene Recall-Stufen hinweg zu einem einzigen Wert zusammen.
Da man für jede Objektklasse einen AP berechnet, nimmt man anschließend den Durchschnitt über alle Klassen – das nennt man Mean Average Precision (mAP).
Der mAP ist der wichtigste Gesamtwert für Object Detection.
Ein hoher mAP bedeutet, dass die KI über alle Klassen hinweg zuverlässig und präzise arbeitet.
<br>
Jede Erkennung der KI hat auch einen sogenannten Confidence Score. Das ist der Wert, der angibt, wie sicher sich die KI ist, dass ein erkanntes Objekt tatsächlich existiert.
Man kann einen Threshold (Grenzwert) festlegen, ab welchem Score eine Erkennung als „gültig“ gilt.
Ein höherer Threshold sorgt für weniger Falschalarme (höhere Precision), ein niedriger Threshold dafür, dass weniger Objekte übersehen werden (höherer Recall).
<br>
Neben der Genauigkeit spielt auch die Geschwindigkeit des Modells eine Rolle.
Diese wird in Frames per Second (FPS) gemessen und zeigt, wie viele Bilder pro Sekunde die KI verarbeiten kann.
Das ist besonders wichtig bei Anwendungen, die in Echtzeit funktionieren müssen, zum Beispiel beim autonomen Fahren oder bei Videoüberwachung.

### Installierung der KI auf einem Raspberry Pi
Dieses <a href="https://roboflow.com/how-to-deploy/deploy-yolov8-to-the-raspberry-pi">Tutorial</a> zeigt, dass die KI nun auf den Raspberry Pi herüberkopiert werden kann (z.B. im Dateiformat TensorFlow Lite). Dazu muss nur der Raspberry Pi über SSH an den Computer verbunden sein. Dann kann die KI auf den Raspberry Pi herüberkopiert werden. Damit die Erkennung auch problemlos mit der Raspberry Pi Kamera funktioniert, müssen die Auflösung und das Bildformat an das Bildmaterial angepasst werden, das für das Training der KI verwendet wurde. Deshalb muss man die Bilder der Kamera nach Erhalt etwas anpassen, bevor man sie in die KI gibt. Ebenso darf z.B. nur alle halbe Sekunde ein Bild an die KI weitergegeben werden, sodass verhindert wird, dass der Raspberry Pi nicht überbeansprucht wird. 
#### Finale Durchführung auf dem Raspberry Pi
Ich folge der folgenden <a href="https://www.youtube.com/watch?v=z70ZrSZNi-8 ">Anleitung</a>, um ein YOLO-Modell auf dem Raspberry Pi laufen zu lassen. So kann die KI entweder über die Live-Kamera iterieren oder über ausgewählte Bilder. Die Bounding Boxes werden direkt auf das Kamerabild gezeichnet. 
Version 1 der KI erreicht auf dem Raspberry Pi 5 eine durchschnittliche Geschwindigkeit von 0.45 FPS und eine durchschnittliche Interferenzzeit von 2245.98 ms. 
Die finale Version der KI erreicht auf dem Raspberry Pi 5 eine durchschnittliche Geschwindigkeit von ... FPS und eine durchschnittliche Interferenzzeit von ... ms. 
#### Voraussetzungen
Um ein neuronales Netzwerk auf einem Raspberry Pi laufen lassen zu können, benötige ich einen Raspberry Pi AI Beschleuniger und einen Kühler. Ebenso muss der Raspberry Pi mit einer Kamera ausgestattet werden. 
#### Installierung der Materialien auf einer Drohne
Im Umfang dieses Projekts ist ebenfalls die Installation des Raspberry Pi AI-Beschleunigers, des Kühlers etc. auf einer Drohne enthalten. Dafür müssen unter anderem mit dem 3D-Drucker personalisierte Schrauben hergestellt werden. Auch die elektronische Verkabelung der neuen Komponenten gehört zu diesem Schritt.
## Optionale Features
* Da ich die Wolfs-Bilder nicht mit einer Wärmebildkamera (Stand: 24.02.25) aufnehmen kann, aber den Wolf auch in Dunkelheit erkennen möchte, könnte ich ein Wärmebild-Filter über das Bildmaterial legen. Anschliessend könnte ich die KI neu trainieren und testen, wie gut das System nun auch Wölfe in der Nacht erkennen kann.
* Ein anderes optionale Feature wäre das Ausprobieren verschiedener YOLO-Modelle und Trainings-Parameter, um die bestmöglichste KI auf einem Raspberry Pi herauszufinden. Dabei muss zwischen Genauigkeit und Geschwindigkeit abgewogen werden. (erledigt)
* Eine andere Erweiterung ist, dass die Koordinaten des Wolfes auf dem Bild ausgegeben werden können. (erledigt)
* Ebenso kann untersucht werden, ob die selbst erstellte KI besser performt als z.B. Chat-GPT API Anfragen oder andere open source object detection Modelle.
* Ich könnte auch das externe YOLO-Modell ersetzen und meinen eigenen Code für die KI schreiben.

# Probleme
* Ein Problem des Projektes könnte die Aufnahme der Wolfs-Bilder sein. Ich bräuchte die Erlaubnis eines Zoos, eine Drohne über den Wolfen fliegen zu lassen oder ein stationäres Gerät während mehrerer Wochen aufbauen zu dürfen.
* Eine andere Schwierigkeit des Themas könnte das Training der KI sein, das einen leistungsstarken Computer bzw. GPU benötigt.
* Eine weitere Problematik ist die Speicherung der mehreren Tausend / Zehntausend / Hundertausend Bildern.
* Ebenso müsste ich mir die Frage stellen, wenn ich ein stationäres Gerät zur Aufnahme verwenden würde, wie ich die Wolfs-Bilder mit nicht Wolfs-Bilder filtere. Ich sollte nur die Wolfs-Bilder speichern, um nicht mehrheitlich Fehl-Bilder zu erhalten.

# Optimierungspotenzial
* Potenzial zur Verbesserung liegt in der Verwendung von <a href="https://www.researchgate.net/publication/370194602_Day-to-night_image_translation_via_transfer_learning_to_keep_semantic_information_for_driving_simulator">Transfer Learning</a>, um beispielsweise Tagesbilder in Nachtbilder oder Sommerbilder in Winterbilder umzuwandeln und so die Robusheit des Modells zu verbessern. Alternativ könnte auch eine Wärmebildkamera verwendet werden. Dann wäre aber die Aufnahme der Bilder deutlich zeitintensiver.

# Hinweise zur Benutzung
Dieses <a href="https://colab.research.google.com/drive/1o5hgyjbkZwoVnYPL-1KSa5cvSLf4A5k9?usp=sharing">Google Colab Notebook</a> verfügt über den Code, der für das Training und die Benutzung der KI notwendig ist. Falls nicht nochmals neu trainiert werden möchte, sollte der Pfad für die "pt"-Datei angepasst werden. Beim <a href="https://colab.research.google.com/drive/1DJzyPceMakVeashy7c20rP2ksB7nRpF7?usp=sharing">Label-Prozess</a> kann ebenfalls herumgespielt werden. Auch hier sollten die Pfade geändert werden.
# Materialliste
<table>
  <thead>
    <tr>
      <th>Produkt</th>
      <th>Kosten</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Raspberry Pi Lüfter (nicht benutzt):<br>
        https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_luefter_fuer_raspberry_pi_5-360116?q=%2Fapi%2Fuser%2FcountrySelect%2Fde%2Fhttps%3A%2F%2Fwww.reichelt.de%2Fde%2Fde%2Fshop%2Fprodukt%2Fraspberry_pi_-_luefter_fuer_raspberry_pi_5-360116 </td>
      <td>5.47 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi AI Beschleuniger (nicht benutzt):<br>
        https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_shield_-_ai_ki_26_tops_raspberry_pi_5-390448 </td>
      <td>106.86 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi Kamera (nicht benutzt):<br>
      https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_kamera_12mp_120_v3-339260</td>
      <td>34 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi Flachbandkabel für Kamera (nicht benutzt):<br>
     https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_flachbandkabel_fuer_kamera_20_cm-360118</td>
      <td>1.20 Fr.</td>
    </tr>
        <tr>
      <td>microSD-Karte für die kurzfristige Speicherung der Videos der Drohne: <br>
        https://www.digitec.ch/de/s1/product/sandisk-extreme-microsdxc-sd-s-microsdxc-256-gb-u3-uhs-i-speicherkarte-20932251?supplier=406802&utm_source=google&utm_medium=cpc&utm_campaign=PROD_CH_PMAX_M6_C4&campaignid=21028347765&adgroupid=&adid=&dgCidg=Cj0KCQiA8q--BhDiARIsAP9tKI3RNmOl8y-l3OyqPT_JXIeHUGtxVwzwmUXusCfflVr4PLTbQIVooJAaAhv_EALw_wcB&gad_source=1&gclid=Cj0KCQiA8q--BhDiARIsAP9tKI3RNmOl8y-l3OyqPT_JXIeHUGtxVwzwmUXusCfflVr4PLTbQIVooJAaAhv_EALw_wcB&gclsrc=aw.ds </td>
      <td>28.60 Fr.</td>
    </tr>
    </tr>
        <tr>
      <td>Paketkosten Tierpark Dählhölzli (für microSD-Karte, damit der Zoo Aufnahmen durchführen kann)
      <td>10.50 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi 5, auf welchem meine KI läuft:<br>
      https://www.digitec.ch/de/s1/product/raspberry-pi-5-8gb-entwicklungsboard-kit-38955607</td>
      <td>88.90 Fr.</td>
    </tr>
    <tr>
      <td>Stick für die Speicherung der Daten:<br>
      https://www.galaxus.ch/de/s1/product/samsung-flash-drive-type-c-512-gb-usb-c-usb-31-usb-stick-44685411?supplier=406802&utm_source=google&utm_medium=cpc&utm_campaign=PMax:+PROD_CH_SSC_Cluster_0.3(C)&campaignid=20975956292&adgroupid=&adid=&dgCidg=CjwKCAjwzMi_BhACEiwAX4YZUIyccBdJ3BmYM50i18C6lFZ4XaK05ULealtZP998f3yWRfcvFZrlhRoCWsQQAvD_BwE&gad_source=1&gclid=CjwKCAjwzMi_BhACEiwAX4YZUIyccBdJ3BmYM50i18C6lFZ4XaK05ULealtZP998f3yWRfcvFZrlhRoCWsQQAvD_BwE&gclsrc=aw.ds</td>
      <td>49.70 Fr.</td>
    </tr>
  </tbody>
</table>
