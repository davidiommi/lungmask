import os
import shutil
from time import time

import numpy as np
import SimpleITK as sitk
import scipy.ndimage as ndimage

import lungmask
from lungmask import mask

if __name__ == "__main__":


    input_image = sitk.ReadImage('./imagesTr/lung_016.nii.gz')
    segmentation = mask.apply(input_image)
    save_file = sitk.GetImageFromArray(segmentation)
    save_file.SetSpacing(input_image.GetSpacing())
    save_file.SetDirection(input_image.GetDirection())
    save_file.SetOrigin(input_image.GetOrigin())

    sitk.WriteImage(save_file, './results/lung_016_results.nii.gz')