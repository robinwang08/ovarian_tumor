import os
from glob import glob

path = 'C:/Users/Robin/Downloads/raw2'
baseDir = os.path.normpath(path)
files = glob(baseDir+'/*/*/*.nrrd')
dcmfiles = glob(baseDir+'/*/*/*.dcm')


for file in files:
    os.remove(file)

for file in dcmfiles:
    os.remove(file)

t1files = glob(baseDir+'/*/T1/*')
for file in t1files:
    os.remove(file)
