# Abstract
In diesem Projekt entwickle ich eine Künstliche Intelligenz, die Wölfe aus der Vogelperspektive erkennt und die Position des Wolfes auf dem Bild zurückgeben kann. Die KI soll auf einem Raspberry Pi eigenständig laufen können. 
# Programmbeschrieb
## Arbeitsschritte
### Erstellung Datenset
Im ersten Arbeitsschritt gilt es, die Wolfs-Aufnahmen zu sammeln. Dafür muss ich mit einem Zoo zusammenarbeiten, der Wölfe in Besitz hat. Ebenso muss ich Schafs-Aufnahmen durchführen, sodass die KI sicherer wird, Wölfe und Schafe zu unterscheiden. Sobald ich über die Aufnahmen verfüge, lade ich das Videomaterial in ein Python-File in VS Code. Dieses extrahiert mithilfe von OpenCV beispielsweise alle halbe Sekunde das aktuelle Frame und speichert dieses als ein neues Bild. Somit können aus wenigen Dateien für die Videos mehrere Tausend Fotos entstehen. Danach müssen die Bilder möglicherweise noch in der Auflösung verkleinert werden, sodass die KI nicht zu gross wird und später auch auf einem Raspberry Pi funktionieren kann. Dafür kann ebenfalls OpenCV in VS Code verwendet werden. Der nächste Schritt ist, die Bilder mit der Position des Wolfes / der Schafe zu beschriften. Zuletzt wird noch das Datenset mit nochmals der gleichen Menge an Bildmaterial, dieses Mal aber mit Nicht-Wolfs-Schaf-Bildern, vervollständigt und als "kein Wolf" beschriftet. 
#### Auswahl Zoo
Bereits angefragte Zoos sind der Tierpark Dählhölzli Bern, der Tierpark Wilhelma in Stuttgart, der Wildnispark Zürich Langenberg, der Wildpark Bruderhaus in Zürich, der Tierpark Goldau, der Alpenzoo in Innsbruck, der Wildpark Feldkirch und der Alternativer Wolf- und Bärenpark im Schwarzwald. Als Backup wären der Parc Animalier de Sainte-Croix in Frankreich, der Juraparc Vallorbe und der Zoo la Garenne in Waadt Möglichkeiten. 

