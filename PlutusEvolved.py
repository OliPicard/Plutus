import requests
import sys
import csv

'''
Plutus - a micro CSV downloader written in Python

-- Updated with multiple download endpoints --
'''


def main():
    subroute()

def first(): // endpoint one
    url = ("http://example")
    b = requests.get(url)
    with open("saveone.csv", "wb") as output:
        output.write(b.content)
    output.close()

def second(): // endpoint two
    url = ("http://example") //url
    c = requests.get(url) //requests get module
    with open("savetwo.csv", "wb") as output: // save file
        output.write(c.content)
    output.close() // close file

def subroute(): // subroute (main dispatch and control)
    first()
    second()
    sys.exit() // terminate after use.


while __name__ == "__main__":
    main()
