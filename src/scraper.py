import os 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.topendsports.com/events/worldcupsoccer/goal-scorers.htm")

df = pd.DataFrame(pd.read_html(driver.page_source)[0]) 

df.to_csv('C:/Users/Checo/Desktop/projectum/learning_projects/worldcup_qatar/data/raw/scorers_per_world_cup.csv', index=False)