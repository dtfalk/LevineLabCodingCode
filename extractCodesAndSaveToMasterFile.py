# written by David Falk, employee at APEX Lab/Nusbaum Lab at UChicago
# for Dani's senior Thesis as a member of the Levine Lab at UChicago
# (2024)

# This code is all that you, the experimenter, might need to change
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# name of the folder where the transcript csvs are stored (we load data from this folder)
transcriptsFolderName = 'transcriptsFolder' 

# name of the folder where we store the outputted master file and error file (we save data to this folder)
saveFolderName = 'saveFolder'

# name of the master file
masterFileName = 'masterFile.csv'

# name of the error file (file for improperly entered codes that may need human review)
errorFileName = 'errorFile.csv'

# python list for each type of code
relationalMathCodes = ['RM-Comparison', 'RM-Relational Mapping', 'RM-Self Connection', 'RM-Calculation',
         'RM-Proportion', 'RM-Definition', 'RM-Inference']
relationalNonMathCodes = ['RN-Comparison', 'RN-Relational Mapping', 'RN-Self Connection', 
                        'RN-Inference', 'RN-Definition']
QuasiRelationalMathCodes = ['QARM-Comparison', 'QARM-Relational Mapping', 'QARM-Self Connection', 'QARM-Calculation',
         'QARM-Proportion', 'QARM-Definition', 'QARM-Inference']
QuasiRelationalNonMathCodes = ['QARN-Comparison', 'QARN-Relational Mapping', 'QARN-Self Connection', 
                        'QARN-Inference', 'QARN-Definition']
nonRelationalMathCodes = ['NM-Label', 'NM-BF', 'NM-Repeat', 'NM-Affirmation']
nonRelationalNonMathCodes = ['NN-Label', 'NN-BF', 'NN-SE', 'NN-Affirmation', 'NN-Repeat']
noDashCodes = ['other', 'offtask']

# master list of all of the codes
codes = relationalMathCodes + relationalNonMathCodes + \
        QuasiRelationalMathCodes + QuasiRelationalNonMathCodes + \
        nonRelationalMathCodes + nonRelationalNonMathCodes + noDashCodes
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# The code below is for importing some modules for creating files and csvs and etc...
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# import os ("operating system") to create folders, find folders/files
# and to make sure that this code will run on any operating system (Mac, Windows, Linux)
import os

# import csv so that we can read from the subjects' CSVs and write to the master file and error file
# these csv files are small so we don't need anything crazy like Pandas or Numpy
import csv
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------



# The code below contains helper functions for the "main" part of the code
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# this helper function returns the folder containing all of the subject transcript CSVs
# and the location of the master file and the error file
def getPaths():

    # these lines are for where we load the data from and where we save the data to
    # ------------------------------------------------------------------------------
    
    # returns the location of this file (dirname returns the location of the file minus the file's name)
    curDir = os.path.dirname(__file__)

    # these are the paths for loading the data (transcripts) and for saving the data (masterFile and errorFile)
    # os.path.join() concatenates a list of names into one long address
    # so we .... 
    # 1) take the current location of this file (curDir)
    # 2) add the name of either the load or save folder (either 'transcriptsFolderName' or 'saveFolderName')
    # 3) For the save files, add the filename (either 'masterFileName' or 'errorFileName')
    # The result is the full location of either where we are loading the data from or loading the data to
    transcriptsFolderPath = os.path.join(curDir, transcriptsFolderName) 
    saveFolderPath = os.path.join(curDir, saveFolderName)
    masterFileSavePath = os.path.join(saveFolderPath, masterFileName)
    errorFileSavePath = os.path.join(saveFolderPath, errorFileName)
    # ------------------------------------------------------------------------------

    # This code is for making the save folder 
    os.makedirs(saveFolderPath, exist_ok = True)
    
    # returns the location of the transcripts and the location where we will save the data to
    return transcriptsFolderPath, masterFileSavePath, errorFileSavePath

# creates and writes the headers to the master file and the error file
def writeHeaders(masterFileSavePath, errorFileSavePath):
    
    # creates the header (subject ID + codes) for the master file
    masterFileHeader = ['Subject ID']
    for code in codes:
        masterFileHeader.append(str(code))
    
    # creates the header (subject ID + code + line) for the error file
    errorFileHeader = ['Subject ID', 'code', 'line']

    # writes the header to the master file
    with open(masterFileSavePath, 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(masterFileHeader)

    # writes the header to the error file
    with open(errorFileSavePath, 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(errorFileHeader)

# gets the results for one subject's files
def getResults(subjectFile, transcriptsFolderPath):

    # gets the subject ID from the filename and removes the '.csv' at the end of the filename
    subjectID = os.path.basename(subjectFile).replace('.csv', '')

    # initialize empty lists for data collection
    results = [subjectID] + (['0'] * len(codes))
    errors = []

    # open the transcript to read in the data
    
    # returns the location of this file (dirname returns the location of the file minus the file's name)
    subjectFilePath = os.path.join(transcriptsFolderPath, subjectFile)
    with open(subjectFilePath, 'r', newline = '') as f:
        reader = csv.reader(f)
        lines = list(reader)
        labelColumnIndex = 0 # index for the column where the labels are

        for j, line in enumerate(lines):
            labelFound = False # variable for keeping track of if the label matches any of our labels

            # skip if it is a blank line
            if len(line) == 0:
                continue

            label = line[labelColumnIndex] # extract the label
            label = label.lower() # make everything lowercase
            label = label.replace(' ', '') # remove all spaces from the label
            if label.lower() in noDashCodes:
                pass
            else:
                label = label.split('-') # split the label into two parts (before the dash vs after the dash)

            for i, code in enumerate(codes):
                # do what we did to the label to the code
                newCode = code.lower()
                newCode = newCode.replace(' ', '')
                if newCode in noDashCodes:
                    if newCode == label:
                        results[i + 1] = str(int(results[i + 1]) + 1)
                        labelFound = True
                        break
                else:
                    newCode = newCode.split('-')
                    if label[0] in newCode[0] and label[1] in newCode[1]:
                        results[i + 1] = str(int(results[i + 1]) + 1)
                        labelFound = True
                        break
            
            if not labelFound:
                seperator = '-'
                errors.append([str(subjectID), seperator.join(label), str(j + 1)])

        return results, errors


    
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# this is the "launchpad" of the code
# The order in which the code runs is determined by the order of the code below
# Any functions above this are helper functions that get run in the code below
if __name__ == '__main__':

    # retrieves the load and save locations and creates the save folder
    transcriptsFolderPath, masterFileSavePath, errorFileSavePath = getPaths()

    # creates and writes the headers to the master file and the error file
    writeHeaders(masterFileSavePath, errorFileSavePath)
    
    errorsList = []
    # iterates over all of the subject files in the transcript folder
    for subjectFile in os.listdir(transcriptsFolderPath):
        results, errors = getResults(subjectFile, transcriptsFolderPath) # retrieves the data in the subject's csv file
        for error in errors:
            errorsList.append(error)

        # writes the subject's data to the master file
        with open(masterFileSavePath, 'a', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(results)

    # writes any codes not in the codes list to the error file for human review
    with open(errorFileSavePath, 'a', newline = '') as f:
        writer = csv.writer(f)
        for error in errors:
            writer.writerow(error)