Letzte Aktualisierung am 05.03.25: Der Tierpark Dählhölzli in Bern hat mir angeboten, dass ein Tierpfleger des Tierparkes mit seiner Drohne für 30 min. Aufnahmen für mich machen würde. Zuletzt habe ich ihnen dafür eine Beschreibung zugesendet, was ich genau bräuchte. Am 06.03. habe ich das Paket mit der microSD-Karte für die Aufnahmen auf die Post gebracht. Nun wird der Tierpfleger die Videos aufnehmen und mir wieder die microSD-Karte zurücksenden.
#### Aufnahme des Wolfs-Bildmaterials 
Prinzipiell gibt es zwei Ansätze für die Aufnahme des Bildmaterials. 
Eine Möglichkeit wäre, eine Drohne in größerer Höhe über die Wölfe fliegen zu lassen. Alternativ könnte eine stationäre Kamera für einen begrenzten Zeitraum an einem erhöhten Punkt installiert werden, um die Wölfe von oben zu filmen. Für beide Optionen brauche ich ungefähr 1,5 Stunden Videomaterial, in dem der Wolf aus der Vogelperspektive sichtbar ist. Es ist egal, auf wie viele Teilvideos die Aufnahmen verteilt sind – wichtig ist nur, dass die Drohne / der Wolf bei einem stationären Gerät nicht an Ort und Stelle bleibt, sondern in Bewegung ist, um verschiedene Situationen und Blickwinkel einzufangen. Die Höhe der Aufnahmen überlasse ich den Gegebenheiten vor Ort, denn oftmals ist das Wolfs-Gehege stark bewaldet, was z.B. einen Drohnenflug stark eingrenzt. Der Wolf sollte auf den Aufnahmen einfach gut erkennbar sein. 
#### Aufnahme des Schafs-Bildmaterials 
Die Aufnahme des Schaf-Bildmaterials lässt sich etwas einfacher gestalten. Hier ist es möglich, einen Bauer anzufragen, ob ich über seine Schafsherde mit einer Drohne fliegen darf. Schafe hat es beispielsweise bei Roggwil, zwischen Frasnacht und Egnach oder vor St.Gallen.
#### Beschriftung des Bildmaterials
Um das Bildmaterial zu beschriften, kann das Bildmaterial z.B. per API automatisiert in Chat GPT hereingeladen werden. Danach kann ein Prompt für die Position des Wolfes gestellt werden und anschliessend die Rückgabe in einem grossen Datenset dem Bild zugeordnet werden. Jedoch wird dieses Verfahren nur mit 80 % des Bildmaterials durchgeführt. Die anderen 20 % des Bildmaterials werden später für das Testen der KI benötigt. 
Alternativen zu Chat GPT sind <a href="https://labelbox.com/ ">Labelbox</a>, <a href="https://roboflow.com/annotate">Roboflow</a>, Labellmg, <a href="https://labelstud.io/">Labelstudio</a> und <a href="https://www.makesense.ai/ ">Makesense.Ai</a>
<br>
##### Beschriftung Test-Datensatz
Als ich ein Test-Datensatz erstellt habe, bin ich dem folgenden <a href="https://www.youtube.com/watch?v=SDV6Gz0suAk">Video</a> gefolgt, das eine automatisierte Beschriftung des Bildmaterials mithilfe von Roboflow zeigt. Das Datenset kann direkt in einer gewünschten Form heruntergeladen werden. Es können verschiedene Klassen festgelegt werden und bei falschen / ungenauen Beschriftungen selbständig angepasst werden. Ebenso kann die Grösse des Train, Valid und Test Set angepasst werden. Aber auch die Bildgrösse ist frei wählbar und Augmentation kann hinzugefügt werden. Die kostenlose Verwendung von Roboflow ist jedoch begrenzt.
### Installierung eines YOLO-Models
Das folgende <a href="https://www.youtube.com/watch?v=_WKS4E9SmkA">Video</a> zeigt, dass das YOLO11n Modell die beste Variante für Echtzeit Objekterkennung auf dem Raspberry Pi 5 ist (das dazu verwendete Datenset hat 750 Bildern und wurde im Format NCNN exportiert). <br>
Siehe Links: https://www.youtube.com/watch?v=LNwODJXcvt4 <br>
https://www.ultralytics.com/de/blog/training-custom-datasets-with-ultralytics-yolov8-in-google-colab <br>
https://www.youtube.com/watch?v=r0RspiLG260 <br>
https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb#scrollTo=4JnkELT0cIJg
https://colab.research.google.com/github/roboflow/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb
### Training des YOLO-Models mit eigenem Datenset
#### Durchführung mit einem Test-Datensatz
Ich habe das Training eines YOLO-Modells in Google Colab mit einem Test-Datensatz durchgeführt. Das Vorgehen wurde in "Train_Google_Colab" dokumentiert. Der Test-Datensatz enthielt 10 Wolfs-Bilder aus der Vogelperspektive. Dies ist der Grund, warum das Modell auch nur eine Precision von 0.42 und eine mAP50 von 0.74 erreichte. Das YOLO v8-Modell wurden mit 50 Epochen, mit einer Bildergrösse von 640x640 und einer Batch-Grösse von 16 trainiert. Als ich das Modell mit drei Test-Bilder ausprobiert habe, hat das Modell keine Bounding Boxen auf den Bildern markiert. 
### Überprüfung der Erfolgsquote der KI
Um die Erfolgsquote der KI zu ermitteln, werden die restlichen 20 % des Bildmaterials in die KI geladen. <br>
Siehe Link: https://labelyourdata.com/articles/object-detection-metrics
### Installierung der KI auf einem Raspberry Pi
Siehe Link: https://roboflow.com/how-to-deploy/deploy-yolov8-to-the-raspberry-pi  <br>
Die KI kann nun auf den Raspberry Pi herüberkopiert (z.B. im Dateiformat TensorFlow Lite) werden. Dazu muss nur der Raspberry Pi über SSH an den Computer verbunden sein. Dann kann die KI auf den Raspberry Pi herüberkopiert werden. Damit die Erkennung auch problemlos mit der Raspberry Pi Kamera funktioniert, müssen die Auflösung und das Bildformat an das Bildmaterial angepasst werden, das für das Training der KI verwendet wurde. Deshalb muss man die Bilder der Kamera nach Erhalt etwas anpassen, bevor man sie in die KI gibt. Ebenso darf z.B. nur alle halbe Sekunde ein Bild an die KI weitergegeben werden, sodass verhindert wird, dass der Raspberry Pi nicht überbeansprucht wird. 
#### Voraussetzungen
Um ein neuronales Netzwerk auf einem Raspberry Pi laufen lassen zu können, benötige ich einen Raspberry Pi AI Beschleuniger und einen Kühler. Ebenso muss der Raspberry Pi mit einer Kamera ausgestattet werden. 
#### Installierung der Materialien auf einer Drohne
Im Umfang dieses Projekts ist ebenfalls die Installation des Raspberry Pi AI-Beschleunigers, des Kühlers etc. auf einer Drohne enthalten. Dafür müssen unter anderem mit dem 3D-Drucker personalisierte Schrauben hergestellt werden. Auch die elektronische Verkabelung der neuen Komponenten gehört zu diesem Schritt.
## Optionale Features
* Da ich die Wolfs-Bilder nicht mit einer Wärmebildkamera (Stand: 24.02.25) aufnehmen kann, aber den Wolf auch in Dunkelheit erkennen möchte, könnte ich ein Wärmebild-Filter über das Bildmaterial legen. Anschliessend könnte ich die KI neu trainieren und testen, wie gut das System nun auch Wölfe in der Nacht erkennen kann.
* Ein anderes optionale Feature wäre das Ausprobieren verschiedener YOLO-Modelle und Trainings-Parameter, um die bestmöglichste KI auf einem Raspberry Pi herauszufinden. Dabei muss zwischen Genauigkeit und Geschwindigkeit abgewogen werden.
* Eine andere Erweiterung ist, dass die Koordinaten des Wolfes auf dem Bild ausgegeben werden können.
* Ebenso kann untersucht werden, ob die selbst erstellte KI besser performt als z.B. Chat-GPT API Anfragen

