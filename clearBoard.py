# EHughes
# 1/16/2025
# Clear all unread discussion posts in MyCourses
# Requires user to login in to their MyCourses account
# and supply the urls to the desired discussion boards

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# start webdriver (opens Chrome in new window)

print("Enter all the discussion board urls to clear separated by a comma")

# clean input and save as a list
url_to_clear = str(input("URLs: ")).replace(" ", "").split(",")
driver = webdriver.Chrome()

links_to_visit = []

for url_index in range(0, len(url_to_clear)):
    url = url_to_clear[url_index]
    driver.get(url)

    # wait until the web page has loaded and user has logged in on the first url visit
    wait = WebDriverWait(driver, timeout=300)
    wait.until(EC.url_matches(url))

    # find web links
    link = driver.find_elements(By.TAG_NAME, "a")

    # search each link for "discussions/threads"
    # add all links with that to a list to be visited

    for i in link:
        if (
            i.get_attribute("href") != None
            and i.get_attribute("href").find("discussions/threads") != -1
        ):
            links_to_visit.append(i.get_attribute("href"))

# visit all the discussion links
for i in links_to_visit:
    driver.get(i)
