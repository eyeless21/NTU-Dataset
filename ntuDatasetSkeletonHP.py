import os,shutil
import os.path
import sys
from os import path
import csv
from pathlib import Path
import fileinput

fileNamesF = []

#Path of skeleton files && Path of the new skeleton.csv files
original_skeleton_location = #path 
base_directory = #path 

#Check and create path for the new csv files 
if  not os.path.exists(#path):
    os.mkdir(base_directory)

#Check and create path for healthAction files
healthActions_directory = os.path.join(base_directory,'healthActions')
if not os.path.exists(healthActions_directory):
    os.mkdir(healthActions_directory)

#copy files to healthActions directory
def copyFiles():
    for fileName in fileNames:
        try:
            source = os.path.join(original_skeleton_location, fileName)
            dest = os.path.join(healthActions_directory, fileName)
            shutil.copyfile(source, dest)
        except OSError:
            pass

#copy skeleton files to a new destination
fileNames = ['S00{}C00{}P00{}R00{}A0{}.skeleton'.format(s,c,p,r,a)
    for s in range(1,10,2)
    for c in range(1,4)
    for p in range(1,9)
    for r in range(1,3) 
    for a in range(41,50)]
fileNamesF.append(fileNames)
copyFiles()

fileNames = ['S0{}C00{}P00{}R00{}A0{}.skeleton'.format(s, c, p, r, a)
             for s in range(11,18, 2)
             for c in range(1, 4)
             for p in range(1, 9)
             for r in range(1, 3)
             for a in range(41, 50)]
fileNamesF.append(fileNames)
copyFiles()

fileNames = ['S00{}C00{}P0{}R00{}A0{}.skeleton'.format(s, c, p, r, a)
             for s in range(1, 10, 2)
             for c in range(1, 4)
             for p in range(10, 40)
             for r in range(1, 3)
             for a in range(41, 50)]
fileNamesF.append(fileNames)
copyFiles()

fileNames = ['S0{}C00{}P0{}R00{}A0{}.skeleton'.format(s, c, p, r, a)
             for s in range(11, 18, 2)
             for c in range(1, 4)
             for p in range(10,40)
             for r in range(1, 3)
             for a in range(41, 50)]
fileNamesF.append(fileNames)
copyFiles()

#Convert skeleton files to csv
base_dir = Path(healthActions_directory).resolve(strict=True)
#print(f"renaming in {base_dir}")

prefix = "\\\\?\\" if sys.platform == "win32" else ""

for src in base_dir.glob("**/*"):
    if src.is_dir():
        continue
    dst = src.with_suffix('.csv')
    if not dst.exists():
        try:
            os.rename(f"{prefix}{src}", f"{prefix}{dst}")
            #print(f"Renamed {src}")
        except Exception as e:
            pass
            #print(f"Error renaming: {e}")

#Delete the first row on every CSV file
for k in range(4):
    for filename in os.listdir(healthActions_directory):
        with open(os.path.join(healthActions_directory, filename), 'r') as fin:
            data = fin.read().splitlines(True)
        with open(os.path.join(healthActions_directory, filename), 'w') as fout:   
            fout.writelines(data[1:])

#Open the file and write the first 25 lines every 28 lines 
for filename in os.listdir(healthActions_directory):
    i = 1
    j = 25
    with open(os.path.join(healthActions_directory, filename), 'r') as fin:
        data = fin.read().splitlines(True)
        num_lines = sum(1 for line in open(os.path.join(healthActions_directory, filename)))
    with open(os.path.join(healthActions_directory, filename), 'w') as fout:
        while j < num_lines:  
         fout.writelines(data[i:j])
         i = i+28
         j = j+28
         
#Replace spaces with commas
for filename in os.listdir(healthActions_directory):
    f = open(os.path.join(healthActions_directory, filename), 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(' ', ',')

    f = open(os.path.join(healthActions_directory, filename), 'w')
    f.write(newdata)
    f.close()
    
#----------------------------------------------------------------------------------------------
    #Create a folder for every ntu action
#folders = ['A041', 'A042', 'A043', 'A044',
#           'A045', 'A046', 'A047', 'A048', 'A049']
#if os.path.exists(healthActions_directory):
#    for folder in folders:
#        try:
#            os.mkdir(os.path.join(healthActions_directory, folder))
#        except Exception as e:
#            pass
#
#actionList = []
#source = healthActions_directory
#
##Move files based on their Action
#def moveCSV():
#    j = 0
#    for root, dirs, files in os.walk(healthActions_directory):
#        for name in files:
#            j = 0
#            for name2 in files:
#                try:
#                    if name.endswith('%s.csv' % folders[j]):
#                        src = os.path.join(healthActions_directory, name)
#                        dest = os.path.join(
#                            healthActions_directory, folders[j], name)
#                        shutil.move(src, dest)
#                except Exception as e:
#                    pass
#                j = j+1
#
#moveCSV()

