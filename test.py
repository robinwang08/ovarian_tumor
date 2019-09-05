
import os
from glob import glob
import pathlib
import os.path
from os import path

patho = 'C:/Users/Robin/Downloads/raw2'
baseDir = os.path.normpath(patho)
files = glob(baseDir+'/*/T2/*.nrrd')

for file in files:
    filePath, fileName = os.path.split(file)
    if fileName == 'segMask_tumor.seg.nrrd':
        continue


    name, ext = fileName.split('.')
    newPath = filePath + '\\' + name + '.nii'

    if path.exists(newPath):
      continue

    loadStart = '[success, loadedVolumeNode] = slicer.util.loadVolume("'
    loadNext = loadStart + file + '", returnNode=True)'
    p = pathlib.PureWindowsPath(loadNext)
    print(p.as_posix())
    saveStart = 'slicer.util.saveNode(loadedVolumeNode, "'
    saveNext = saveStart + newPath + '")'
    p = pathlib.PureWindowsPath(saveNext)
    print(p.as_posix())
