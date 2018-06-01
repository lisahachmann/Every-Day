import time
from time import localtime as lt
import bs4
import html.parser as hp
import requests

class learn_everyday():

# A function that emails me one website/fact a day.
# Allows me to choose between a wikipedia page and a dictionary entry.

  def __init__(self):
    self.time = lt()
    self.timestr = time.strftime("%H:%M:%S", lt())
    self.soups = {}

  def wikipedia_scraping(self, url):
    #need a way to choose a random entry in wikipedia. list all, random number index and then that entry?
    r = requests.get(url)
    html = str(r.content)
    self.soups[url] = bs4(html, 'html.parser')

  def send_email(self, time):
    if (self.time == '7:00:00'):
        #send the email when it's 7AM
        print("It's 7AM")
        print (type(time) is str)
    print (time)

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Pioneer_Helmet'
    teacher = learn_everyday()
    timetaught = teacher.send_email(teacher.timestr)
    teacher.wikipedia_scraping(url)
