import os
import requests
import caching

#import API key
goodreadsKey = os.environ.get('VARENV')

def main():
    search_goodreads()
def search_goodreads():
    #search by Title, author or ISBN
    search = input("Enter search: ")

    url = str("https://goodreads.com/search/index.html?key=" + goodreadsKey + '&q=' + search)

    #request book info from GoodReads
    response = requests.get(url)

    #return response
    print(response.text)
    print(url)
main()
