# Recursive Web Crawler User Manual

**Program Information**

The crawler.py program is a python script that will parse through the different
links of a website, clicking on each link and following the link tree through different
websites. The program will print the different links to the scren, as well as keep track
of what links have been visited. 
The program will only go to a user specified level of depth when navigating
different websites. 


**Running the Program**

To start the program the user should call crawler.py from
the command line interface

	$ python [directory]/crawler.py

Following this the user should pass in an absolute URL as the first paremeter
of the program. This is where the web crawler will start from

	$python [directory]/crawler.py https://absolute_url

The crawler will default to 3 layers of depth, though the user can override this
level of depth with an optional paremeter

[Optional Parmeter]

	If the user wishes they can add in an optional paremeter to
	change the level of depth the program links to. This is done
	by adding an integer into the second parameter

	$python [directory]/crawler.py https://absolute_url [integer]


**Potential Errors**

An error will arrise if the user attempts to pass in 
anything other than an absolute url for the main program paramter. 

An error will also arrise if the user attempts to pass in a non
integer value into the optional depth requirement

The program may come accross websites that cannot be accessed while running, this will
result in an error message being printed, but not the crashing of the program. 
