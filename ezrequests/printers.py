import requests
from bs4 import BeautifulSoup

def h1_printer(url):
    """ get the h1 tag text from any url and print it """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tag = soup.find('h1')
    if h1_tag:
        print(h1_tag.text)
    else:
        print("No <h1> tag found.")

def h2_printer(url):
    """ get the h2 tag text from any url and print it """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h2_tag = soup.find('h2')
    if h2_tag:
        print(h2_tag.text)





