import csv
import requests
import time
import os
from datetime import datetime
import numpy
from bs4 import BeautifulSoup
import re

# today = datetime.now().strftime("%d-%m-%y-%H:%M")
# os.mkdir("./output/" + today)

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "cookie": '__gcl_au=1.1.579528899.1614204981; hubspotutk=a6f04bbaf2d0bdbd2827e78f2d97a0b1; usprivacy=1---; _hjid=25562147-fca7-497c-a335-c1b34ca43fd2; AMCV_3B6E35F15A82BBB00A495D91@AdobeOrg=1585540135|MCIDTS|18691|MCMID|13735329281857089950375566803053947169|MCAAMLH-1615436264|7|MCAAMB-1615436264|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1614838664s|NONE|MCAID|300DAFD6E0D3C18C-40000744B05068DA|MCCIDH|519030287|vVersion|4.4.0; _aimtellSubscriberID=26ed008b-9b8d-cfa1-7f99-e4f97d3e83dd; __gads=ID=1a44e8b4e6c8ca8b:T=1614831467:S=ALNI_MZc1FKCfFdIqr9y9IbVyVn4iJiY8g; _admrla=2.0-405125cd-5c0e-caec-b3fb-6549b0f86924; fpestid=xPkaeKLRAOBHUOYmVkCRgMchoVcwV_YUTGf1PenUBvF_LPMEym7hQyRTuKVnNumfkZQ6Uw; adcloud={"_les_v":"y,legacy.com,1614838647"}; _sp_id.218c=40881d7453926ced.1614831464.3.1614836848.1614834134; optimizelyEndUserId=oeu1616518153674r0.7061804611129419; __cfduid=db14d7e050bca4932ef5eb213538602921617045302; _ga=GA1.2.806206518.1614204981; _awl=2.1618427570.0.4-a94e1692-405125cd5c0ecaecb3fb6549b0f86924-6763652d75732d6561737431-60773eb2-1; spid.7b56=c89c1479-83ad-44e9-bdce-7e7b099a6143.1618427570.1.1618427591.1618427570.e45c77a2-461d-47e0-bdea-984fcb992c36; _ga_G2BL49024K=GS1.1.1618427569.1.1.1618427657.60; __qca=P0-966112119-1618588377459; __hssrc=1; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+16+2021+12:17:54+GMT-0400+(Eastern+Daylight+Time)&version=6.14.0&hosts=&landingPath=NotLandingPage&groups=C0003:1,C0001:1,C0002:1,C0004:1,BG11:1&AwaitingReconsent=false&geolocation=US;NC; OptanonAlertBoxClosed=2021-04-16T16:17:54.301Z; AMP_TOKEN=$NOT_FOUND; _gid=GA1.2.948075377.1619037483; cf_chl_prog=a11; cf_clearance=2b8bef404b9cb38c0f90be316b29ef6db7c5669d-1619039804-0-250; __hstc=217861641.a6f04bbaf2d0bdbd2827e78f2d97a0b1.1614204982318.1619037483331.1619039805578.24; __hssc=217861641.1.1619039805578',
    "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "pragma": "no-cache",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

nc_releases = list(csv.reader(open('./data/all_random_1.csv')))
# nc_releases = list(csv.reader(open('./data/test_nc_releases.csv')))

legacy_dot_com_results = [['Release_First_Name', 'Release_Last_Name', 'Release_Middle_Initial', 'Release_Birthdate', 'Release_Date', 'Obituary_Found', 'Obituary_First_Name', 'Obituary_Middle_Name', 'Obituary_Last_Name', 'Obituary_Date_Info', 'Obituary_Death_Age', 'Obituary_Birth_Year', 'Obituary_Death_Year', 'Obituary_Location', 'Obituary_Text', 'Obituary_Link']]
counter = 0

