import os
import pandas as pd

if __name__ == '__main__':
    curDir = os.path.dirname(__file__)
    loadFolder = os.path.join(curDir, 'transcriptsFolderExcel')
    saveFolder = os.path.join(curDir, 'transcriptsFolder')

    excelFiles = os.listdir(loadFolder)
    print(len(excelFiles))
    for excelFile in excelFiles:
        loadPath = os.path.join(loadFolder, excelFile)
        savePath = os.path.join(saveFolder, excelFile.replace('.xlsx', '.csv'))
        df = pd.read_excel(loadPath)
        df.to_csv(savePath, index = False)
