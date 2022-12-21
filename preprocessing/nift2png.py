
import numpy as np
import cv2
import nibabel as nib 
import os
input_image_mask = nib.load(r'D:\AI_Ethiopia\Stroke project 1\stroke dataset\new organized\hemoragic stroke\22\22\Manual_Mask_1_Reader_1.nii')  
for i in range(input_image_mask.shape[2]):  
    input_slice_mask = np.asarray(input_image_mask.get_fdata()) [:,:,i].astype(np.float32)  
    if len(input_slice_mask.shape)==2:  
        #input_slice_mask = np.expand_dims(input_slice_mask, axis=1)  
        path_mask = os.path.join(r'D:\AI_Ethiopia\Stroke project 1\stroke dataset\new organized\hemoragic stroke\22\22\Manual_Mask_1_Reader_1' + str(i) + ".png")  
        cv2.imwrite(path_mask, input_slice_mask)  
