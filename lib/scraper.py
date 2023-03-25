import os 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains


# i is the index of the table
def df_from_website(url: str, i: int):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    df = pd.DataFrame(pd.read_html(driver.page_source)[i]) 
    return df

# Import path for where to save location
def save_csv(df, path_name: str):
    df.to_csv(path_name , index=False)
    return print('Done')

    
    