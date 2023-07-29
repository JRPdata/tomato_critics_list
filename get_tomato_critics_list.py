import json
import requests
from bs4 import BeautifulSoup
from time import sleep

def get_critic_names(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    critic_names = []
    for critic in soup.find_all('a', class_='critic-authors__name'):
        critic_names.append(critic.text.strip())
    return critic_names

def main():
    base_url = "https://www.rottentomatoes.com/critics/authors?letter="
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '#']

    all_critics = []

    for letter in letters:
        url = base_url + letter.lower()
        critics = get_critic_names(url)
        all_critics.extend(critics)
	# Don't hammer server
        sleep(2)

    all_critics.sort()  # Sort the list of critic names alphabetically

    with open("tomato_current_critics.json", "w") as json_file:
        json.dump(all_critics, json_file, indent=4)

    print(f"Number of critics found: {len(all_critics)}")

if __name__ == "__main__":
    main()
