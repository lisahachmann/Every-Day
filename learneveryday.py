import time
from time import localtime as lt
#import beautifulsoup4 as bs4

class learn_everyday():

# A function that emails me one website/fact a day.
# Allows me to choose between a wikipedia page and a dictionary entry.

  def __init__(self):
    self.time = lt()
    self.timestr = time.strftime("%H:%M:%S", lt())

  #def wikipedia_scraping(self):
    #need a way to choose a random entry in wikipedia. list all, random number index and then that entry?

  def send_email(self, time):
    if (self.time == '7:00:00'):
        #send the email when it's 7AM 
        print(time)
        print (type(time) is str)



if __name__ == '__main__':
    teacher = learn_everyday()
    timetaught = teacher.send_email(teacher.timestr)
    print(timetaught)
