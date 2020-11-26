import os
import requests
import cgi

#import API key
goodreadsKey = os.environ.get('VARENV')

def main():
    search_goodreads()
def search_goodreads():
    #search by Title, author or ISBN
    search = iformData.getvalue('search')

    url = str("https://goodreads.com/search/index.html?key=" + goodreadsKey + '&q=' + search)

    #request book info from GoodReads
    response = requests.get(url)

    #return response
    print(response.text)
    print(url)

    print """ Content-type: text/html\n\n
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Test</title>
        </head>
        <body>
            <p> Books {0} </p>
        </body>
    </html>
    """ .format(response.txt)
main()
