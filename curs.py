import curses

import time
import os
import mechanize
#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]  	# [('User-agent', 'Firefox')]

url="http://www.nettutor.com"
response = br.open(url)

html = response.read()
soup = BeautifulSoup(html, 'html.parser')


response1 = br.response()  # get the response again


#username=input("username:")
username="nt_admin"
#password=input("pass:")
password="NetTutor@2015"

br.select_form(nr=0)
br.form['username'] = username
br.form['password'] = password
br.submit()



#print(response.read())      # the text of the page
start_time = time.time()
time_seconds = 30

##CURSES!!!!!!!!

stdscr = curses.initscr()

curses.noecho()

curses.cbreak()

stdscr.keypad(1)



begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE )

#appears my terminal is 43 deep by 139 wide. something to work wi(d)th.

stdscr.addstr(20,50," NET  TUTOR ",curses.color_pair(1) )
stdscr.addstr(21,50,"  MONITOR! ",curses.color_pair(1) )

time.sleep(1)
stdscr.refresh()
time.sleep(1)
###END CURSES!!!!!!!
