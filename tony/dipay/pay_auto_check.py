#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function
import os, sys
import time
import ast
import json
import Queue
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def main(*args):
  print("start test chrom.")
  target_url = None
  #doman_url = None
  #file_name = None
  try :
    target_url = str(sys.argv[1])
  except :
    print("url=", target_url)
    return

  #try :
  #  file_name = str(sys.argv[2])
  #except :
  #  print("file=", file_name)
  #  return
  
    
  fp = os.path.join(BASE_DIR, "chromedriver")
  caps = DesiredCapabilities.CHROME
  caps['loggingPrefs'] = {'performance': 'ALL'}

  self_options = webdriver.ChromeOptions()
  self_options.add_argument('-log-level=3')
  self_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  
  
  chrome_options = Options()
  chrome_options.add_experimental_option('w3c', False)
  chrome_options.add_argument('-log-level=3')
  chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
  #chrome_options.addArguments("ignore-certificate-errors");

  driver = webdriver.Chrome(executable_path="chromedriver", desired_capabilities=caps, options=chrome_options)
  #driver = webdriver.Chrome(executable_path=fp, desired_capabilities=caps, options=chrome_options)
  print(driver)
  url = target_url

  print(url)

  que = Queue.Queue()

  #wait = ui.WebDriverWait(driver,10)
  #wait.until(lambda driver: driver.find_element_by_方法("定位路径自己来"))
  driver.get(url)
  #time.sleep(5)
  #que.get(timeout=5)
  try:
    que.get(timeout=5)
  except Queue.Empty:
    pass


  # -- is login -- #
  context = driver.find_element_by_css_selector('#pd-form-username')
  context.send_keys("admin")
  #que.get(timeout=0.5)
  try:
    que.get(timeout=0.5)
  except Queue.Empty:
    pass

  context = driver.find_element_by_css_selector('#pd-form-password')
  context.send_keys("123456")
  try:
    que.get(timeout=0.5)
  except Queue.Empty:
    pass

  sign_link = driver.find_element_by_link_text('Sign in')
  sign_link.click()
  
  try:
    que.get(timeout=7)
  except Queue.Empty:
    pass



  #url = url + "/admin/task/task.html"
  #driver.get(url)

  # -- pays -- #
  sign_link = driver.find_element_by_link_text(u'订单管理')
  sign_link.click()
  try:
    que.get(timeout=0.5)
  except Queue.Empty:
    pass

  sign_link = driver.find_element_by_link_text(u'任务列表')
  sign_link.click()
  try:
    que.get(timeout=3)
  except Queue.Empty:
    pass

  #driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@src='/admin/dashboard.html?addtabs=1']"));
  #time.sleep(3)

  #driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@src='/admin/task/task.html?addtabs=1']"));
  #time.sleep(7)
  #que = Queue.Queue()
  #loop_delay = 3 

  while True:
    ## -- Refresh -- #
    #print("Refresh.")
    #driver.refresh()
    #time.sleep(3)
    print("loop. run")
    while True:
      try:
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@src='/admin/task/task.html?addtabs=1']"));
        print("have iframe")
        break

      except:
        pass
        print("no iframe")
    #que.get(timeout=7)
    try:
      que.get(timeout=0.5)
    except Queue.Empty:
      pass
   

    try:
      ok_link = driver.find_element_by_link_text(u'确认')
      ok_link.click()
      try:
        que.get(timeout=0.5)
      except Queue.Empty:
        pass
      print("ok.")

      check_link = driver.find_element_by_link_text(u'确定')
      check_link.click()
      try:
        que.get(timeout=0.5)
      except Queue.Empty:
        pass
      print("check.")
    except:
      print("---no have.")

      try:
        que.get(timeout=5)
      except Queue.Empty:
        pass


    driver.refresh()
    try:
      que.get(timeout=7)
    except Queue.Empty:
      pass




  que = Queue.Queue()
  for i in xrange(300):
  #for i in xrange(8):
    print("loop", i)
    try:
      que.get(timeout=1)
    except Queue.Empty:
      pass

  net_log = driver.get_log('performance')
  print ( "driver = ", len(net_log) )




  driver.close()

  
if __name__ == "__main__":
    print ("hello word")
    main()


