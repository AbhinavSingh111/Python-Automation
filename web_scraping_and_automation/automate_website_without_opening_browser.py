# headless mode

# first create a driver.
# A driver allows us to interact with the website using selenium

# now the default behaviour of selenium is to open a chrome browser and then do the task 
# but with few tweaks we can do it without opening the browser
# here we are doing by without  opening the browser 
#  in order to do that we have to to import options from selenium

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# for selenium 4 and above
from selenium.webdriver.chrome.service import Service
import pandas as pd
website = 'https://www.thesun.co.uk/sport/football/'
# path of chrome driver
path = "D:\Python Automation\web_scraping_and_automation\chromedriver"

#headless-mode
options = Options()
options.headless = True


# define driver
# for selenium 4 and above
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)
driver.get(website)
# driver.find_element will find only the first matching element
containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

titles=[]
subtitles = []
links = []

# find only titles
for container in containers:
   title =  container.find_element(by="xpath",value='./a/h3').text
   titles.append(title)
   subtitle = container.find_element(by="xpath",value='./a/p').text
   subtitles.append(subtitle)
   link = container.find_element(by="xpath",value='./a').get_attribute("href")
   links.append(link)

# makeing dataframe to export the lists to csv
my_dict={'title':titles,'subtitle':subtitles,'link':links}
df_headlines = pd.DataFrame(my_dict)

df_headlines.to_csv('headless_headlines.csv')
driver.quit()




