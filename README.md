Contact Info: dtfalk@uchicago.edu and 1-413-884-2553 


Hello y'all over at the Levine lab!

This is a README for how to use the code in this github repository.

This README is broken down into the following sections:
1) How to download the code
2) Where to put the transcripts
3) How to run the code
4) what you might need to change
5) how to have a good time while you are doing 1-4 and troubleshooting tips


How to download the code
==================================================================================
1) Go to the following link: https://github.com/dtfalk/LevineLabCodingCode
2) Click on the bright green "Code" button on the right side of the screen 
3) Click "Download ZIP" to download the code as a zip file
4) Find the code you downloaded (it should be called something like "LevineLabCodingCode-master.zip")
5) Open it and then open the "LevineLabCodingCode-master" folder
6) Drag the "extractCodesandSaveToMasterFile.py" to your desktop
7) Create a folder on your desktop to store the code in. Call it whatever you'd like. Just make it memorable so you can find it again
8) Move the "extractCodesandSaveToMasterFile.py" file from your desktop to the the folder you created in step 7
==================================================================================



Where to put the transcripts
==================================================================================
1) Within the folder you just created on your desktop, create a new folder and call it "transcriptsFolder"
2) Download all of your transcripts. Make sure that the name of the transcripts is just the subject number. For example, if the subject number is "999999", then the file itself should be called "999999.csv". In your file explorer it may just be listed as "999999", that is not a problem. Just make sure that its name, other than the file extension at the end, is just the subject number.
3) Move all of these transcripts into the "transcriptsFolder". When you click on the "transcriptsFolder" in your file explorer you should see a list of files. Make sure you don't create a subfolder within "transcriptsFolder". "transcriptsFolder" should just contain the transcript CSV files.
==================================================================================


How to run the code
==================================================================================
1) Go to the following link: https://code.visualstudio.com/Download
2) Download the version of VS Code that matches your computer type/operating system
3) Once VS Code is downloaded, open the installer and choose the option to create a desktop icon. This creates an icon on your desktop so that you can double click the icon and it will open VS Code.
4) Open VS Code and navigate to the "extensions" tab. It should be one of the icons on the left side of your screen (it is on Windows, but it might be different on Mac). Then search for "Python" in the extensions tab. This downloads all of the necessary stuff to run Python code.
5) Restart VS Code (Quit and reopen it)
6) Navigate to the "File" tab and then select "Open Folder". Open the folder that has the code and the transcripts
7) Go to the "Terminal" tab and select "New Terminal". This should open a terminal on your screen. You should be able to type in the terminal. It should say something like "PS C:\Users\userName\OneDrive\Desktop\yourFolderName> ". Whatever you named your folder should be the last thing written on that line. That indicates that your computer will look in the correct place for your code when it tries to run your code.
8) type "python extractCodesAndSaveToMasterFile.py" into the terminal and press "Enter" or whatever you press on your computer to enter things.
9) Let the code run for a second
10) Open the overall folder with the code + transcriptsFolder in your file explorer. You should see a "saveFolder".
11) This folder contains a file called "masterFile.csv" and "errorsFile.csv". The masterFile is the masterFile with the coded results. The errorsFile contains all of the codes that were not according to the coding scheme that you gave me (misspellings, etc...). The masterFile.csv should have the bulk of the coding done for y'all and the errorFile.csv is thigns that should be reviewed by a human. 
12) upload these CSVs into google drive or whatever your preferred CSV viewer is
==================================================================================


What you might need to change
==================================================================================
If you're feeling adventurous, then you can open the "extractCodesAndSaveToMasterFile.py" file and make some modifications to your liking. The first section of code contains some variables that you may want to change. The list of variables you can change are below:

1) "transcriptsFolderName": This is the name of the folder where your transcripts are stored. If you want to call the folder something other than "transcriptsFolder", then change this variable to whatever you decide to name the folder in which you store the transcript CSVs.
2) "saveFolderName": Change this to whatever you want the name of the folder that contains the output files to be. If you change it to another name, then you will find the "masterFile.csv" and "errorFile.csv" stored within a folder with that name.
3) "masterFileName" and "errorFileName": If you want your output files to have different names, then change these variables. 
4) "relationalMathCodes", "relationalNonMathCodes", etc...: If you want to add or remove codes to your analysis, then add them to these lists according to the format you see in the code. Make sure to add a dash ("-") assuming it is a two part code (e.g. 'NM-Label"). If it is a code without a dash, then add it to the "noDashCodes" list without any capital letters or spaces.
==================================================================================

how to have a good time while you are doing 1-4 and troubleshooting tips
==================================================================================
Do something fun to relax and reach out to me at dtfalk@uchicago.edu or at 413-884-2553. Either one is fine for me, but if you choose to text me, then please identify yourself so I know that you are not spam.
==================================================================================

