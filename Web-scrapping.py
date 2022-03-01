from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.imdb.com/chart/top/"
page = requests.get(url,verify=False)


soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find('tbody', class_="lister-list").find_all('tr')

with open('Top_movies_list.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Rank', 'Movie_name', 'Year', 'Rating']
    thewriter.writerow(header)

    for list in lists:
        Rank = list.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        Movie_name = list.find('td', class_="titleColumn").a.text
        Year = list.find('td', class_="titleColumn").span.text.strip('()')
        Rating = list.find('td', class_="ratingColumn imdbRating").strong.text
    
        info = [Rank, Movie_name, Year, Rating]
        thewriter.writerow(info)
