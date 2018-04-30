This is the plainest update scraper! Can be expanded for more complex queries.

Takes the page url, keyword, and frequency (in minutes) as arguments, then queries the page at the given frequency and checks for the appearance of the keyword.

#### How can this be useful?
If you're waiting for a ticket release, new webcomic chapter or even a relevant tweet, you can set this to run and forget about refreshing the page yourself!

#### Example:
search.txt:
```
url: "https://changelogs.ubuntu.com/meta-release"
key: "18.04"
frq: "5"
```

noti.py:
Checks once every 5 minutes for the meta-release of Ubuntu 18.04 in the changelogs.

#### How can I expand this?
Add a sound notification! Add an image pop-up! Get rid of the text output and make it terminal-independent!

#### How do I RUN this?

` git clone "https://github.com/haexa/notipy.git"`\
` cd notipy`\
Open search.txt with your text editor of choice and change the url, key and frq variables.
` python noti.py`


#### How did you think of this name? It's genius and very original!
Thanks, I'm creative like that.
