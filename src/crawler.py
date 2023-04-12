#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys
import time

def crawl(url,maxdepth = 2, depth = 0, visited = set(), urlDepths = []):
    try:
        try:
            """
            Given an absolute URL, print each hyperlink found within the document.
        
            Your task is to make this into a recursive function that follows hyperlinks
            until one of two base cases are reached:
        
            0) No new, unvisited links are found
            1) The maximum depth of recursion is reached
            """
            if url not in visited:
                for i in range(depth):
                    print("    ", end="")
                print(url)
                urlDepths.append(url)
                visited.add(url)
            response = requests.get(url)
            if not response.ok:
                print(f"crawl({url}): {response.status_code} {response.reason}")
                visited.add(url)
                return len(visited)
            html = BeautifulSoup(response.text, 'html.parser')
            links = html.find_all('a')

            if depth >= maxdepth:
                depth += 1
                for a in links:
                    link = a.get('href')
                    absoluteURL = urljoin(url, link)
                    if (link == None) or ("#" in link):
                        continue
                    elif absoluteURL not in visited:
                        # Create an absolute address from a (possibly) relative URL

                        # Only deal with resources accessible over HTTP or HTTPS
                        if absoluteURL.startswith('http'):
                            for i in range(depth):
                                print("    ", end="")
                            print(absoluteURL)
                            visited.add(absoluteURL)
                            requests.get(absoluteURL)
                depth -= 1
            else:
                for a in links:
                    link = a.get('href')
                    absoluteURL = urljoin(url, link)
                    if (link == None) or ("#" in link):
                        continue
                    elif absoluteURL not in visited:
                        # Create an absolute address from a (possibly) relative URL

                        # Only deal with resources accessible over HTTP or HTTPS
                        if absoluteURL.startswith('http'):
                            depth += 1
                            return crawl(absoluteURL,maxdepth,depth,visited,urlDepths)
            if len(urlDepths) > 1:
                urlDepths = urlDepths[:-1]
                return crawl(urlDepths[-1],maxdepth,depth - 1,visited,urlDepths)
            else:
                return len(visited)
        except KeyboardInterrupt:
            return len(visited)
    except:
        print(f"an error occured while attempting to access {url}")
        return crawl(url, maxdepth, depth, visited, urlDepths)

## An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
elif len(sys.argv) == 2:
    url = sys.argv[1]
    maxDepth = 3
elif len(sys.argv) == 3:
    url = sys.argv[1]
    maxDepth = int(sys.argv[2])

#print("\tTODO: determine whether variable `url` is an absolute URL")

if bool(urlparse(url).netloc):

    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")

    beforeTime = time.time()

    numURLS = crawl(url, maxDepth - 1)

    afterTime = time.time()

    print(f"Program ran for {afterTime-beforeTime} seconds and visited {numURLS} unique URLs")
    #print("\tTODO: are all of the TODOs deleted?")

else:
    print("Error: argument supplied is not an absolute url")