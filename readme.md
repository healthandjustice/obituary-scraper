# Obituary Scraper

This code was developed in Python and scrapes Legacy.com for a list of names and birth dates. Matches only occur if the names and birth dates are a match. The code parses two different HTML elements to find age, birth date, and death date. The code utilizes beautiful soup to parse text from HTML elements. The first element is:

> 'obit_age_data = result.find('div', class_='PersonAge').text'

The second element is:

> 'obit_text = result.find('div', class_='obitText').text'

There are several methods used to parse years and age values from these text blurbs.

The code only looks for people with death years > 2017. This is project specific and can be adjusted in the code.
