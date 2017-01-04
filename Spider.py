from __future__ import print_function
from bs4 import BeautifulSoup
from time import time
import urllib2
import sys
import re

try:
    linksWorking = [sys.argv[1]]
except IndexError as ex:
    print("You did not specify a site.")
    sys.exit(-1)

try:
    sys.argv[2]
except IndexError as ex:
    print("You did not specify a search topic.")

linksProcessed = []
UsefulUrls = []

def extractLinks(site):
    global linksWorking
    global titles
    req = urllib2.Request(site, headers={'User-Agent' : "Byron's Spider"})
    html = urllib2.urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        if link.get('href') not in linksWorking and link.get('href') not in linksProcessed: # stops links being duplicated
            linksWorking.append(link.get('href'))

def scanForTopic(URL, searchForTopic):
    global UsefulUrls
    soup = BeautifulSoup(urllib2.urlopen(URL).read(), 'html.parser')
    if bool(soup.body.findAll(text=searchForTopic)):
        UsefulUrls.append(URL)

s = round(time(), 2)

while True:
    print('Link Count: ' + str(len(linksWorking) + len(linksProcessed)) + '   Time Elapsed ' + str(round(time() - s, 2)) + 's', end='\r')
    sys.stdout.flush()
    try:
        scanForTopic(linksWorking[0], sys.argv[2])
        extractLinks(linksWorking[0])
        linksProcessed.append(linksWorking[0])
        linksWorking.pop(0)
    except IndexError as ex:
        print("Processing Complete\nHere are the indexed sites!\n")

        print(('\n').join(linksProcessed) + '\n' + ('\n').join(linksWorking))

        print("\n Useful Urls \n")

        print(('\n').join(UsefulUrls))
        try:
            with open("sites.txt",'w') as file:
                file.write(('\n').join(linksWorking) + '\n' + ('\n').join(linksProcessed))

            with open("sites_found.txt",'w') as file:
                file.write(('\n').join(UsefulUrls))
        except UnicodeError as ex:
            with open("sites.txt",'w') as file:
                for i in sites:
                    try:
                        file.write(i + '\n')
                    except UnicodeError as ex:
                        pass
            with open("sites_found.txt",'w') as file:
                for i in UsefulUrls:
                    try:
                        file.write(i + '\n')
                    except UnicodeError as ex:
                        pass
        sys.exit(0)
    except KeyboardInterrupt as ex:
        print("\nLogging & Exiting...\nHere are the indexed sites!\n")

        print(('\n').join(linksProcessed) + '\n' + ('\n').join(linksWorking))

        print("\n Useful Urls \n")

        print(('\n').join(UsefulUrls))
        try:
            with open("sites.txt",'w') as file:
                file.write(('\n').join(linksWorking) + '\n' + ('\n').join(linksProcessed))

            with open("sites_found.txt",'w') as file:
                file.write(('\n').join(UsefulUrls))
        except UnicodeError as ex:
            with open("sites.txt",'w') as file:
                for i in sites:
                    try:
                        file.write(i + '\n')
                    except UnicodeError as ex:
                        pass
            with open("sites_found.txt",'w') as file:
                for i in UsefulUrls:
                    try:
                        file.write(i + '\n')
                    except UnicodeError as ex:
                        pass
        sys.exit(0)
    except urllib2.URLError as ex:
        pass

    except Exception as ex:
        print("\n--- Error Occurred ---\n")
        print(str(format(ex)))
        try:
            with open("sites.txt",'w') as file:
                file.write(('\n').join(linksWorking) + '\n' + ('\n').join(linksProcessed))
        except UnicodeError as ex:
            with open("sites.txt",'w') as file:
                for i in linksWorking:
                    try:
                        file.write(i + '\n')
                    except UnicodeError as ex:
                        pass
                for i in linksProcessed:
                    try:
                        file.write(i + '\n')
                    except UnicodeError as ex:
                        pass
        sys.exit(0)
        linksWorking.pop(0)
