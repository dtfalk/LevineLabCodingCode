# written by David Falk, employee at APEX Lab/Nusbaum Lab at UChicago
# for Dani's senior Thesis as a member of the Levine Lab at UChicago
# (2024)

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
    transcriptsFolderPath = os.path.join(curDir, CSVtranscriptsFolderName) 
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

        # iterates over every line of data in the transcript csv file
        for j, line in enumerate(lines):

            # variable for keeping track of if the label matches any of our labels.
            # this resets for each new piece of data, because this represents if we found a match in the codes
            # for a given line/label/piece of data in this transcript
            labelFound = False 

            # skip this label if it is a blank line,
            # if it is the last line (the files sent to me had a list of 0's as the very last line),
            # or if there is a header (the files sent to me had 3 lines of headers so I needed to skip those lines)
            if len(line) == 0 or j < 3 or j == len(lines) - 1:
                continue

            label = line[labelColumnIndex] # extract the label from the csv
            newLabel = label.lower() # make everything jn the label lowercase
            newLabel = newLabel.replace(' ', '') # remove all spaces from the label
            
            # handles one word (no dash) codes
            if newLabel in noDashCodes:

                # iterate over all of the codes
                for i, code in enumerate(codes):

                    # if the label equals a code, then add one to the counter for that code
                    if newLabel == code.lower():
                        results[i + 1] = str(int(results[i + 1]) + 1)
                        labelFound = True

            # otherwise, it is a code with a dash in it, and this else statement handles that case.
            # big picture: split the label (and the codes) into two parts: everything that comes before
            # the dash ("-") and everything that comes after the dash. If a label (the data on one line of a transcript csv)
            # and a code have the same values before and after the dash, then the label matches the code and we add one to the 
            # counter for that code.       
            else:
                newLabel = newLabel.split('-') # split the label into two parts (before the dash vs after the dash)
                
                # iterate over all of the codes with dashes in them. Since this is the case where the label has no dash
                # we can skip all of the codes that don't have dashes in them. This is what "if code in noDashCodes: continue" does
                for i, code in enumerate(codes):

                    # skips the codes without a dash in them
                    if code in noDashCodes:
                        continue

                    # do what we did to the label to the code (make it lowercase, remove spaces, and split into two parts)
                    newCode = code.lower()
                    newCode = newCode.replace(' ', '')
                    newCode = newCode.split('-')

                    # if the first part of the label matches the first part of the code and
                    # the second part of the label matches the second part of the code,
                    # then we have a match! If so, then add one to the counter that keeps track
                    # of how many times that code showed up in the transcript
                    if newLabel[0] in newCode[0] and newLabel[1] in newCode[1]:
                        results[i + 1] = str(int(results[i + 1]) + 1) # cast the counter to an integer, add one to it, then cast it back to a string
                        labelFound = True # signifies that we found a match and we don't need to add this label to the error files
                        break # since we found a match, we don't need to keep looking through codes to find a match. Stop the search here
            

            # if we don't find a match for the label after searching through all of the codes, then add this label to the error file
            if not labelFound:
                seperator = '-'
                errors.append([str(subjectID), seperator.join([label]), str(j + 1)])

        # return the labels we found a match for (results) and the labels we did not find a match for (errors)
        # in a format that we can use to write them to a csv file. Happy to explain more about how this formatting works! just ask!
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
    
    errorsList = [] # oython list for keeping track of the labels that didn't have a match

    # iterates over all of the subject files in the transcript folder
    for subjectFile in os.listdir(transcriptsFolderPath):
        # For each transcript, retrieve the data in the subject's csv file 
        # (the labels with matches [i.e. results] and the labels without matches [i.e. errors])
        results, errors = getResults(subjectFile, transcriptsFolderPath)

        # add the errors to the list of errors
        for error in errors:
            errorsList.append(error)

        # writes the results (the labels with matches) to the master file
        with open(masterFileSavePath, 'a', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(results)

    # writes any codes not in the codes list to the error file for human review
    with open(errorFileSavePath, 'a', newline = '') as f:
        writer = csv.writer(f)
        for error in errorsList:
            writer.writerow(error)


