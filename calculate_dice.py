import csv
import os
import argparse
import glob
import nrrd
import re
import numpy as np
import pandas
from sklearn import preprocessing as sklearn_preprocessing
from itertools import combinations

from config import config
from filenames import ACCEPTED_FILENAMES
from segmentation import calculate_volume

from filenames import IMAGE, SEGMENTATION, T1, T2

def dice_score(seg_1, seg_2):
    return np.sum(seg_1[seg_2==1])*2.0 / (np.sum(seg_1) + np.sum(seg_2))

def run(files, nicknames, features, out):
    feat = pandas.read_pickle(features)

    by_index = dict() # index > nicknames > (t1_seg, t2_seg)

    nickfiles = dict()
    filesnick = dict()
    for i, f in enumerate(files):
        nickfiles[nicknames[i]] = f
        filesnick[f] = nicknames[i]

    for f in files:
        df = pandas.read_pickle(f)
        for index, row in df.iterrows():
            t1_seg = row.to_frame().loc["path", T1, SEGMENTATION][0]
            t2_seg = row.to_frame().loc["path", T2, SEGMENTATION][0]
            d = by_index.get(index, dict())
            d[filesnick[f]] = (t1_seg, t2_seg)
            by_index[index] = d

    scores = list()
    for index, names in by_index.items():
        loaded = dict()
        for f in names.values():
            loaded[f[0]] = nrrd.read(f[0])[0]
            loaded[f[1]] = nrrd.read(f[1])[0]
        if len(names.keys()) < 2:
            continue
        for first, second in combinations(names.keys(), 2):
            try:
                #t1
                scores.append(dict(
                    index=index,
                    first=first,
                    second=second,
                    outcome=feat.loc[index]["outcome"],
                    modality="t1",
                    score=dice_score(loaded[names[first][0]], loaded[names[second][0]]),
                ))
            except:
                print("could not match these two: {}: {} <=> {}: {}".format(first, names[first][0], second, names[second][0]))
                print("sizes: {}, {}".format(loaded[names[first][0]].shape, loaded[names[second][0]].shape)),
            try:
                #t2
                scores.append(dict(
                    index=index,
                    first=first,
                    outcome=feat.loc[index]["outcome"],
                    second=second,
                    modality="t2",
                    score=dice_score(loaded[names[first][1]], loaded[names[second][1]]),
                ))
            except:
                print("could not match these two: {}: {} <=> {}: {}".format(first, names[first][1], second, names[second][1]))
                print("sizes: {}, {}".format(loaded[names[first][1]].shape, loaded[names[second][1]].shape)),
    return pandas.DataFrame(scores)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        type=str,
        nargs="+",
        help='pkl files of to_process features')
    parser.add_argument(
        '--nicknames',
        type=str,
        nargs="+",
        help='nicknames for pkl files')
    parser.add_argument(
        '--features',
        type=str,
        default=config.RAW_FEATURES,
        help='features')
    parser.add_argument(
        '--out',
        type=str,
        help='output folder')
    FLAGS, unparsed = parser.parse_known_args()
    run(FLAGS.files, FLAGS.nicknames, FLAGS.features, FLAGS.out)
