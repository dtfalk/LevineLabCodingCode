Contact Info: dtfalk@uchicago.edu and 1-413-884-2553 


Hello y'all over at the Levine lab!

This is a README for how to use the code in this github repository.

This README is broken down into the following sections:
1) How to download the code
2) Where to put the transcripts 
3) How to run the code
4) *optional* How to convert excel files (.xlsx) to CSV files (.csv)
5) what you might need to change
6) how to have a good time while you are doing 1-4 and troubleshooting tips


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
2) Download all of your transcripts. Make sure that the name of the transcripts is just the subject number. For example, if the subject number is "999999", then the file itself should be called "999999.csv". In your file finder/explorer it may just be listed as "999999", that is not a problem. Just make sure that its name, other than the file extension at the end, is just the subject number.
3) Move all of these transcripts into the "transcriptsFolder". When you click on the "transcriptsFolder" in your file finder/explorer you should see a list of files. Make sure you don't create a subfolder within "transcriptsFolder". "transcriptsFolder" should just contain the transcript CSV files.
==================================================================================


How to run the code
==================================================================================
1) Go to the following link: https://code.visualstudio.com/Download
2) Download the version of VS Code that matches your computer type/operating system
3) Once VS Code is downloaded, open the installer and choose the option to create a desktop icon. This creates an icon on your desktop so that you can double click the icon and it will open VS Code.
4) Open VS Code and navigate to the "extensions" tab. It should be one of the icons on the left side of your screen (it is on Windows, but it might be different on Mac). Then search for "Python" in the extensions tab. Download this extension. This downloads all of the necessary stuff to run Python code.
5) Restart VS Code (Quit and reopen it)
6) Navigate to the "File" tab and then select "Open Folder". Open the folder that has the code and the transcripts
7) Go to the "Terminal" tab and select "New Terminal". This should open a terminal on your screen. You should be able to type in the terminal. It should say something like "PS C:\Users\userName\OneDrive\Desktop\yourFolderName> ". Whatever you named your folder should be the last thing written on that line. That indicates that your computer will look in the correct place for your code when it tries to run your code.
8) type "python extractCodesAndSaveToMasterFile.py" into the terminal and press "Enter" or whatever you press on your computer to enter things.
9) Let the code run for a second
10) Open the overall folder with the code + transcriptsFolder in your file finder/explorer. You should see a "saveFolder".
11) This folder contains a file called "masterFile.csv" and "errorsFile.csv". The masterFile is the masterFile with the coded results. The errorsFile contains all of the codes that were not according to the coding scheme that you gave me (misspellings, etc...). The masterFile.csv should have the bulk of the coding done for y'all and the errorFile.csv is things that should be reviewed by a human. 
12) upload these CSVs into google drive or whatever your preferred CSV viewer is
==================================================================================


