from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.options import Options
waiting_time = int(input("If you Have a Slow Wifi i would recomend 10 seconds if you have a good to fast wifi just leave it "))
searchmusic = input("Enter Music Name\n")
browser = webdriver.Chrome()
browser.get("https://www.mp3juices.cc/")
for counter in range(1, waiting_time):
    print("Waiting for " + str(counter) + " just to make sure the website is already loaded\n")
    sleep(1)
search = browser.find_element_by_xpath("//*[@id='query']")
search.send_keys(searchmusic)
for counter in range(1, 10):
    print("Waiting for " + str(counter) + " just to make sure the website is already loaded\n")
    sleep(1)

enterbutton = browser.find_element_by_xpath("//*[@id='button']")
enterbutton.click()
for counter in range(1, waiting_time):
    print("Waiting for " + str(counter) + " just to make sure the website is already loaded\n")
    sleep(1)
downloadbutton = browser.find_element_by_xpath("//*[@id='1|NyVYXRD1Ans|VGhlIEdyZWF0ZXN0IFNob3dtYW4gQ2FzdCAtIFRoZSBHcmVhdGVzdCBTaG93IChPZmZpY2lhbCBBdWRpbykubXAz']")
downloadbutton.click()
for counter in range(1, waiting_time):
    print("Waiting for " + str(counter) + " just to make sure the website is already loaded\n")
    sleep(1)
download = browser.find_element_by_xpath("//*[@id='download_1']/div[3]/a[1]")   
download.click()