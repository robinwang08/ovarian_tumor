from glob import glob
import pathlib
import os.path
from os import path
import shutil


patho = 'C:/Users/Robin/Downloads/raw1'
baseDir = os.path.normpath(patho)
files = glob(baseDir + '/*/T2/*.nii')

for file in files:
    filePath, fileName = os.path.split(file)
    a = filePath.split('\\')


    nePath = 'C:/Users/Robin/Downloads/raw2/' + a[5]
    neePath = nePath + '/T2'
    newPath = neePath + '/' + fileName

    if not os.path.isdir(nePath):
        os.mkdir(nePath)

    if not os.path.isdir(neePath):
        os.mkdir(neePath)

    shutil.move(file, newPath)