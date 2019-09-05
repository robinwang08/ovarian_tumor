import os
import sys
import glob
from shutil import copy

all_nrrd = glob.glob("{}/**/*.nrrd".format(sys.argv[1]), recursive=True)

rename_dict = dict()

for name in all_nrrd:
    new_name = name.replace(sys.argv[1], "")
    new_name = new_name.replace("(1)", "")
    new_name = new_name.replace("MRN C", "2")
    new_name = new_name.replace("MRN", "segMask_tumor")
    split_name = new_name.split("/")
    new_name = "{}/{}-1/{}".format(sys.argv[2], split_name[0], "/".join(split_name[1:]))
    rename_dict[name] = new_name

for key, value in rename_dict.items():
    print("{}\t\t->\t\t{}".format(key, value))
    os.makedirs(os.path.dirname(value), exist_ok=True)
    copy(key, value)
