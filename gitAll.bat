git status
git add .
IF EXIST "%1" 
(
    git commit -m %1
)
ELSE 
(
    git commit -m"random commit"
)
git push origin master