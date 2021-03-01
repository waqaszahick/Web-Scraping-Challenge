# Web-Scraping-Challenge
Assignment # 11: Web Scraping

This is my over all 11th, and fir 'web scraping' assignment. In this assignment, I was required to build a web application that scrapes various websites for data related to the "Mission to Mars" and to display the information in a single HTML page. It was a 2-step assignment and I performed the following tasks to complete it:

Step 1: Scraping

* I complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests / Splinter.
* I create a Jupyter Notebook file called "mission_to_mars.ipynb" and used this to complete all of my scraping and analysis tasks.
* I scraped the following:
  - NASA Mars News - scrape the "NASA Mars News" website and collected the latest "News Title" and "(News) Paragraph Text". Assigned the text to variables that I could reference later.
  - JPL Mars Space Images (Featured Image):
    1. Visited the URL for JPL "Featured Space Image".
    2. Used "Splinter" to navigate the site, to find the image URL for the current "Featured Mars Image", and assigned the URL string to a variable called featured_image_url.
    3. Made sure to find the image URL to the full size ".jpg" image.
    4. Made sure to save a complete URL string for this image.
  - Mars Facts:
    1. Visited the "Mars Facts" web page and used "Pandas" to scrape the table containing facts about the planet including Diameter, Mass, etc.
    2. Used "Pandas" to convert the data to a HTML table string.
  - Mars Hemispheres:
    1. Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
    2. I had to click each of the links to the hemispheres in order to find the image URL to the full resolution image.
    3. Saved both the image URL string for the full resolution hemisphere image, and the hemisphere title containing the hemisphere name.
    4. Used a "Python" dictionary to store the data using the keys "img_url" and "title"
    5. Appended the dictionary with the image URL string and the hemisphere title to a list. This list contained one dictionary for each hemisphere.

Step 2 - MongoDB and Flask Application

* Used "MongoDB" with "Flask" templating to create a new HTML page that displayed all of the information that was scraped from the URLs above.
* Started by converting my "Jupyter" notebook into a "Python" script called "scrape_mars.py" with a function called "scrape" that would execute all of my scraping code from above, and return one "Python" dictionary containing all of the scraped data.
* Created a route called "/scrape" that would import my "scrape_mars.py" script and would call my "scrape" function.
* Stored the return value in "Mongo" as a "Python" dictionary.
* Created a root route "/" that would query my "Mongo" database and would pass the Mars data into an HTML template to display the data.
* Created a template HTML file called "index.html" that would take the Mars data dictionary and would display all of the data in the appropriate HTML elements.