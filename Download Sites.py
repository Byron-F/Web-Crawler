import sys
import urllib.request
import os

try:
    file = open(sys.argv[1])
    sites = (file.read()).split()
    file.close()
except IndexError as ex:
    try:
        file = open("sites.txt")
        sites = (file.read()).split()
        file.close()
    except IOError as ex:
        print("FAIL: Failed to find a sites.txt")
        sys.exit(-1)
except IOError as ex:
    print("WARNING: Failed to find file")
    try:
        file = open("sites.txt")
        sites = (file.read()).split()
        file.close()
    except IOError as ex:
        print("FAIL: Failed to find a sites.txt")
        sys.exit(-1)

for i in range(len(sites)):
    print("Downloading Sites: (" + str(i + 1) + '/' + str(len(sites)) + ')', end='\r')
    sys.stdout.flush()

    try:
        data = urllib.request.urlopen(sites[i]).read()
    except Exception as ex:
        print("Failed to download: " + str(sites[i]))

    with open('HTML/' + ''.join(c for c in sites[i] if not c in ['.',':','/'])[6:][:-3] + '.html','wb+') as file:
        file.write(data)
