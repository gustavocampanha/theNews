from selenium import webdriver
import pyautogui as auto
from time import sleep

  mail_check = 
  mails = list()
  mails.append('joaocarlos00010101010101010')
  mails.append('senha123.')
  navegador = webdriver.Chrome()
  navegador.get('https://account.proton.me/signup?plan=free&billing=12&currency=EUR&language=en')
  sleep(2)
  auto.typewrite(mails[0])
  sleep(2)
  auto.hotkey('tab')
  auto.hotkey('tab')
  sleep(2)
  auto.typewrite(mails[1])
  sleep(2)
  auto.hotkey('tab')
  auto.typewrite(mails[1])
  auto.hotkey('tab')
  auto.hotkey('enter')
  sleep(6)
  auto.hotkey('tab')
  auto.hotkey('tab')
  auto.hotkey('tab')
  auto.hotkey('enter')