*optional* How to convert excel files (.xlsx) to CSV files (.csv)
==================================================================================
0) RECOMMENDED: The easiest option here is to save the files as csv files. This is available in google drive. All you need to do is to select the "save as" option and choose "save as CSV. Otherwise, the next steps are a bit involved yet will be necessary for the code to run as they need to be CSV files...
1) Create a folder within the folder that contains your "extractCodesAnd..." file and your "transcriptsFolder" called "transcriptsFolderExcel".
2) Download all of your excel transcripts and place them in the "transcriptsFolderExcel" folder. Ideally, these excel files will contain ONLY the list of codes. They should be in the first column of the excel files Avoid adding any headers or any trailing data such as a list of zeroes. Just one column with the list of labels/codes that you want coded into a master file. 
as a list of zeroes. All that should be in these files is one long column with the labels.
3) Now you need to download something called "anaconda" from https://www.anaconda.com/download/ . Clicking on this link should suggest the version to download that your computer supports. Download this and follow the installation steps. If there is an option for a desktop icon, then select it.
5) open "anaconda prompt". If that doesn't appear (it doesn't seem to on MAC devices), then open up "terminal".
6) You should see a command line/terminal prompt and something like "(base) C:/Users/yourUserName >" or something similar. The "base" means that you installed anaconda correctly. 
7) Once you are here type/enter: conda create --name "LevineLabCoding" and then "conda activate LevineLabCoding"
8) This creates an anaconda environment where you can download some additional packages so that the conversion code will run properly. The word "base" should have changed to "LevineLabCoding". 
9) Now type and enter "pip install pandas". Let this do its thing. 
10) Once you get the option to type again, type/enter "code". This should open up VS Code with your anaconda environment activated. 
11) If steps 5-10 don't work as expected, then search for/open "anaconda navigator". It should look like a big green circle. Once it has opened, click on the "preferences" option. It should be under the "file" tab. Scroll down until you see the "VS Code path" text entry option.
12) Now open your file explorer/finder. Find VS Code. You need to copy its "path". If you don't know how to do this, you can google something like "how to copy an application as a path on a _____ device" (enter mac, windows, linux, or whatever operating system you use instead of the _____). Copy the path and then paste it into the "vs code path" option on anaconda navigator. Save this change and restart anaconda naviagtor.
13) Once you reopen anaconda navigator, select the "envirnoments" tab and create a new environment and call it "LevineLabCoding". Let it finish creating this environment and then click on the "home" tab and click the "launch" button under the VS Code icon.
14) This should open vs code. Open a terminal and type "pip install pandas" and let that finish.
15) If you choose the anaconda navigator route, then every time you try to run the conversion code you have to open anaconda navigator, open the "environments" tab, select the "LevineLabCoding" environment, and then press launch underneath the vs code icon. If you choose the terminal/anaconda prompt route, then every time you run the conversion code you will need to open the terminal/prompt, type "conda activate LevineLabCoding" and then type "code" so that the environment will be activated when you run your code. 
16) Once you have vs code open with the anaconda evironment activated, open your folder with the excel transcripts/code in VS Code as described in the previous section.
17) type/enter "python convertExcelToCSV.py" into the terminal and let the conversion code run. You should now see a "transcriptsFolder" and if you open it, then it will be populated with csv versions of your files.
18) Now you can run "extractCodesAndSaveToMasterFile.py" according to the instructions in the previous section
19) I seriously recommend you just download the files as CSVs to begin with and save yourself the trouble of this section. My instructions are not perfect and there's plenty of annoying computer things that can happen and make this part fail. But if you want to know more about coding in python, then knowing the basics of setting up and using an anaconda environment is invaluable.
==================================================================================


What you might need/want to change
==================================================================================
If you're feeling adventurous, then you can open the "extractCodesAndSaveToMasterFile.py" file and make some modifications to your liking. The first section of code contains some variables that you may want to change. The list of variables you can change are below:

1) "transcriptsFolderName": This is the name of the folder where your transcripts are stored. If you want to call the folder something other than "transcriptsFolder", then change this variable to whatever you decide to name the folder in which you store the transcript CSVs.
2) "saveFolderName": Change this to whatever you want the name of the folder that contains the output files to be. If you change it to another name, then you will find the "masterFile.csv" and "errorFile.csv" stored within a folder with that name.
3) "masterFileName" and "errorFileName": If you want your output files to have different names, then change these variables. 
4) "relationalMathCodes", "relationalNonMathCodes", etc...: If you want to add or remove codes to your analysis, then add them to these lists according to the format you see in the code. Make sure to add a dash ("-") assuming it is a two part code (e.g. 'NM-Label"). If it is a code without a dash, then add it to the "noDashCodes" list without any capital letters or spaces.
==================================================================================


How to have a good time while you are doing 1-4 and troubleshooting tips
==================================================================================
Do something fun to relax and reach out to me at dtfalk@uchicago.edu, dtfbaseball@gmail.com or at 413-884-2553. Either one is fine for me, but if you choose to text/call me, then please identify yourself so I know that you are not spam.
==================================================================================

