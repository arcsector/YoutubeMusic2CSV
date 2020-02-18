import csv
import re
import logging
from pprint import pprint 
logging.basicConfig()
lines = open("ytm.txt", 'r').read().split('\n')

songlist = []
isPrevLineSong = False
songdict = {}
timestamp = re.compile('[\d:]+')

prevline = ''
for line in lines:
    logging.debug(line)
    if line == " " or line == "":
        logging.debug("found dummy line")
        prevline = line
        continue
    
    # weed out timestamps
    if bool(timestamp.match(line)):
        logging.debug("found timestamp")
        prevline = line
        continue

    # find line of name
    if prevline == '':
        logging.debug("found song name")
        songlist.append(songdict)
        songdict = {}
        songdict['title'] = line
        isPrevLineSong = True
        prevline = line
        continue
    
    # if previous line was song, grab artist
    if isPrevLineSong:
        logging.debug("found artist")
        songdict['artist'] = line

    # if previous line was not a song, and this line still has text
    #  (because it passed the dummy line check), then we need to add 
    #  it to the artist tab, the whole reason for this script
    if not isPrevLineSong and prevline != '\t' and not prevline == '':
        logging.debug("found additional artist line")
        songdict['artist'] = songdict['artist'] + line
    
    # set previous line
    prevline = line
    # at end of loop if we've found artist previous line was not a song
    if isPrevLineSong == True:
        isPrevLineSong = False
if songlist[0] == {}:
    songlist = songlist[1:]
logging.debug("writing csv")
with open('ytm.csv', 'w+') as ytm:
    writer = csv.DictWriter(ytm, ['title', 'artist'])
    writer.writeheader()
    for x in songlist:
        writer.writerow(x)
f = open('ytm.csv', 'r')
doc = f.read().replace('\n\n', '\n')
f.close()
with open('ytm.csv', 'w') as document:
    document.write(doc)