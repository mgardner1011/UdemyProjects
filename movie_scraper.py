"""
Empire's top 100 movie list page https://www.empireonline.com/movies/features/best-movies-2 is rendered using JavaScript
so the data we are looking to scrape is not in the source code.
In order to pull the list of 100 movies we are wanting you will need to run this code in the developer tools console
copy(document.querySelector('html').outerHTML)
Once that is copied, you can save a local file of the html, and run the rest of the code in this file
"""
from bs4 import BeautifulSoup

try:
    with open('website.html') as file:
        contents = file.read()
except FileNotFoundError:
    print("You need to create the html file for Empire's website locally")
soup = BeautifulSoup(contents, 'html.parser')

movie_tags = soup.find_all(name='h3', class_='jsx-4245974604')
movie_list = [movie.getText() for movie in movie_tags]
movie_list.reverse()

with open('movie_list.txt', mode='w') as file:
    for movie in movie_list:
        file.write(f'{movie}\n')
