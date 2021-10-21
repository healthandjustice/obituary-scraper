import requests
import csv

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "cookie": '_gcl_au=1.1.579528899.1614204981; hubspotutk=a6f04bbaf2d0bdbd2827e78f2d97a0b1; usprivacy=1---; _hjid=25562147-fca7-497c-a335-c1b34ca43fd2; AMCV_3B6E35F15A82BBB00A495D91@AdobeOrg=1585540135|MCIDTS|18691|MCMID|13735329281857089950375566803053947169|MCAAMLH-1615436264|7|MCAAMB-1615436264|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1614838664s|NONE|MCAID|300DAFD6E0D3C18C-40000744B05068DA|MCCIDH|519030287|vVersion|4.4.0; _aimtellSubscriberID=26ed008b-9b8d-cfa1-7f99-e4f97d3e83dd; __gads=ID=1a44e8b4e6c8ca8b:T=1614831467:S=ALNI_MZc1FKCfFdIqr9y9IbVyVn4iJiY8g; _admrla=2.0-405125cd-5c0e-caec-b3fb-6549b0f86924; fpestid=xPkaeKLRAOBHUOYmVkCRgMchoVcwV_YUTGf1PenUBvF_LPMEym7hQyRTuKVnNumfkZQ6Uw; adcloud={"_les_v":"y,legacy.com,1614838647"}; _sp_id.218c=40881d7453926ced.1614831464.3.1614836848.1614834134; optimizelyEndUserId=oeu1616518153674r0.7061804611129419; __cfduid=db14d7e050bca4932ef5eb213538602921617045302; _gid=GA1.2.1461330368.1618427074; _ga=GA1.2.806206518.1614204981; _awl=2.1618427570.0.4-a94e1692-405125cd5c0ecaecb3fb6549b0f86924-6763652d75732d6561737431-60773eb2-1; spid.7b56=c89c1479-83ad-44e9-bdce-7e7b099a6143.1618427570.1.1618427591.1618427570.e45c77a2-461d-47e0-bdea-984fcb992c36; _ga_G2BL49024K=GS1.1.1618427569.1.1.1618427657.60; AMP_TOKEN=$NOT_FOUND; __qca=P0-966112119-1618588377459; __hstc=217861641.a6f04bbaf2d0bdbd2827e78f2d97a0b1.1614204982318.1618586911128.1618588377751.22; __hssrc=1; cf_chl_prog=a10; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+16+2021+12:17:54+GMT-0400+(Eastern+Daylight+Time)&version=6.14.0&hosts=&landingPath=NotLandingPage&groups=C0003:1,C0001:1,C0002:1,C0004:1,BG11:1&AwaitingReconsent=false&geolocation=US;NC; OptanonAlertBoxClosed=2021-04-16T16:17:54.301Z; cf_clearance=db7c26f0f14d22e13d062bc80f5b836760b44c34-1618590308-0-250; __hssc=217861641.13.1618588377751',
    "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
}

nc_releases = list(csv.reader(open('./data/test_nc_releases.csv')))

for person in nc_releases[1:]:
    print(person[1] + ', ' + person[2])
    URL = 'https://www.legacy.com/search?countryId=366899&countryUrl=united-states-of-america&dateRange=All&firstName=' + person[2] + '&lastName=' + person[1] + '&stateAbbrev=NC&stateId=366845&stateUrl=north-carolina'
    print(URL)
    page = requests.get(URL, headers=headers)
    print(page)