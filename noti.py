import requests, time

# the plainest update scraper
# expand for more complex pages/queries/notifications

# takes arguments of page, search query and frequency
# notifies once the query has appeared on the page

# EXAMPLE:
# Page to be queried >  https://changelogs.ubuntu.com/meta-release
# Query >  18.04
# Frequency >  5
# checks once every 5 minutes for mentions of "18.04" on the page.

with open("search.txt", "r") as f:
    for i,line in enumerate(f):
        if i==0:
            url = line[6:-2]
        if i==1:
            query = line[6:-2]
        if i==2:
            freq = float(line[6:-2])


page = requests.get(url)
if page.status_code != 200:
    print "Page didn't load successfully."
else :
    while query not in page.content :
        print "still not there..."
        time.sleep(freq*60)
        page = requests.get(url)

    print "found it! exiting..."
