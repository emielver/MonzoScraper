from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import os

# The base url for blogposts
base_url = "https://monzo.com/blog/latest/"
monzo_url = "https://monzo.com"
counter = 481

def save_blog_post(blog):
    global counter
    # Get info about the blogpost
    name = blog.h2.text
    date = blog.time.text
    # find the url of the blogpost
    blog_url = ''
    links = blog.find_all('a', {'href' : True})
    # Make sure there is only one link, otherwise there's a mistake
    assert len(links) == 1
    blog_url = links[0]['href']
    # We combine the two urls into one
    total_url = monzo_url + blog_url
    # We go onto the blog link and try to extract the text
    # We start by opening the url and extracting all text
    req = Request(total_url, headers={"User-Agent": "Mozilla/5.0"})
    html_data = urlopen(req).read()
    parsed_data = soup(html_data, "lxml")
    # Now we see that the page is split into sections, and the first section
    # is the text from the blogpost, so we extract that information
    sections = parsed_data.findAll("section")
    if counter in [274, 348, 481]:
        counter += 1
    else:
        text = sections[0].text
        # We might also want to analyse the authors and see if we can tell
        # them apart. So we use the second section to get the name of the authors
        author_info = sections[1].find_all('p')
        # Since the author's name appears first, we can 
        author = author_info[0].text
        title = author_info[1].text
        # Now we save all info of the blogpost to a file,
        # and we order them sequentially
        filename = "blogpost" + str(counter) + ".txt"
        counter += 1
        print("Creating %s" %  (filename))
        # We create and write to the file
        file = open(filename, 'w')
        # Start with the title of the blogpost
        file.write("Title: " + name + "\n")
        # Then the author
        file.write("Author: " + author + "\n")
        # Now the position of the author
        file.write("Position: "  + title + "\n")
        # Now the date of the blogpost
        file.write("Date: " + date + "\n")
        # Finally the actual text
        file.write(text)
        # Now we close it
        file.close()
        print("Wrote file and continuing!")
    
def get_blog_posts(url):
    # Get the page of blogposts
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    # Grab the data from the page
    html_data = urlopen(req).read()
    # Parse the data using BS4
    parsed_data = soup(html_data, "lxml")
    # Find the list of all blogposts
    blogs = parsed_data.findAll("article")
    print("Found %d blogs!" % len(blogs))
    # for each blogpost
    for blog in blogs:
        # save the blogpost
        save_blog_post(blog)

def main():
    # Where we want to store the blogposts
    os.chdir("/Users/emielv/desktop/MonzoBlogs")
    # different for the first page
##    url = base_url
##    print("Checking page 1 of blogposts")
##    get_blog_posts(url)
    # For the number of pages
    for i in range(41, 45):
        print("Checking page %s of blogposts" % i)
        url = base_url + str(i) + "/"
        get_blog_posts(url)

main()
    
