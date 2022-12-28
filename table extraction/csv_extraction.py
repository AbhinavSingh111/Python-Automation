# scrapping csv files from a website using pandas
import pandas as pd
# reading 1 csv file from the website
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
# renamning columns
df_premier21.rename(columns={'FTHG':'HOME_GOALS_NAME','FTAG':'AWAY_GOALS'},inplace=True)
print(df_premier21)