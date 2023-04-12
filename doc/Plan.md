# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

Takes in 2 command line arguments from the user, firstly (and required) a 
absolute url, the second (optional) argument from the user is the maximum number of
links from the starting website to navigate. Default 3 links for argument two

The program will then go to a variety of links and print to the user the maximum number
of links followed and the time it took to go to those links 


## Phase 1: System Analysis *(10%)*

**Deliver:**

Takes in an absolute url from the user which is saved to a set to keep track of, and
also to a variable for successive recursion. 

The program then uses third party modules to check for other URLs on the website, finds
one, joins the partial url with the previous URL to create a new absolute URL, passes
this argument back into the original program. 

Establish a base case check for each iteration, check to see if a link that is found has
already been visited, if it has then it is skipped. If the program cannot find any links
or any links that haven't already been visited, then the program exits.


## Phase 2: Design *(30%)*

**Deliver:**

crawl(url, maximum depth = 2, depth = 0, visitsed = set()):
	

	#program should print out the current url at the level of depth that
	#the program is currently at
	for i in range(depth):
		print("    ",end=""_
	print(url)



	if depth >- maximum depth:
		if the level of depth by the program is
		currently at the maximum depth of the program
		All current links on the page should be printed
		and then the program should return back to the previous level of 
		depth

	else:
		program should look at all links on the page.	
		if a link on the page hasn't yet been visited
		the program should increase the depth by 1
		append the link to the visited hashable set,
		and then call the crawl() function again but 
		passing in the new url
		crawl(newURL, maximumDepth, depth, visited)

	
if len(sys.argv) < 2:
	print an error message to the screen
	specifiying not enough inputs and quit the 
	program
elif len(sys.argv) == 2:
	the url of the program should be equal to the user
	specified url and the depth will 
elilf len(sys.argv) == 3:
	the url should be user specified 
	and the depth of the program should also be user specified


Call function and establish time variables to handle how long the program is running


## Phase 3: Implementation *(15%)*

**Deliver:**

import requests
from bs4 import Beautiful Soup
from urllib.prase import urlparse, urljoin
import sys
import time

def crawl(url, maxdepth = 2, depth = 0, visited = set(), previousURLs = []):
	try:
		previousURLs.append(url)
		for i in range(depth):
			print("    ", end = "")
		print(url)
		visisted.add(url)
		response = requests.get(url)
		if not response.ok:
			print(f"crawl({url}): {response.status_code} {response.reason}")
			return
		
		html = BeautifulSoup(response.text, 'html.parser')
		links = html.find_all('a')
	
		if depths >= maxdepth:
			depth += 1
			for a in links:
				link = a.get('href')
				absoluteURLl = urljoin(url,link)
				if absoluteURL not in visited:
					if (link == None) or ('#' in link):
						continue
					elif absoluteUrl.startswith('http')
						visited.add(absoluteURL)
						for i in range(depth):
							print(absoluteURL)
						print(absoluteURL)
				depth -= 2
				return crawl(urlDepths[-2],maxdepth,depth,visited,previousURLs)
		else:
			for a in links:
				link = a.get('href')
				absoluteURL = urljoin(url,link)
				if (link == None) or ("#" in link):
					continue
				elif absoluteURL not in visited:
					if absoluteURL.startswith('http'): depth += 1 
						return crawl(absoluteURL, maxdepth, depth, visisted, previousURLs)
		return len(visited)
	except KeyBoardInterrupt:
		return len(visited)

if len(sys.argv) < 2:
	print("Error: no Absolute URL supplied")
elif len(sys.argv) == 2:
	url = sys.argv[1]
	maxDepths = 2
elif (len(sys.argv) == 3:
	url = sys.arv[1]	
	maxDepth = int(sys.argv[2])

plural = 's' if maxDepth != 1 else ''
print(f"Crawling from {url} to a maximum depth of {maxDepth + 1} link{plural}")

beforeTime = time.time()
numURLS = crawl(url,maxDepth)

afterTime = time.time()

print(f"Program ran for {afterTime-beforeTime} seconds and visited {numURLS} unique URLs')

## Phase 4: Testing & Debugging *(30%)
**Deliver:**

Program had some issues with not being able to go back to a previous layer to look
at new URLS. I fixed this by adjusting the ways in which the URLS are printed to the
screen, so now the formatting of all the different layers are correct.

Program had some issues of getting stuck in a loop of continually going back
to the same existing URL. I fixed this by making sure that it was added to the 
visited set, and if it was then it would refuse to look at it again. 

Program on testing server says that it visits a site multiple times, though while it does
go back to a previous URL to look at the next possible links it doesn't actualy do much
with that URL, so I didn't know how to fix that

Excpetion handling had some issues, though I was able to get the try and except blocks 
nested properly to work out


## Phase 5: Deployment *(5%)*

**Deliver:**

Program successivly pushed to git lab and all parts of the program are still functional 





## Phase 6: Maintenance

**Deliver:**

Most all of my program is decently clear when looking at it. The different if and elif
blocks make the flow of data throughout the program pretty easy to look at. Additionally, the 
calculations being performed within the different blocks is also clear, only having a brief
look at the contents of the url, and then deciding whether or not to pass it into 
the program

Theres a chance that some of the different nests in the program could get a bit
confusing looking at it on first glance, though im pretty sure that it would be easy to 
figure out

The doccuemntation is clear, with the manual offering a clear explanation to how the computer works,
and also the plan including a clear purpose of the system and a clear explanation for the 
written code.

The only way the program would stop working after updating is if the third party modules imported
by the program stop working for some reason. If that does occur then there isn't anything that
I can do about it and I will jsut have to wait for the third party module developers to fix it. 

It would be quite easy to add in a new feature to this program in a few months, the code is
flexible and recursive, so simply changing one function will change the entire program. 

It would be quick to find the cause of a bug if it were reported, the program is small and all
the functionality of the program is isolated to one function, and that function only contains
two if/elif/else blocks. 

All parts of this program work in a way that I understand



