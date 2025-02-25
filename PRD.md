# Abstract
In diesem Projekt entwickle ich eine Künstliche Intelligenz, die Wölfe aus der Vogelperspektive erkennt und die Position des Wolfes auf dem Bild zurückgeben kann. Die KI soll auf einem Raspberry Pi eigenständig laufen können. 
# Programmbeschrieb
## Arbeitsschritte
### Erstellung Datenset
Im ersten Arbeitsschritt gilt es, die Wolfs-Aufnahmen zu sammeln. Dafür muss ich mit einem Zoo zusammenarbeiten, der Wölfe in Besitz hat. Sobald ich über die Aufnahmen verfüge, lade ich das Videomaterial in ein Python-File in VS Code. Dieses extrahiert mithilfe von OpenCV beispielsweise alle halbe Sekunde das aktuelle Frame und speichert dieses als ein neues Bild. Somit können aus wenigen Dateien für die Videos mehrere Tausend Fotos entstehen. Danach müssen die Bilder möglicherweise noch in der Auflösung verkleinert werden, sodass die KI nicht zu gross wird und später auch auf einem Raspberry Pi funktionieren kann. Dafür kann ebenfalls OpenCV in VS Code verwendet werden. Der nächste Schritt ist, die Bilder mit der Position des Wolfes zu beschriften. Zuletzt wird noch das Datenset mit nochmals der gleichen Menge an Bildmaterial, dieses Mal aber mit Nicht-Wolfs-Bildern, vervollständigt und als "kein Wolf" beschriftet. 
#### Auswahl Zoo
Bereits angefragte Zoos sind der Tierpark Dählhölzli Bern, der Tierpark Wilhelma in Stuttgart, der Wildnispark Zürich Langenberg, der Wildpark Bruderhaus in Zürich, der Alpenzoo in Innsbruck und der Alternativer Wolf- und Bärenpark im Schwarzwald. Als Backup wären der Parc Animalier de Sainte-Croix in Frankreich, der Juraparc Vallorbe und der Zoo la Garenne in Waadt Möglichkeiten. 

Letzte Aktualisierung am 24.02.25: Der Tierpark Dählhölzli in Bern hat mir angeboten, dass ein Tierpfleger des Tierparkes mit seiner Drohne die Aufnahmen für mich machen würde. Zuletzt habe ich ihnen dafür eine Beschreibung zugesendet, was ich genau bräuchte. 
#### Aufnahme des Bildmaterials
Prinzipiell gibt es zwei Ansätze für die Aufnahme des Bildmaterials. 
Eine Möglichkeit wäre, eine Drohne in größerer Höhe über die Wölfe fliegen zu lassen. Alternativ könnte eine stationäre Kamera für einen begrenzten Zeitraum an einem erhöhten Punkt installiert werden, um die Wölfe von oben zu filmen. Für beide Optionen brauche ich ungefähr 1,5 Stunden Videomaterial, in dem der Wolf aus der Vogelperspektive sichtbar ist. Es ist egal, auf wie viele Teilvideos die Aufnahmen verteilt sind – wichtig ist nur, dass die Drohne / der Wolf bei einem stationären Gerät nicht an Ort und Stelle bleibt, sondern in Bewegung ist, um verschiedene Situationen und Blickwinkel einzufangen. Die Höhe der Aufnahmen überlasse ich den Gegebenheiten vor Ort, denn oftmals ist das Wolfs-Gehege stark bewaldet, was z.B. einen Drohnenflug stark eingrenzt. Der Wolf sollte auf den Aufnahmen einfach gut erkennbar sein. 
#### Beschriftung des Bildmaterials
Um das Bildmaterial zu beschriften, kann das Bildmaterial z.B. per API automatisiert in Chat GPT hereingeladen werden. Danach kann ein Prompt für die Position des Wolfes gestellt werden und anschliessend die Rückgabe in einem grossen Datenset dem Bild zugeordnet werden. Jedoch wird dieses Verfahren nur mit 80 % des Bildmaterials durchgeführt. Die anderen 20 % des Bildmaterials werden später für das Testen der KI benötigt. 
Alternativen zu Chat GPT sind <a href="https://labelbox.com/ ">Labelbox</a>, <a href="https://roboflow.com/annotate">Roboflow</a>, Labellmg und <a href="https://www.makesense.ai/ ">Makesense.Ai</a>
### Installierung eines YOLO-Models
### Training des YOLO-Models mit eigenem Datenset
### Überprüfung der Erfolgsquote der KI
Um die Erfolgsquote der KI zu ermitteln, werden die restlichen 20 % des Bildmaterials in die KI geladen. <br>
Siehe Link: https://labelyourdata.com/articles/object-detection-metrics
### Installierung der KI auf einem Raspberry Pi
Die KI kann nun auf den Raspberry Pi herüberkopiert (z.B. im Dateiformat TensorFlow Lite) werden. Dazu muss nur der Raspberry Pi über SSH an den Computer verbunden sein. Damit die Erkennung auch problemlos mit der Raspberry Pi Kamera funktioniert, müssen die Auflösung und das Bildformat an das Bildmaterial angepasst werden, das für das Training der KI verwendet wurde. Deshalb muss man die Bilder der Kamera nach Erhalt etwas anpassen, bevor man sie in die KI gibt. Ebenso darf z.B. nur alle halbe Sekunde ein Bild an die KI weitergegeben werden, sodass verhindert wird, dass der Raspberry Pi nicht überbeansprucht wird. 
#### Voraussetzungen
Um ein neuronales Netzwerk auf einem Raspberry Pi laufen lassen zu können, benötige ich einen Raspberry Pi AI Beschleuniger und einen Kühler. Ebenso muss der Raspberry Pi mit einer Kamera ausgestattet werden. 
## Optionale Features
* Da ich die Wolfs-Bilder nicht mit einer Wärmebildkamera (Stand: 24.02.25) aufnehmen kann, aber den Wolf auch in Dunkelheit erkennen möchte, könnte ich ein Wärmebild-Filter über das Bildmaterial legen. Anschliessend könnte ich die KI neu trainieren und testen, wie gut das System nun auch Wölfe in der Nacht erkennen kann.
# Skizze
# Technische Details

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
      https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_kamera_1_6mp_shutter_c-_cs-fassung-345205</td>
      <td>52.33 Fr.</td>
    </tr>
   <tr>
   <td>Raspberry Pi Kamera-Objektiv:<br>
        Option 1 (Weitwinkel): <a href="https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_objektiv_fuer_cs-fassung_6mm_weitwinkel-276922">6mm Weitwinkel</a><br>
        Option 2 (Teleobjektiv): <a href="https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_objektiv_fuer_c-fassung_16mm_teleobjektiv-276921">16mm Teleobjektiv</a>
    </td>
    <td>Option 1:<br>
        24.95 Fr.<br>
        Option 2:<br>
        52.30 Fr.
    </td>
    </tr>
    <tr>
      <td>Raspberry Pi Flachbandkabel für Kamera:<br>
      https://www.reichelt.com/ch/de/shop/produkt/raspberry_pi_-_kabel_flachbandkabel_fuer_kamera_30_cm-360119</td>
      <td>2.18 Fr.</td>
    </tr>
  </tbody>
</table>
