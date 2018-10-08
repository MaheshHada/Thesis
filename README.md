# Labelling of the apk files as malware or benign

<b>How to use and Input:</b>

git clone https://github.com/MaheshHada/Thesis.git <br>
cd Thesis <br>
mkdir input <br> <br>

Paste the directory e.g. 'Malware Dataset' which contains apk files in the 'input' directory created above. <br><br>

In python(2) shell:<br> <br>
import malware_data_extract_script as ms<br>
ms.extract('Malware Dataset') <br> <br>
Note: 'Malware Dataset' is the directory which contains the apk files, It's name has to be passed in the extract function.<br> <br>

<b> For extracting the permissions from the apk file </b> <br>
import extract_apkdata as ep <br>
ep.extract('Malware Dataset') <br><br> 

<b>Output:</b> <br>
The script generates two files in the output directory:<br>
1) <b>malware_list.csv</b> which contains the evaluation of each apk file against all antivirus on virustotal.com <br>
2) <b>malware_score.csv</b> which contains total and positives ran accross all the antivirus for each apk file on virustotal.com<br>
3) creates a directory <b>Extracted Data</b> in output directory which includes a seperate text file with permissions for each apk file. <br>
