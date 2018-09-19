# Labelling of the apk files as malware or benign

How to use:

git clone 
cd Thesis
mkdir input

Paste the directory e.g. 'Malware Dataset' which contains apk files in the 'input' directory created above.

In python(2) shell:
import malware_data_extract_script as ms
ms.extract('Malware Dataset') //'Malware Dataset' is the directory which contains the apk files, It's name has to be passed.

Output:
The script generates two files in the output directory:
1) malware_list.csv
2) malware_score.csv
