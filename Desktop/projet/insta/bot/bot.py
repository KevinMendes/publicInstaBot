import contextlib
import itertools
import datetime
import time
from multiprocessing.connection import wait
from pyclbr import Function
import uuid
from numpy import diff
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pathlib
from bot.utils.until import untilClickableXPATH, untilSelectableXPATH, untilVisibleXPATH, untilClickableCSS
from bot.utils.find import findByXPATH, findByCSS

cDate = datetime.datetime.now()
currentDate = cDate.strftime("%d/%m/%Y")
class Bot():
      
  def __init__(self, login: str, password: str) -> None:
    options = webdriver.FirefoxOptions()    
    options.capabilities["marionette"] = False
    cPath = pathlib.Path().resolve()
    options.add_argument('--disable-gpu')
    #options.add_argument('--headless')
    self.login = login
    self.password = password
    self.driver = webdriver.Firefox(options=options, executable_path=fr"{cPath}\bot\geckodriver.exe")
    self.countOfFollow = 0
    self.messageCount = 0
    
  def teardown_method(self):
    self.driver.quit()
  
  def Connexion(self):
    self.driver.get("https://www.instagram.com/")
    self.driver.set_window_size(1346, 708)
    # 3 | waitForElementVisible | xpath=//form[@id='loginForm']/div/div/div/label/input | 10
    # Attente de l'affichage des éléments de connexions
    untilClickableXPATH(self.driver,  "/html/body/div[4]/div/div/button[2]", 10).click() #close modal
    untilClickableCSS(self.driver, "div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1)", 10)
    untilClickableXPATH(self.driver, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input", 10).send_keys(self.login)
    findByXPATH(self.driver, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(self.password)
    untilClickableXPATH(self.driver, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input", 10).send_keys(Keys.ENTER)
    print("connected")

  def doThing(self, listOfHashtag: list, passedPub: list, passedPubUpdate: Function) -> None:
    with contextlib.suppress(Exception):
      untilClickableXPATH(self.driver, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]", 10).click() #close modal

    untilClickableXPATH(self.driver, "/html/body/div[1]/section/main/div/div/div/section/div/button", 20).click() #id check
    
    with contextlib.suppress(Exception):
      untilClickableXPATH(self.driver, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]", 10).click() #close modal

    
    for tag in listOfHashtag: 
      break;
      #untilClickableCSS(self.driver, "._aawh", 10)
      hashtagSearchZone = untilClickableXPATH(self.driver, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input")
      hashtagSearchZone.clear()
      hashtagSearchZone.send_keys(f"#{tag}")
      print(tag)
      try:
        untilClickableXPATH(self.driver, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div", 10).click()
        untilVisibleXPATH(self.driver, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/header/div[2]/div/div[1]", 10)
      except Exception:
        continue;

      listOfPost = []
      
      for i, j in itertools.product(range(1, 4), range(1, 4)):
        link = untilClickableXPATH(
              self.driver,
              f"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[{i}]/div[{j}]/a", 8
          ).get_attribute("href")
        listOfPost.append(link)
      print(listOfPost)

      #check if link is in passedPub.csv
      listOfOwner = []
      for pub in passedPub:
          listOfOwner.append(pub[3])
          if pub[0] in listOfPost:
            listOfPost.remove(pub[0])

      #waiter for instabotcontroller
      for link in listOfPost:
        self.driver.get(link)
        like = untilClickableXPATH(self.driver, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button', 10) #like icon
        like

        try:
          findByXPATH(self.driver, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div/div/span[2]/a')
          continue;
        except Exception:
          print("Pas une publication en duo")
        untilClickableXPATH(self.driver, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/a')
        owner = findByXPATH(self.driver, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/a').text
        if owner in listOfOwner:
          print(f"{owner} already liked")
          continue;

        try:
          findByXPATH(self.driver, '//*[@id="mount_0_0_qT"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div[2]/span')
          continue;
        except Exception:
          print('Not official - continue action')

        like.click() #like
        try:
          untilClickableCSS(self.driver, 'button._acan:nth-child(2)', 10).click() #click s'abonner
        except Exception:
          continue;

        if self.messageCount <= 14:
          try:
            untilClickableXPATH(self.driver, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys('WOW!!! 😏')
            untilClickableCSS(self.driver, 'button._acan:nth-child(3)').click()
            self.messageCount += 1
          except Exception:
            print("Impossible d'envoyer un message")
        
        url = link
        tag = tag
        DatePassage = currentDate


        passedPubUpdate([url, tag, DatePassage, owner, "Non", uuid.uuid4()])
        self.countOfFollow+=1
        if self.countOfFollow==100: #100 pour pas de soucis
          print("ended")
          break;
        time.sleep(60)
  

  def unSub(self, passedPub: list, modifyPassedPub: Function):
    cDlist = currentDate.split("/")
    cD = datetime.datetime(int(cDlist[2]), int(cDlist[1]), int(cDlist[0])) #currentDay

    passedPub
    unsub = 0
    for pub in passedPub:
      if pub[2] == 'DatePassage': #ignore first line of file
        continue;
      pDlist = pub[2].split("/")
      pD = datetime.datetime(int(pDlist[2]), int(pDlist[1]), int(pDlist[0])) #passedDay
      diffDay = int((cD - pD).days)
      if diffDay >= 4 and pub[4] == "Non":
        name = pub[3]
        self.driver.get(f'https://www.instagram.com/{name}/?hl=fr')
        untilClickableXPATH(self.driver, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button', 10).click()
        #use javascript selector in selenium
        time.sleep(2)
        untilClickableXPATH(self.driver, "//*[text()='Se désabonner']").click()
        
        modifyPassedPub(pub[5])
        print("unsub", pub[3])
        time.sleep(15)
        self.driver.switch_to.window(self.driver.window_handles[0]) #delete?
        print(f"{pub[3]} is not followed anymore")
        unsub+=1
      elif diffDay < 4:
        print("fin")
        break; 
      elif unsub ==200:
        print("ended by number of unsub")
        break;
#TODO2 : si le désabo marche pas, tenter enter - tab - enter sur la pop up
