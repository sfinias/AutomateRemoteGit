
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PRIVACY = None

if len(sys.argv) > 2:
    REPONAME = sys.argv[2]

    if len(sys.argv) == 4:
        PRIVACY = sys.argv[3]

    driver = webdriver.Chrome("xxx/chromedriver.exe")
    driver.get("https://github.com/login")

    mail = driver.find_element_by_name("login")
    mail.send_keys("xxx")

    password = driver.find_element_by_name("password")
    password.send_keys("xxx")

    password.send_keys(Keys.RETURN)

    driver.get("https://github.com/new")

    name_field = driver.find_element_by_name("repository[name]")
    name_field.send_keys(REPONAME)


    if PRIVACY == "True":
        private_button = driver.find_element_by_id("repository_visibility_private")
        private_button.click()

    submit = driver.find_element_by_class_name("first-in-line")
    submit.submit()
    # driver.quit()

    CURRENT_PATH = sys.argv[1]

    myCmd = r'cd {}' \
            r'&&git init&&' \
            r'git status&&' \
            r'git add .&&' \
            r'git commit -m"casual commit"&&' \
            r'git remote add origin https://github.com/Takfes/{}.git&&' \
            r'git push -u origin master'.format(CURRENT_PATH,REPONAME)

    os.system(myCmd)


else:
    print("The correct input is <filename> <whereami> <reponame> <isPrivate(default:false)>")
