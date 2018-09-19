# Labelling of the apk files as malware or benign

<b>How to use:</b>

git clone <br>
cd Thesis <br>
mkdir input <br> <br>

Paste the directory e.g. 'Malware Dataset' which contains apk files in the 'input' directory created above. <br><br>

In python(2) shell:<br>
import malware_data_extract_script as ms<br>
ms.extract('Malware Dataset') //'Malware Dataset' is the directory which contains the apk files, It's name has to be passed.<br>

<b>Output:</b> <br>
The script generates two files in the output directory:<br>
1) malware_list.csv which contains the evaluation of the apk file gainst each antivirus on virustotal.com <br>
2) malware_score.csv which contains total and positives for each apk file <br>
