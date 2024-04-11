import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Create the soup
response = requests.get(url=URL)
content = response.text
soup = BeautifulSoup(markup=content, features='html.parser')

# Create list of 100 movies in form of '1) The Godfather'
raw_movies = soup.find_all(name='h3')
movie_list = [(movie.getText() + "\n") for movie in raw_movies]

# Reverse the list so that #1 is first
movie_list.reverse()

# Save 100 movies to movies.txt
with open("./movies.txt", 'w', encoding='utf-8') as movie_file:
    movie_file.writelines(movie_list)
