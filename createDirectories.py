# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:49:16 2020

@author: madank
"""

import os
import pandas as pd
import shutil as sh

def createDirectories(folder, excelFile, image_folder, destination_folder):
    path = "./Diabetic Retina"
    fileList = os.listdir(path) # get file list in the path directory
    img_folder = os.listdir(path+"/"+image_folder)
    
    # list files
    for f in fileList: 
        print(f)
        
    # populate train.csv into a pandas DataFrame
    train = pd.read_csv(path +"/"+ excelFile)
    print(train.shape) # print DataFrame shape
    print(train.head()) # print first 5 records of the DataFrame
    print(train['level'].value_counts())
    
    for i in range(len(train)):
        image  = train.loc[i, 'image']
        folder = train.loc[i, 'level']
        
        print(folder)
        for filename in img_folder:
            if filename.startswith(image):
                if folder==0:
                    sh.copy(path+"/"+image_folder+"/"+image+".jpeg",path+"/"+destination_folder+"/0")
                elif folder==1:
                    sh.copy(path+"/"+image_folder+"/"+image+".jpeg",path+"/"+destination_folder+"/1")
                elif folder==2:
                    sh.copy(path+"/"+image_folder+"/"+image+".jpeg",path+"/"+destination_folder+"/2")
                elif folder==3:
                    sh.copy(path+"/"+image_folder+"/"+image+".jpeg",path+"/"+destination_folder+"/3")
                elif folder==4:
                    sh.copy(path+"/"+image_folder+"/"+image+".jpeg",path+"/"+destination_folder+"/4")
        

createDirectories("Diabetic Retiina" , "trainLabels.csv", "train", "DR_Classify")      