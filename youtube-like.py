from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from openpyxl import load_workbook
# import time

# choosing the browser to use
driver = webdriver.Firefox()

# my target website
driver.get("https://www.youtube.com/")

# the login process
login = driver.find_element(By.CLASS_NAME, "yt-spec-touch-feedback-shape__fill").click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "identifierId")))
userName = driver.find_element(By.ID, "identifierId")
userName.submit()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "whsOnd zHQkBf")))
userPassword = driver.find_element(By.CLASS_NAME, "whsOnd zHQkBf")
userPassword.submit()

# wait for 2fa
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "search")))

driver.find_element(By.CLASS_NAME, "yt-spec-icon-shape").click()
driver.find_element(By.CLASS_NAME, "title style-scope ytd-guide-entry-renderer").click()


# for loop iterating through column A. start at 2(first value not header), 0 fails 
for i in range(2, len(sheet["a"])):
    searchBar = driver.find_element(By.ID, "q") # find search bar
    searchBar.send_keys(sheet["a" + str(i)].value) # enter cell content as a string
    searchBar.submit()
    time.sleep(10) # for loop works faster than selenium, so sleep while it works
    try: # find the duplicate box, if there is one (throws error)
        # WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "ui-id-1")))
        error.find_element(By.CLASS_NAME, "borderbox-title")
        print("found error", i) # for me visually
        sheet["g"+str(i)] = "Possible duplicate!" # write to column G
    except: # if NOT found, let me know, go to home (search bar is not same object, searchBar fails)
        driver.get("https://norcal.neoserra.com/")
        print("can't find box", i)
        sheet["g"+str(i)] = "No duplicate!" # write to column G
        if i%2:
            workbook.save("ebNumbs.xlsx")
        # pass
    time.sleep(5) # for loop works faster than selenium, so sleep while it works
workbook.save("ebNumbs.xlsx")
