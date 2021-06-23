# import chrome webdriver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

# open bookmarks file
with open("bookmarks.html") as page:
    soup = BeautifulSoup(page, 'html.parser')

# pull all linkedin links from bookmarks
links = []
for i in soup.find_all('a'):
    link = i.get('href')        # gets each link in the file
    if "linkedin" in link:      # filters out job links not going to linkedin
        links.append(link)

# Prompt user for login info
# Logging in is necessary so that you can see the full descriptions of everything
print("Please ensure that 2-Factor Authentication of your LinkedIn account is turned OFF")
username = input("Enter your LinkedIn email/phone: ")
password = input("Enter your LinkedIn password: ")

# Open login page
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# Enter login info
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

desc = []       # list will contain all job descriptions

# go to each job link and get its job description, append to desc
for l in links:
    browser.get(l)      # go to link
    try:
        # click "see more" button on description
        see_more = browser.find_element_by_class_name("artdeco-card__actions")
        see_more.click()
        desc.append(browser.find_element_by_id("job-details").text)     # append text from job description to list of job descpritons
    except NoSuchElementException:
        # Reaches a "Something went wrong" page
        print(l, " no longer exists")
        continue

# add all job descriptions to text file
allJobDesc = open(r'Job Descriptions.txt','w')
for i in desc:
    allJobDesc.write(i + '\n')
allJobDesc.close()
