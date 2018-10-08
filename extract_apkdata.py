import requests, sys, csv, datetime, os, time, re, glob
import xml.etree.ElementTree as ET 

numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def extract(dirname):
    print "Extracting information from the apk files:"
    path = 'input/' + dirname + '/'
    cmd1 = "unzip "
    cmd = "apktool d "
    for file in sorted(glob.glob(os.path.join(path, '*.apk')), key=numericalSort):
        filename = file.split('/')[2]
        print "Extraction the information from apk file ", filename
        os.system(cmd + "'" + path + filename + "'")

    outputdir = "output/Extracted Data/"
    os.system("mkdir 'output/Extracted Data'")
    
    for d in os.listdir(os.getcwd()):
        if os.path.isdir(d):
            if(d.isdigit()):
                tree = ET.parse(os.path.join(d + "/AndroidManifest.xml"))
                root = tree.getroot()
                permissions = []
                for child in root:	
                    if child.tag == 'uses-permission':
                        permissions.append(child.attrib['{http://schemas.android.com/apk/res/android}name'])
                outputfile = open(outputdir + d + '.txt', 'w')
                with outputfile as f:
                    for permission in permissions:
                        f.writelines(permission +  '\n')
    print "Extraction Done"
