### END-TO-END BASH SCRIPT TO CREATE A NEW LOCAL AND REMOTE REPO THROUGH PYTHON


#### Configuration
1. https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_win32.zip
2. pip install selenium
3. add python to environment variables (where python//which python)
4. add .bat , .sh and .py files in a folder already listed in environment variables


#### How to use
> FROM CMD : gitNew [reponame] [privacy (defaults to False)]
> FROM GIT : gitAll.sh OR gitAll (after the proper alias have been set)


### BONUS
1. Set env variables under "envVars" ; Configure Notepad, Sublime as text editors
2. Set alias for GitBash


#### Add Notepad, Sublime under an environment variables path
ONE_OFF  : setx envVars "C:\Program Files\Notepad++;C:\Program Files\Sublime Text 3"
ADDITION : setx envVars "%envVars%;C:\Users\takis\AppData\Local\atom"
CHECK    : echo %envVars%


#### Set alias for the GitBash
1. open/create a .bashrc in the directory of GitBash (where GitBash opens by default)
2. in the .bashrc file add the following
* alias npp='notepad++'
* alias sub='sublime_text'
* alias gitNew='gitNew.sh'
* alias gitAll='gitAll.sh'
* alias gitLoc='gitLoc.sh'
3. once set either reponen GitBash or source .bashrc

