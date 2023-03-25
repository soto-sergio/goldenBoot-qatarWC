import pandas as pd
import lib.scraper

# Website to scrape
url = "https://www.worldfootball.net/goalgetter/wm-2022-in-katar/"        
# Table index from Website
i = 1 
# Path to save file. Include name of file + .csv extension                                                                  
path =  "C:/Users/Checo/Desktop/projectum/learning_projects/worldcup_qatar/data/raw/qatar_wc_scorers.csv"                                                                 

df = lib.scraper.df_from_website(url,i)                                   # Calls functions to create df
lib.scraper.save_csv(df,path)                                             # Calls function to save file
