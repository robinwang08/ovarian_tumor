import nrrd
import os
from segmentation import calculate_largest_slice, select_slice, bounding_box, crop, resize
from config import config
import matplotlib.pyplot as plt
from path import Path



def deleteUselessFiles(path):
    d = Path(path)
    allList = d.walkfiles('*')
    for file in allList:
        if not file.endswith(".nrrd"):
            file.remove()    
    return


def load_image(image_path, segmentation_path, verbose=False):
    image, _ = nrrd.read(image_path)
    segmentation, _ = nrrd.read(segmentation_path)
    if verbose:
        print("""
        image: {}
        seg: {}
""".format(image.shape, segmentation.shape))

    largest_plane = calculate_largest_slice(segmentation)
    image, segmentation = select_slice(image, segmentation, largest_plane)

    bounds = bounding_box(segmentation)
    image, segmentation = crop(image, segmentation, bounds)

    masked = image * segmentation
    masked = resize(masked, (config.IMAGE_SIZE, config.IMAGE_SIZE))
    
    return masked

    
    
#load_image('C:/research/renal/data/imagingVolumeL.nrrd', 'C:/research/renal/data/segMask_tumorL.nrrd')
    
def processFiles(path):
    savePath = "C:/Users/Robin/Downloads/OvarianQA/test/"

    if not os.path.isdir(path):
        return
    batch = os.listdir(path)
    for dir in batch:
        batchFolders = os.listdir(path + "/" + dir)
        for folder in batchFolders:
            batchSubFoldersPath = path + "/" + dir + "/" + folder
            batchSubFolders = os.listdir(batchSubFoldersPath)
            for dicom in batchSubFolders:
                if not os.path.isdir(batchSubFoldersPath + "/" + dicom):
                    continue
                if dicom == "DICOM":
                    batchSubFoldersViewsPath = batchSubFoldersPath + "/" + dicom
                    batchSubFoldersViews = os.listdir(batchSubFoldersViewsPath)
                    for modal in batchSubFoldersViews:    
                        imageFile = savePath + dir + "-" + folder + "-" + modal
                        
                        imageVolume1 = batchSubFoldersViewsPath + "/" + modal + "/" + "imagingVolume1.nrrd"
                        segMask1 = batchSubFoldersViewsPath + "/" + modal + "/" + "segMask_tumor1.nrrd"
   
                        imageVolume2 = batchSubFoldersViewsPath + "/" + modal + "/" + "imagingVolume2.nrrd"
                        segMask2 = batchSubFoldersViewsPath + "/" + modal + "/" + "segMask_tumor2.nrrd"
                        
                        imageVolume3 = batchSubFoldersViewsPath + "/" + modal + "/" + "imagingVolume3.nrrd"
                        segMask3 = batchSubFoldersViewsPath + "/" + modal + "/" + "segMask_tumor3.nrrd"                        
                        
                        
                        imageVolume4 = batchSubFoldersViewsPath + "/" + modal + "/" + "imagingVolume4.nrrd"
                        segMask4 = batchSubFoldersViewsPath + "/" + modal + "/" + "segMask_tumor4.nrrd"  
                        
                        imageVolume5 = batchSubFoldersViewsPath + "/" + modal + "/" + "imagingVolume5.nrrd"
                        segMask5 = batchSubFoldersViewsPath + "/" + modal + "/" + "segMask_tumor5.nrrd"
                        
                        try:
                            if os.path.isfile(imageVolume1) and os.path.isfile(segMask1):
                                plotImage = load_image(imageVolume1, segMask1)    
                                plt.imsave(imageFile+"1.png", plotImage)
                            if os.path.isfile(imageVolume2) and os.path.isfile(segMask2):
                                plotImage = load_image(imageVolume2, segMask2)    
                                plt.imsave(imageFile+"2.png", plotImage)
                            if os.path.isfile(imageVolume3) and os.path.isfile(segMask3):
                                plotImage = load_image(imageVolume3, segMask3)    
                                plt.imsave(imageFile+"3.png", plotImage)
                            if os.path.isfile(imageVolume4) and os.path.isfile(segMask4):
                                plotImage = load_image(imageVolume4, segMask4)    
                                plt.imsave(imageFile+"4.png", plotImage)
                            if os.path.isfile(imageVolume5) and os.path.isfile(segMask5):
                                plotImage = load_image(imageVolume5, segMask5)    
                                plt.imsave(imageFile+"5.png", plotImage)    
                        except Exception as e:
                                print(e)
                                print(imageFile)
                              
    return

path = "C:/Users/Robin/Downloads/test"
processFiles(path)
#deleteUselessFiles(path)