# Probleme
* Ein Problem des Projektes könnte die Aufnahme der Wolfs-Bilder sein. Ich bräuchte die Erlaubnis eines Zoos, eine Drohne über den Wolfen fliegen zu lassen oder ein stationäres Gerät während mehrerer Wochen aufbauen zu dürfen.
* Eine andere Schwierigkeit des Themas könnte das Training der KI sein, das einen leistungsstarken Computer bzw. GPU benötigt.
* Eine weitere Problematik ist die Speicherung der mehreren Tausend / Zehntausend / Hundertausend Bildern.
* Ebenso müsste ich mir die Frage stellen, wenn ich ein stationäres Gerät zur Aufnahme verwenden würde, wie ich die Wolfs-Bilder mit nicht Wolfs-Bilder filtere. Ich sollte nur die Wolfs-Bilder speichern, um nicht mehrheitlich Fehl-Bilder zu erhalten.

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
      <td>Raspberry Pi Lüfter:<br>
        https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_luefter_fuer_raspberry_pi_5-360116?q=%2Fapi%2Fuser%2FcountrySelect%2Fde%2Fhttps%3A%2F%2Fwww.reichelt.de%2Fde%2Fde%2Fshop%2Fprodukt%2Fraspberry_pi_-_luefter_fuer_raspberry_pi_5-360116 </td>
      <td>5.47 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi AI Beschleuniger:<br>
        https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_shield_-_ai_ki_26_tops_raspberry_pi_5-390448 </td>
      <td>106.86 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi Kamera:<br>
      https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_kamera_12mp_120_v3-339260</td>
      <td>34 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi Flachbandkabel für Kamera:<br>
     https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_flachbandkabel_fuer_kamera_20_cm-360118</td>
      <td>1.20 Fr.</td>
    </tr>
        <tr>
      <td>microSD-Karte: <br>
        https://www.digitec.ch/de/s1/product/sandisk-extreme-microsdxc-sd-s-microsdxc-256-gb-u3-uhs-i-speicherkarte-20932251?supplier=406802&utm_source=google&utm_medium=cpc&utm_campaign=PROD_CH_PMAX_M6_C4&campaignid=21028347765&adgroupid=&adid=&dgCidg=Cj0KCQiA8q--BhDiARIsAP9tKI3RNmOl8y-l3OyqPT_JXIeHUGtxVwzwmUXusCfflVr4PLTbQIVooJAaAhv_EALw_wcB&gad_source=1&gclid=Cj0KCQiA8q--BhDiARIsAP9tKI3RNmOl8y-l3OyqPT_JXIeHUGtxVwzwmUXusCfflVr4PLTbQIVooJAaAhv_EALw_wcB&gclsrc=aw.ds </td>
      <td>28.60 Fr.</td>
    </tr>
    </tr>
        <tr>
      <td>Paketkosten Tierpark Dählhölzli
      <td>10.50 Fr.</td>
    </tr>
    <tr>
      <td>Raspberry Pi 5:<br>
      https://www.digitec.ch/de/s1/product/raspberry-pi-5-8gb-entwicklungsboard-kit-38955607</td>
      <td>88.90 Fr.</td>
    </tr>
    <tr>
      <td>Stick?</td>
      <td></td>
    </tr>
  </tbody>
</table>
