# import chrome webdriver
from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

# Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# Enter login info:
# Logging in is necessary so that you can see the full descriptions of everything
print("Please ensure that 2-Factor Authentication of your LinkedIn account is turned OFF")
elementID = browser.find_element_by_id('username')
username = input("Enter your LinkedIn username: ")
elementID.send_keys(username)
elementID = browser.find_element_by_id('password')
password = input("Enter your LinkedIn password: ")
elementID.send_keys(password)
elementID.submit()

# list of links to job postings
# TODO: create a function to pull these links automatically
links = ["https://www.linkedin.com/jobs/view/2271522921/?refId=5ab7b47e-3106-4af7-bd73-af408d413cc2&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/1964667931/?refId=259d2759-6a27-4496-87ba-213236b13768&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2287499320/?refId=51b12b18-3ff7-4c88-974b-83feaa080a29&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2317721846/?refId=a3ae45fe-42fb-467a-ae85-9678252e1117&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2323977495/?refId=a3ae45fe-42fb-467a-ae85-9678252e1117",
"https://www.linkedin.com/jobs/view/2328358119/?refId=a3ae45fe-42fb-467a-ae85-9678252e1117&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2352913360/?refId=a3ae45fe-42fb-467a-ae85-9678252e1117&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2352268686/?refId=07c6cca2-641f-40cd-b0b5-8244c3049a46&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2334355295/?refId=07c6cca2-641f-40cd-b0b5-8244c3049a46&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2371215234/?refId=c6e1f690-1741-4aae-98af-5bab8f918293&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2340838013/?refId=c6e1f690-1741-4aae-98af-5bab8f918293&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2369012266/?refId=08a60692-2222-4b2a-a32a-9f52ef0c9929&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2300196183/?refId=08a60692-2222-4b2a-a32a-9f52ef0c9929&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2349751747/?refId=edeb276f-ac30-4c9e-9602-aa04e7eab0a0&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2308222335/?refId=edeb276f-ac30-4c9e-9602-aa04e7eab0a0&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2325349899/?refId=6bf3a41e-f154-4103-8a5d-b04db443f4ed&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2349082805/?refId=4dbacf60-ab04-436f-9180-f94169bea3a2&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2372479887/?refId=4dbacf60-ab04-436f-9180-f94169bea3a2&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2286329822/?refId=49b3b4b9-b545-4704-8341-c2ee7117ede1&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2354686203/?refId=49b3b4b9-b545-4704-8341-c2ee7117ede1&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2291182222/?refId=49b3b4b9-b545-4704-8341-c2ee7117ede1&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2357260171/?refId=8dddeb66-4d62-4692-8ab6-4f6ce19e305b&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2334139577/?refId=2c739a7f-951e-4c2a-965f-a7762ab39b31&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2346392135/?refId=2ffdd501-915c-4b9b-9cc2-3d07673ab410&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2001282532/?refId=2ffdd501-915c-4b9b-9cc2-3d07673ab410&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2357355530/?refId=2523f0c5-784a-449b-87ff-17d98e884620&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2369327981/?refId=2523f0c5-784a-449b-87ff-17d98e884620&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2259666441/?refId=2523f0c5-784a-449b-87ff-17d98e884620&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2368911534/?refId=58a79696-a49b-404a-89c7-a999818ac188&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2234234533/?refId=58a79696-a49b-404a-89c7-a999818ac188&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2388371055/?refId=58a79696-a49b-404a-89c7-a999818ac188&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/1954682398/?refId=58a79696-a49b-404a-89c7-a999818ac188&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2334354636/?refId=0a86cb00-4503-404c-a454-12cfa23c31ea",
"https://www.linkedin.com/jobs/view/2252341133/?refId=0a86cb00-4503-404c-a454-12cfa23c31ea&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2335422481/?refId=6c1e1f8e-6389-40f2-a3b2-e44be620b950&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2381347564/?refId=00d165dd-aa86-4953-b55f-38ea05016943&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2334182768/?refId=00d165dd-aa86-4953-b55f-38ea05016943&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2393313632/?refId=00d165dd-aa86-4953-b55f-38ea05016943&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2349921290/?refId=00d165dd-aa86-4953-b55f-38ea05016943&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2377838275/?refId=00d165dd-aa86-4953-b55f-38ea05016943&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2390379761/?refId=00d165dd-aa86-4953-b55f-38ea05016943&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2425355193/?refId=8cb24fe2-188a-473a-959e-82fac362bb67&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2427168385/?refId=c0be074e-4a98-49b9-89e2-a9c21ce0eb69&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2427921475/?refId=c0be074e-4a98-49b9-89e2-a9c21ce0eb69&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2434904585/?refId=c0be074e-4a98-49b9-89e2-a9c21ce0eb69&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2346174315/?refId=c0be074e-4a98-49b9-89e2-a9c21ce0eb69&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2401116064/?refId=b312926a-5879-4ac7-9bcb-6ff36a085e66&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2403723968/?refId=b312926a-5879-4ac7-9bcb-6ff36a085e66&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2426494539/?refId=829702cb-cefb-48f1-9c14-ad1d357a48a7&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2373963262/?refId=829702cb-cefb-48f1-9c14-ad1d357a48a7&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2268827173/?refId=829702cb-cefb-48f1-9c14-ad1d357a48a7&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2430402905/?refId=829702cb-cefb-48f1-9c14-ad1d357a48a7&trk=flagship3_job_home_savedjobs",
"https://www.linkedin.com/jobs/view/2402754151/?refId=829702cb-cefb-48f1-9c14-ad1d357a48a7"]
desc = []       # list will contain all job descriptions

# go to each job link and get its job description, append to desc
for l in links:
    browser.get(l)      # go to link
    # click "see more" button on description
    see_more = browser.find_element_by_class_name("artdeco-card__actions")
    see_more.click()
    desc.append(browser.find_element_by_id("job-details").text)     # append text from job description to list of job descpritons

# add all job descriptions to text file
allJobDesc = open(r'Job Descriptions.txt','w')
for i in desc:
    allJobDesc.write(i + '\n')
allJobDesc.close()
