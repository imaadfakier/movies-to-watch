import requests
import bs4
import lxml
import collections

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
response.raise_for_status()
website_html = response.text

soup = bs4.BeautifulSoup(website_html, 'html.parser')


def give_me_numbers(start, stop=0, step=1):
    for the_num in range(start, stop, step):
        yield the_num


movie_names_with_text_before = soup.select('.jsx-4245974604.listicle-item-content p:nth-child(2) a:first-child')[::-1]

hundred_movies_list = collections.OrderedDict(
    {
        f'{num}': movie_names_with_text_before[num - 1].string[24:]
        for num
        in give_me_numbers(1, len(movie_names_with_text_before) + 1)
    }
)  # <-- learned something new!!

with open('top-97-movies.txt', 'w') as file:
# with open('top-97-movies-changed-format.txt', 'w') as file:
    # for ranking, movie in hundred_movies_list:  # ValueError: not enough values to unpack (expected 2, got 1)
    # for movie_info in hundred_movies_list:  # only keys will be accessible; same with hundred_movies_list.keys()
    for ranking, movie in hundred_movies_list.items():
        file.write('{ranking}) {movie}\n'.format(ranking=ranking, movie=movie))
