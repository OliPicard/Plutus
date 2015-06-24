import requests
import sys
import csv

'''
Plutus - a micro CSV downloader written in Python
'''


def main():
    subroute()

def subroute():
    url = ('http://example') // a path to your server.
    b = requests.get(url)
    with open("save.csv", "wb") as output:
        output.write(b.content)
    output.close()
    sys.exit()








while __name__ == "__main__":
    main()
