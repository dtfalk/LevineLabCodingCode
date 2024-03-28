# some packages we want to import
# os is for file names/locations
# pandas is for reading and saving files
import os
import pandas as pd

if __name__ == '__main__':

    # gets the locations of where we load the excel files from and where
    # we save the csv files to
    curDir = os.path.dirname(__file__)
    loadFolder = os.path.join(curDir, 'transcriptsFolderExcel')
    saveFolder = os.path.join(curDir, 'transcriptsFolder')

    # stores the names of the excel files as a python list
    excelFilesNames = os.listdir(loadFolder)
    
    # iterates over all of the excel files that we are going to convert to csv files
    for excelFileName in excelFilesNames:

        # gets the location of the excel files and the location where we will save
        # the converted csv file to
        csvFileName = excelFileName.replace('.xlsx', '.csv') # changes the '.xlsx' to '.csv'
        loadPath = os.path.join(loadFolder, excelFileName)
        savePath = os.path.join(saveFolder, csvFileName)

        # read the excel file into a "pandas dataframe"
        excelFile = pd.read_excel(loadPath)

        # takes the data frame and saves it as a csv file in the proper location
        excelFile.to_csv(savePath, index = False)