for person in nc_releases[1:]:
    print(person[1] + ', ' + person[2])
    URL = 'https://www.legacy.com/search?countryId=366899&countryUrl=united-states-of-america&dateRange=All&firstName=' + person[2] + '&lastName=' + person[1] + '&stateAbbrev=NC&stateId=366845&stateUrl=north-carolina'
    print(URL)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Pull out element where person level data is contained
    results = soup.find_all('div', class_='PersonItem')

    # Get birthyear from nc releases
    if int(person[7].split('/')[2]) < 10:
        release_birth_year = '20' + person[7].split('/')[2]
    else:
        release_birth_year = '19' + person[7].split('/')[2]

    print(page)

    # Download
    # open("./output/" + today + "/" + person[2] + person[1] + ".html", "w").write(page.text)

    # No results then just create a row with only the release data and blank obiturary data
    if not results:
        obit_text = ''
        obit_age = ''
        obit_location = ''
        obit_name = ''
        obit_link = ''
        obit_true_age = None
        new_row = [person[2], person[1], person[3], person[7], person[20], 'No']
        legacy_dot_com_results.append(new_row)
    
    # Otherwise give all obituary variables a empty value
    for result in results:
        obit_text = ''
        obit_age = ''
        obit_true_age = None
        obit_location = ''
        obit_name = ''
        obit_link = ''
        obit_birth_year = 0
        obit_death_year = 0

        # if results[0].find('div', class_='obitText') is not None:
        #     obit_text = results[0].find('div', class_='obitText').text
        # if results[0].find('div', class_='PersonAge') is not None:
        #     obit_age = results[0].find('div', class_='PersonAge').text
        # if results[0].find('div', class_='PersonLocation') is not None:
        #     obit_location = results[0].find('div', class_='PersonLocation').text
        # if results[0].find('div', class_='PersonName') is not None:
        #     obit_name = results[0].find('div', class_='PersonName').text
        # if results[0].find('div', class_='personDetails') is not None:
        #     obit_link = results[0].find('div', class_='personDetails').find('a', href=True)['href']

        # Use beautiful soup to search through PersonItem and extract
        # text / values from divs
        if result.find('div', class_='obitText') is not None:
            obit_text = result.find('div', class_='obitText').text
        if result.find('div', class_='PersonAge') is not None:
            obit_age_data = result.find('div', class_='PersonAge').text
        if result.find('div', class_='PersonLocation') is not None:
            obit_location = result.find('div', class_='PersonLocation').text
        if result.find('div', class_='PersonName') is not None:
            obit_name = result.find('div', class_='PersonName').text
        if result.find('div', class_='personDetails') is not None:
            obit_link = result.find('div', class_='personDetails').find('a', href=True)['href']

        # Get obit death year
        if (len(obit_age_data.split(' - ')) == 2):
            obit_death_year = obit_age_data.split(' - ')[1]
            obit_birth_year = obit_age_data.split(' - ')[0][-4:]
            print(obit_birth_year)
            if len(obit_death_year) > 4:
                obit_death_year = obit_death_year[-4:]
        elif len(re.findall('(\d{4})', obit_text)) > 0:
            years_in_text = re.findall('(\d{4})', obit_text)
            for year in years_in_text:
                if int(year) >= 1990 and int(year) <= 2021:
                    obit_death_year = int(year)
                    break
            for year in years_in_text:   
                if int(year) > 1910 and int(year) <= 2005:
                    obit_birth_year = int(year)
                    break
        else:
            obit_death_year = None
            obit_birth_year = None
        
        if obit_death_year == 0:
            obit_death_year = None
        if obit_birth_year == 0:
            obit_birth_year = None
        
        # Get Obit Age
        if (len(obit_age_data.split('Age ')) == 2):
            obit_true_age = obit_age_data.split('Age ')[1][0:2]
        elif (len(obit_text.split('Age ')) == 2):
            obit_true_age = obit_text.split('Age ')[1][0:2]
        elif len(re.findall('(,\s\d{2},)', obit_text)) > 0:
            ages_in_text = re.findall('(,\s\d{2},)', obit_text)
            for age in ages_in_text:
                clean_age = age.replace(",", "")
                clean_age = clean_age.replace(" ", "")
                if int(clean_age) >= 16:
                    obit_true_age = int(clean_age)
                    break
        elif len(re.findall('(\s\d{2},?!\s,\d{4})', obit_text)) > 0:
            ages_in_text = re.findall('(\s\d{2},?!\s,\d{4})', obit_text)
            for age in ages_in_text:
                if int(age.rstrip(',')) >= 16:
                    obit_true_age = int(age.rstrip(','))
                    break
        if obit_death_year is not None and obit_birth_year is not None:
            obit_true_age = int(obit_death_year) - int(obit_birth_year)
        
        # Fill in birth year if we have death year and age
        if obit_death_year is not None and obit_true_age is not None and obit_birth_year is None:
            obit_birth_year = int(obit_death_year) - int(obit_true_age)
        
        # Split obit_name
        obit_first_name = ''
        obit_middle_name = ''
        obit_last_name = ''
        exploded_name = obit_name.split(' ')
        if (len(exploded_name) == 2):
            obit_first_name = exploded_name[0]
            obit_last_name = exploded_name[1]
        elif (len(exploded_name) == 3):
            obit_first_name = exploded_name[0]
            obit_last_name = exploded_name[2]
            obit_middle_name = exploded_name[1]
        elif (len(exploded_name) == 1):
            obit_first_name = exploded_name[0]
        else:
            obit_first_name = obit_name

        new_row = [person[2], person[1], person[3], person[7], person[20], 'Yes', obit_first_name, obit_middle_name, obit_last_name, obit_age_data, obit_true_age, obit_birth_year, obit_death_year, obit_location, obit_text, obit_link]

        # We are matching based on Name and Birth Year
        if release_birth_year in obit_age_data or release_birth_year in obit_text or int(release_birth_year if release_birth_year is not None else 0) == int(obit_birth_year if obit_birth_year is not None else 0):
            legacy_dot_com_results.append(new_row)
            break
        elif result == results[-1]:
            for backup in results:
                obit_text = ''
                obit_age_data = ''
                obit_true_age = None
                obit_location = ''
                obit_name = ''
                obit_link = ''
                obit_birth_year = 0
                obit_death_year = 0

                if backup.find('div', class_='obitText') is not None:
                    obit_text = backup.find('div', class_='obitText').text
                if backup.find('div', class_='PersonAge') is not None:
                    obit_age_data = backup.find('div', class_='PersonAge').text
                if backup.find('div', class_='PersonLocation') is not None:
                    obit_location = backup.find('div', class_='PersonLocation').text
                if backup.find('div', class_='PersonName') is not None:
                    obit_name = backup.find('div', class_='PersonName').text
                if backup.find('div', class_='personDetails') is not None:
                    obit_link = backup.find('div', class_='personDetails').find('a', href=True)['href']

                # Get obit death year
                if (len(obit_age_data.split(' - ')) == 2):
                    obit_death_year = obit_age_data.split(' - ')[1]
                    obit_birth_year = obit_age_data.split(' - ')[0][-4:]
                    print(obit_birth_year)
                    if len(obit_death_year) > 4:
                        obit_death_year = obit_death_year[-4:]
                elif len(re.findall('(\d{4})', obit_text)) > 0:
                    years_in_text = re.findall('(\d{4})', obit_text)
                    for year in years_in_text:
                        if int(year) >= 1990 and int(year) <= 2021:
                            obit_death_year = int(year)
                            break
                    for year in years_in_text:   
                        if int(year) > 1910 and int(year) <= 2005:
                            obit_birth_year = int(year)
                            break
                else:
                    obit_death_year = None
                    obit_birth_year = None

                if obit_death_year == 0:
                    obit_death_year = None
                if obit_birth_year == 0:
                    obit_birth_year = None
                
                # Go to next if obit death year is < 2017 
                if obit_death_year is not None:
                    if int(obit_death_year) < 2017:
                        continue
                elif obit_death_year is None and obit_birth_year is None:
                    continue
                elif backup == results[-1]:
                    break

                # Get Obit Age
                if (len(obit_age_data.split('Age ')) == 2):
                    obit_true_age = obit_age_data.split('Age ')[1][0:2]
                elif (len(obit_text.split('Age ')) == 2):
                    obit_true_age = obit_text.split('Age ')[1][0:2]
                elif len(re.findall('(,\s\d{2},)', obit_text)) > 0:
                    ages_in_text = re.findall('(,\s\d{2},)', obit_text)
                    for age in ages_in_text:
                        clean_age = age.replace(",", "")
                        clean_age = clean_age.replace(" ", "")
                        if int(clean_age) >= 16:
                            obit_true_age = int(clean_age)
                            break
                elif len(re.findall('(\s\d{2},?!\s,\d{4})', obit_text)) > 0:
                    ages_in_text = re.findall('(\s\d{2},?!\s,\d{4})', obit_text)
                    for age in ages_in_text:
                        if int(age.rstrip(',')) >= 16:
                            obit_true_age = int(age.rstrip(','))
                            break
                if obit_death_year is not None and obit_birth_year is not None:
                    obit_true_age = int(obit_death_year) - int(obit_birth_year)

                # Fill in birth year if we have death year and age
                if obit_death_year is not None and obit_true_age is not None and obit_birth_year is None:
                    obit_birth_year = int(obit_death_year) - int(obit_true_age)

                # Split obit_name
                obit_first_name = ''
                obit_middle_name = ''
                obit_last_name = ''
                exploded_name = obit_name.split(' ')
                if (len(exploded_name) == 2):
                    obit_first_name = exploded_name[0]
                    obit_last_name = exploded_name[1]
                elif (len(exploded_name) == 3):
                    obit_first_name = exploded_name[0]
                    obit_last_name = exploded_name[2]
                    obit_middle_name = exploded_name[1]
                elif (len(exploded_name) == 1):
                    obit_first_name = exploded_name[0]
                else:
                    obit_first_name = obit_name

                new_row = [person[2], person[1], person[3], person[7], person[20], 'Yes',  obit_first_name, obit_middle_name, obit_last_name, obit_age_data, obit_true_age, obit_birth_year, obit_death_year, obit_location, obit_text, obit_link]
                legacy_dot_com_results.append(new_row)

                # We are matching based on Name and Birth Year
                if release_birth_year in obit_age_data or release_birth_year in obit_text or int(release_birth_year if release_birth_year is not None else 0) == int(obit_birth_year if obit_birth_year is not None else 0):
                    legacy_dot_com_results.append(new_row)
                    break

    # delays = [7, 4, 6, 2, 3, 9]
    # delay = numpy.random.choice(delays)
    # time.sleep(delay)


    # if len(results) > 0:
    #     # print(results[0].prettify())
    #     obit_text = ''
    #     obit_age = ''
    #     obit_location = ''
    #     obit_name = ''
    #     if results[0].find('div', class_='obitText') is not None:
    #         obit_text = results[0].find('div', class_='obitText').text
    #     if results[0].find('div', class_='PersonAge') is not None:
    #         obit_age = results[0].find('div', class_='PersonAge').text
    #     if results[0].find('div', class_='PersonLocation') is not None:
    #         obit_location = results[0].find('div', class_='PersonLocation').text
    #     if results[0].find('div', class_='PersonName') is not None:
    #         obit_name = results[0].find('div', class_='PersonName').text

    #     new_row = [person[2], person[1], 'Yes', obit_name, obit_age, obit_location, obit_text]
    #     legacy_dot_com_results.append(new_row)
    # break
    # if counter == 1001:
    #     break
    # counter = counter + 1

with open("./output/all_random_1_out.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(legacy_dot_com_results)

# with open('./data/filtered_nc_releases_1-10-20.csv') as data:
#     nc_releases = csv.reader(data)
#     for row in nc_releases:
#         URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
#         page = requests.get(URL)
#         print(row)