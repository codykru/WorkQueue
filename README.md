# WorkQueue
A project created to better view the students waiting in queue for NetTutor.com, does not require a second browser 

Very Specific use. 

Trying to port the entire thing to use curses but running into some issues. 
  * Page does not refresh
  * Experience with curses is minimal at best 
  
Currently: pastes over the terminal over and over again, was using os.clear() 
          but was testing to see if the data was updating (which it is not)

curs.py is an experimentation with curses
first.py is the first attempt at writing this python script to do so. 

ISSUES: 
*mechanize is not compatible with python3, have to look into alternatives. 
