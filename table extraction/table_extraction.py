import pandas as pd
# to extract the tables from a website 
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
for i in simpsons:
    print(i)