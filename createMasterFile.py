# written by David Falk, employee at APEX Lab/Nusbaum Lab at UChicago
# for Dani's senior Thesis as a member of the Levine Lab at UChicago
# (2024)

import os
import csv

# This code is all that you, the experimenter, might need to change
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# name of the folder where the transcript csvs are stored (we load data from this folder)
CSVtranscriptsFolderName = 'transcriptsFolder' 

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


# The code below contains helper functions for the "main" part of the code
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# this helper function returns the folder containing all of the subject transcript CSVs
# and the location of the master file and the error file
def getPaths():
    
    # the location of this file (dirname returns the location of the file minus the file's name)
    curDir = os.path.dirname(__file__)

    # these are the paths for loading the data (transcripts) and for saving the data (masterFile and errorFile)
    # os.path.join() concatenates a list of names into one long address
    # so we .... 
    # 1) take the current location of this file (curDir)
    # 2) add the name of either the load or save folder (either 'transcriptsFolderName' or 'saveFolderName')
    # 3) For the save files, add the filename (either 'masterFileName' or 'errorFileName')
    # The result is the full location of either where we are loading the data from or loading the data to
    transcriptsFolderPath = os.path.join(curDir, CSVtranscriptsFolderName) 
    saveFolderPath = os.path.join(curDir, saveFolderName)
    masterFileSavePath = os.path.join(saveFolderPath, masterFileName)
    errorFileSavePath = os.path.join(saveFolderPath, errorFileName)
    # ------------------------------------------------------------------------------

    # This code is for making the save folder 
    os.makedirs(saveFolderPath, exist_ok = True)
    
    # returns the location of the transcripts and the location where we will save the data to
    return transcriptsFolderPath, masterFileSavePath, errorFileSavePath

# gets the results for one subject's files
def getResults(subjectFile, transcriptsFolderPath):

    # get the location of the subject's data file
    subjectFilePath = os.path.join(transcriptsFolderPath, subjectFile)

    # Gets the subject's ID number
    subjectID = os.path.basename(subjectFile).replace('.csv', '')

    # initialize empty lists for data collection
    results = [subjectID] + (['0'] * len(codes))
    errors = []

    # open the transcript to read the subject's data
    with open(subjectFilePath, 'r', newline = '') as f:
        
        reader = csv.reader(f)
        lines = list(reader)

        for lineIndex, line in enumerate(lines):

            # variable for keeping track of if the label matches any of our labels.
            labelFound = False 

            # skip this label if it is a blank line,
            # if it is the last line (the files sent to me had a list of 0's as the very last line),
            # or if there is a header (the files sent to me had 3 lines of headers so I needed to skip those lines)
            if len(line) == 0: # or lineIndex < 3 or lineIndex == len(lines) - 1:
                continue
            
            # extract the label from the line, make lowercase, remove all spaces, and split by dashes
            label = line[0].lower().replace(' ', '').split('-')

            # iterate over codes to see if we find a match
            for codeIndex, code in enumerate(codes):
                splitCode = code.lower().replace(' ', '').split('-')
                if len(label) == len(splitCode) and label[0] == splitCode[0]:
                    if all([label[i] in splitCode[i] for i in range(1, len(label))]):
                        results[codeIndex + 1] = str(int(results[codeIndex + 1]) + 1)
                        labelFound = True 
                        break 

            # adds the code to the list of errors if it doesn't match one of our labels
            if not labelFound:
                errors.append([str(subjectID), '-'.join(label), str(lineIndex + 1)])

        # return the labels we found a match for (results) and the labels we did not find a match for (errors)
        # in a format that we can use to write them to a csv file. Happy to explain more about how this formatting works! just ask!
        return results.copy(), errors.copy()

        
    
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# this is the "launchpad" of the code
# The order in which the code runs is determined by the order of the code below
# Any functions above this are helper functions that get run in the code below
def main():

    # retrieves the load and save locations and creates the save folder
    transcriptsFolderPath, masterFileSavePath, errorFileSavePath = getPaths()
    
    # lists to store results and errors
    resultsList = []
    errorsList = [] 
    
    # iterates over all of the subject files in the transcript folder
    for subjectFile in os.listdir(transcriptsFolderPath):
        
        # For each transcript, retrieve the data from the subject's csv file 
        results, errors = getResults(subjectFile, transcriptsFolderPath)

        # add the results to the list of results
        resultsList.append(results)

        # add the errors to the list of errors
        errorsList.extend(errors)

    
    # creates the header (subject ID + code + line) and writes the data for the error file
    errorFileHeader = ['Subject ID', 'code', 'line']

    with open(errorFileSavePath, mode = 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(errorFileHeader)
        for error in errorsList:
            writer.writerow(error)
    
    # creates the header (subject ID + codes) and writes the data for the master file
    masterFileHeader = ['Subject ID']
    for code in codes:
        masterFileHeader.append(str(code))

    with open(masterFileSavePath, mode = 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(masterFileHeader)
        for result in resultsList:
            writer.writerow(result)

if __name__ == '__main__':
    main()