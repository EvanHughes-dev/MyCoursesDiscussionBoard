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

# remove any spaces in the url and separate along the comma
# into a list. Most urls don't have commas, but they can contain them
url_to_clear = str(input("URLs: ")).replace(" ", "").split(",")
driver = webdriver.Chrome()

links_to_visit = []

for url_index in range(0, len(url_to_clear)):
    url = url_to_clear[url_index]
    driver.get(url)

    # wait until the web page has loaded and user has logged in on the first url visit
    wait = WebDriverWait(driver, timeout=300)
    wait.until(EC.url_matches(url))

    # the first time a link is executed, the user will be prompted to login to their account
    # Once the user has logged in, the url will match the provided url, but none of the
    # elements on the page will be loaded, causing driver.find_element to return an empty list
    # to get around this, on the first loop reload the url. This forces the program to wait
    # until the page has fully loaded

    if url_index == 0:
        driver.get(url)
    # find web links
    link = driver.find_elements(By.TAG_NAME, "a")

    # search each link for "discussions/threads"
    # add all links with that to a list to be visited

    for thread in link:
        if (
            thread.get_attribute("href") != None
            and thread.get_attribute("href").find("discussions/threads") != -1
        ):
            links_to_visit.append(thread.get_attribute("href"))

# visit all the discussion links
# since the user is logged in, this clears it for their account

for thread in links_to_visit:
    driver.get(thread)
