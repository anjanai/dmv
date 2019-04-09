import datetime
from selenium import webdriver

now = datetime.datetime.now().strftime("%A %m-%d %H:%M")
hour = int(now.split()[-1].split(':')[0])
if hour > 17 or hour < 8:
    exit (0)

day = now.split()[0]
if day == 'Sunday':
    exit(0)

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="c:/users/anjana/tools/chromedriver.exe", chrome_options=options)
driver.get("https://www.dmv.ca.gov/portal/dmv/detail/fo/offices/fieldoffice?number=632")


d = driver.find_element_by_id("WaitTimesData").text
*rest, last = d.split()
driver.quit()


with open("dmv-waits.txt", "a") as myfile:
    myfile.write (f'{now}\t{last}\n')




