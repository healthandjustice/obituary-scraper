# Obituary Scraper

This code was developed in Python and scrapes Legacy.com for a list of names and birth dates. Matches only occur if the names and birth dates are a match. The code parses two different HTML elements to find age, birth date, and death date. The code utilizes beautiful soup to parse text from HTML elements. The first element is:

> 'obit_age_data = result.find('div', class_='PersonAge').text'

The second element is:

> 'obit_text = result.find('div', class_='obitText').text'

There are several methods used to parse years and age values from these text blurbs.

The code only looks for people with death years > 2017. This is project specific and can be adjusted in the code.

# Project status: 

This project is in the development phase. We are in the process of developing the algorithm that captures ages and dates from obituary text on Legacy.com. There is code that is specific to testing. This code appended data to the results when there is not a name and birth year match. It goes down the list of results from Legacy.com ([example](https://www.legacy.com/search?countryId=366899&countryUrl=united-states-of-america&dateRange=All&firstName=john&lastName=smith&stateAbbrev=NC&stateId=366845&stateUrl=north-carolina)) and appends data so that we can visually assess whether a match could have been made and adjust the algorithm accordingly. When the algorithm is complete, we can remove the following code: lines 178 – 284.  

# Libraries 

## Csv: 

* This library is used to read in the list of releases. For NC it comes in CSV format. 
* Documentation: https://docs.python.org/3/library/csv.html 

## Requests: 

* This library is used to send HTTP requests to www.legacy.com.  
* Documentation: https://pypi.org/project/requests/ 

## BeautifulSoup: 

* This library is used to parse through the HTTP response body, which is in HTML. 
* We can use it to scan the hierarchy of HTML tags and access values. 
* Documentation: https://beautiful-soup-4.readthedocs.io/en/latest/ 

## Re: 
* This library is used to search via regular expression. 
* We use it to parse the obituary blurb that often comes with a PersonItem. 
* We use it to extract numbers, such as Age and birth year. 

# Project Setup: 

## Location: https://github.com/healthandjustice/obituary-scraper 

1. Go to terminal and run “git clone https://github.com/healthandjustice/obituary-scraper.git” 
2. Open up the obituary-scraper folder in your code editor of choice.  
3. If you aren’t sure where to start I recommend vscode or sublime text 
4. Open scrape_obits.py 
5. Follow instructions specific to your code editor to select the virtual environment interpreter. 
6. If you need help creating a virtual environment: https://docs.python.org/3/library/venv.html 
7. Check that the “./data” folder contains your input: “nc_releases_1000.csv” 
8. Run the code and verify that the output is saved in “./output”. 

# TO-DO: 

## Important: When testing and debugging code, limit the number of requests you send to Legacy.com. Sending thousands of requests at once many times a day could cause them to block the program in their robot.txt file. 

* Analyze the current output and look for ages and years in the obituary text that were not captured. 
* Add to regular expression or adjust the algorithm to capture all of these. For example, we want to extract AGE: 73, DEATH_YEAR: 10/31/2201, BIRTH_YEAR: 05/16/1948. 
* Remove code that lists potential matches: lines 178 – 284. If development is ongoing these line numbers will change. 
* Obtain the final list of release names and birth years 
* Run the code with the new input  

 

 