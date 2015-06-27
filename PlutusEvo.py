import requests
import sys
import csv
import os

'''
Plutus - a micro CSV downloader written in Python

-- Updated with multiple download endpoints --
-- Updated with directory download --
'''


def main():
    subroute()

def first(): # endpoint one
    url = ("http://example")
    b = requests.get(url)
    name_of_file = 'save'
    save_path = 'data' # location
    complete = os.path.join(save_path, name_of_file+'.csv')
    with open(complete, "wb") as output:
        output.write(b.content)
    output.close()

def second(): # endpoint two
    url = ("http://example") #url
    c = requests.get(url) #requests get module
    name_of_file = 'savetwo'
    save_path = 'data'
    complete = os.path.join(save_path, name_of_file+'.csv')
    with open("savetwo.csv", "wb") as output: # save file
        output.write(c.content)
    output.close() // close file

def subroute(): // subroute (main dispatch and control)
    first()
    second()
    sys.exit() // terminate after use.


while __name__ == "__main__":
    main()
