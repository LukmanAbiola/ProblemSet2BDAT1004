import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def webdir(URL: str, depth: int, indent: int, total_allowed_links = 5):
    # This function takes URL, depth and indent as parameters
    # total_allowed_links is an additional variable that sets upper limit for links to be printed (for the sake of demonstration)

    if depth == 0:
        # Just print the current URL
        curr_url = ' '*indent + URL
        print(curr_url)
    else:
        curr_url = ' '*indent + URL
        print(curr_url)
        try:
            # Get the response from current URL
            response = requests.get(URL)
            if response.status_code != 200:
                return
            children_links = extract_links(response.text)
            for child_link in children_links:
                if total_allowed_links <= 0:
                    break
                # Make absolute link
                absolute_url = urljoin(URL, child_link)
                total_allowed_links -= 1
                webdir(absolute_url, depth - 1, indent + 4)
        except:
            print("Some exception occurred")


def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


# URL = 'https://www.apple.com/in/mac/'
# webdir(URL, 2 , 0)
