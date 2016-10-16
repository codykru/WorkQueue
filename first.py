import time
import os
import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]  	# [('User-agent', 'Firefox')]

url="http://www.nettutor.com"
response = br.open(url)

html = response.read()
soup = BeautifulSoup(html, 'html.parser')




response1 = br.response()  # get the response again
#print (response1.read())     # can apply lxml.html.fromstring()

#have to input in quotes currently 
username=input("username:")
#username="username"
password=input("pass:")
#password="pass"

br.select_form(nr=0)
br.form['username'] = username
br.form['password'] = password
br.submit()



#print(response.read())      # the text of the page
start_time = time.time()
time_seconds = 30

current_time = start_time
# while(time.time() - start_time < time_seconds):

while(1):

	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	# os.system('clear')
	curr_response = br.response()  # get the response again
	# print (response1.read())     # can apply lxml.html.fromstring()\


	soup = BeautifulSoup(curr_response)
	print("\n===============================================================================================")

	titles = soup.find_all('tr')[0]
	for tit in titles:
		print('%14s' % tit.text),
		print('\t'),

	for tr in soup.find_all('tr')[1:]:
		student = tr.find_all('td')
		i = 0
		# widths = ['10','10','10','10','10','10','10',]

		print('\n')					#skip new line to beautify a bit
		for data in student:
			if(len(data.text) > 14):
				print('%14s' % "placeholder"),
			else:
				print('%14s' % data.text ),
			print("\t"),
		print("\n------------------------------------------------------------------------------")
	time.sleep(5)
