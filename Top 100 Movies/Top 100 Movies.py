import logging
import requests
from bs4 import BeautifulSoup
logging.basicConfig(level=logging.INFO)

try:
    logging.info("Attempting to make connection")
    URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    logging.info("Connection made successfully")
except RuntimeError:
    logging.warning("Unable to make connection")

logging.debug("Fetching html from website")
website = requests.get(URL).text
soup = BeautifulSoup(website, "html.parser")

logging.debug("Attempting to local h3 title objects")
movies = soup.find_all("h3", "title")

titles = [movie.get_text() for movie in movies][::-1]

try:
    logging.info("Attempting to write to file")
    with open("movies.txt", mode="w") as file:
        for movie in titles:
            file.write(f"{movie}\n")
    print(f"Successfully wrote list to file: {file.name}")
    logging.info("Successfully wrote to file")
except FileNotFoundError:
    logging.warning("No such file exists")
except FileExistsError:
    logging.warning("Unable to write to existing file of the same name")
