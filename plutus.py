import requests
import sys
import os
import csv
from io import StringIO
import json
#!/usr/bin/env python
'''
Plutus - a micro CSV downloader written in Python
-- Updated with multiple download endpoints --
-- Updated with alternative directory support --
Developed with love by OliPicard - Man Machine Software Inbetween copyright 2015
'''


def main():
    subroute()


def settings():
    try:
        config = json.loads(open('config.json').read())
        if len(config['ip']) == 0:
            print("Please edit your config.json file to include the proxy URL.")
            sys.exit()
        if len(config['save_path']) == 0:
            print("Please edit your config.json file to include the save_path.")
            sys.exit()
        if len(config['image_path']) == 0:
            print("please edit your config.json file to include the image_path.")
            sys.exit()
    except IOError:
        print("Json failed to load. terminating application")
        sys.exit()
    return config

def one():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/include/export.php?type=Pass")
    b = requests.get(url)
    name_of_file = 'save'
    save_path = config['save_path']
    complete = os.path.join(save_path, name_of_file+".csv")
    with open(complete, "wb") as output:
        output.write(b.content)
    output.close()

def two():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/include/export.php?type=SSH")
    c = requests.get(url)
    name_of_file = 'saveone'
    save_path = config['save_path']
    complete = os.path.join(save_path, name_of_file+".csv")
    with open(complete, "wb") as output:
        output.write(c.content)
    output.close()

def three():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/generated-graphs/connections_per_country_pie.png")
    d = requests.get(url)
    name_of_file = 'sometwo'
    save_path = config['image_path']
    complete = os.path.join(save_path, name_of_file+".png")
    with open(complete, "wb") as output:
        output.write(d.content)
    output.close()

def four():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/generated-graphs/success_ratio.png")
    e = requests.get(url)
    name_of_file = 'somethree'
    save_path = config['image_path']
    complete = os.path.join(save_path, name_of_file+".png")
    with open(complete, "wb") as output:
        output.write(e.content)
    output.close()

def five():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/generated-graphs/human_activity_per_day.png")
    f = requests.get(url)
    save_path = config['image_path']
    name_of_file = 'somefour'
    complete = os.path.join(save_path, name_of_file+".png")
    with open (complete, "wb") as output:
        output.write(f.content)
    output.close()



def six():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/include/export.php?type=allActivity")
    d = requests.get(url)
    csv_file = StringIO(d.content.decode())
    csv_reader = csv.DictReader(csv_file)
    save_path = config['save_path']
    name_of_file = 'output'
    complete = os.path.join(save_path, name_of_file+".csv")
    fieldnames = ['??timestamp', 'username', 'password', 'input']
    with open(complete, 'w', newline='') as output:
        w = csv.DictWriter(output, fieldnames=fieldnames)
        w.writeheader()
        for row in csv_reader:
            new_row = {field: row[field] for field in fieldnames}
            w.writerow(new_row)
def seven():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/generated-graphs/probes_per_day.png")
    e = requests.get(url)
    save_path = config['image_path']
    name_of_file = 'somefive'
    complete  = os.path.join(save_path, name_of_file+".png")
    with open (complete, "wb") as output:
        output.write(e.content)
    output.close()

def eight():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/include/export.php?type=Combo")
    d = requests.get(url)
    csv_file = StringIO(d.content.decode())
    csv_reader = csv.DictReader(csv_file)
    save_path = config['save_path']
    name_of_file = 'somesix'
    complete = os.path.join(save_path, name_of_file+".csv")
    fieldnames = ['\ufeff\ufeffusername/password', 'COUNT(username)']
    with open(complete, 'w', newline='') as output:
        w = csv.DictWriter(output, fieldnames=fieldnames)
        w.writeheader()
        for row in csv_reader:
            new_row = {fieldnames[0]: '{\ufeff\ufeffusername}/{password}'.format(**row), fieldnames[1]: row['COUNT(username)']}
            w.writerow(new_row)
def nine():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/generated-graphs/top10_combinations_pie.png")
    g = requests.get(url)
    save_path = config['image_path']
    name_of_file = 'somesix'
    complete = os.path.join(save_path, name_of_file+".png")
    with open(complete, "wb") as output:
        output.write(g.content)
    output.close()

def ten():
    config = settings()
    ip = config['ip']
    url = ("http://"+ip+"/kippo-graph/generated-graphs/top10_usernames.png")
    h = requests.get(url)
    save_path = config['image_path']
    name_of_file = 'someseven'
    complete = os.path.join(save_path, name_of_file+".png")
    with open(complete, "wb") as output:
        output.write(h.content)
    output.close()

def subroute():
    one()
    two()
    three()
    four()
    five()
    six()
    seven()
    eight()
    nine()
    ten()
    sys.exit()


if __name__ == "__main__":
    main()