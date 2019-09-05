#!/usr/bin/python
import os
from glob import glob
import nibabel as nib
import numpy as np
from shutil import copyfile

def n4_bias_correction(image):
    import ants
    as_ants = ants.from_numpy(image)
    corrected = ants.n4_bias_field_correction(as_ants)
    return corrected.numpy()

def imageNorm():
    patho = '/media/user1/my4TB/robin/ovarian/ovarian_data/raw1'
    baseDir = os.path.normpath(patho)
    files = glob(baseDir + '/*/T1POST/imagingVolume-resampled.nii')
    labels = glob(baseDir + '/*/T1POST/segMask_tumor-resampled.nii')

    for file in files:
        filePath, fileName = os.path.split(file)
        a = filePath.split('/')

        print('starting with file ' + file)

        startPath = '/media/user1/my4TB/robin/ovarian/ovarian_data/normalized/'
        nePath = startPath + a[8]
        neePath = nePath + '/T1POST'
        newPath = neePath + '/' + fileName

        if not os.path.isdir(startPath):
            os.mkdir(startPath)

        if not os.path.isdir(nePath):
            os.mkdir(nePath)

        if not os.path.isdir(neePath):
            os.mkdir(neePath)

        n1_img = nib.load(file)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img = n4_bias_correction(img)
        imgmax = img.max()
        img = np.true_divide(img, imgmax)
        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newPath)
        print('finished with file ' + file)

    for label in labels:
        filePath, fileName = os.path.split(label)
        a = filePath.split('/')

        print('starting with mask ' + label)

        startPath = '/media/user1/my4TB/robin/ovarian/ovarian_data/normalized/'
        nePath = startPath + a[8]
        neePath = nePath + '/T1POST'
        newPath = neePath + '/' + fileName

        copyfile(label, newPath)

        print('finished moving mask ' + label)

def maskNorm():
    patho = '/media/user1/my4TB/robin/ovarian/ovarian_data/raw2'
    baseDir = os.path.normpath(patho)
    files = glob(baseDir + '/*/T2/imagingVolume-resampled.nii')
    labels = glob(baseDir + '/*/T2/segMask_tumor-resampled.nii')

    for file in files:
        filePath, fileName = os.path.split(file)
        a = filePath.split('/')

        print('starting with file ' + file)

        startPath = '/media/user1/my4TB/robin/ovarian/ovarian_data/normalized/'
        nePath = startPath + a[8]
        neePath = nePath + '/T2'
        newPath = neePath + '/' + fileName

        if not os.path.isdir(startPath):
            os.mkdir(startPath)

        if not os.path.isdir(nePath):
            os.mkdir(nePath)

        if not os.path.isdir(neePath):
            os.mkdir(neePath)

        n1_img = nib.load(file)
        n1_header = n1_img.header
        n1_affine = n1_img.affine
        img = n1_img.get_fdata()
        img = n4_bias_correction(img)
        imgmax = img.max()
        img = np.true_divide(img, imgmax)
        new_img = nib.Nifti1Image(img, n1_affine, n1_header)
        nib.save(new_img, newPath)
        print('finished with file ' + file)

    for label in labels:
        filePath, fileName = os.path.split(label)
        a = filePath.split('/')

        print('starting with mask ' + label)

        startPath = '/media/user1/my4TB/robin/ovarian/ovarian_data/normalized/'
        nePath = startPath + a[8]
        neePath = nePath + '/T2'
        newPath = neePath + '/' + fileName

        copyfile(label, newPath)

        print('finished moving mask ' + label)

imageNorm()
maskNorm()