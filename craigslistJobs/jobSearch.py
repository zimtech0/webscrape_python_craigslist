# import get to call a get request on the craigslist site

from bs4 import BeautifulSoup
# brings python  libraries
import requests
import pprint
import re
import urllib3
import urllib.request 
#from urllib.request import Request, urlopen#attempt to handle errors
#from urllib.error import URLError#aatempt to handle errors
# array of craigslist job website
urls = [
        'https://albuquerque.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://atlanta.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://austin.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://baltimore.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://boston.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://charlotte.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://charleston.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://chicago.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://cleveland.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://columbia.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://dallas.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://detroit.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://denver.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://fayetteville.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://greensboro.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://hartford.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://houston.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://indianapolis.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://jacksonville.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://lasvegas.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://losangeles.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://inlandempire.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://memphis.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://miami.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://milwaukee.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://minneapolis.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://newlondon.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://neworleans.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://newyork.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://philadelphia.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://norfolk.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://phoenix.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://portland.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://raleigh.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://richmond.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://saltlakecity.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://sanantonio.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://savannah.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://seattle.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://sfbay.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://stcloud.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://tucson.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://washingtondc.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        'https://wilmington.craigslist.org/search/jjj?excats=15-1-10-1-1-19-2-3-2-3-2-2-14-25-25-1-1-1-1-1-1&is_telecommuting=1&employment_type=1&employment_type=2&employment_type=3',
        ]


# for loop to go through multiple craigslist sites
def findJobs():
    jobTitle = 'Job Title : '
    postDate = 'Post Date : '
    postLink = 'Link : '
    postLocation = 'Craigslist Site : '
    postDescription = ' Job Description :'
    resultCount= 'Count :'
    for url in urls:
    # getting webpage, creating a response object.
        response = requests.get(url)
    #response content pass to bs4
        soup = BeautifulSoup(response.content, "html.parser",)  
    #finds all a tags and specific class that contains craiglist jobs ads
        titles = soup.find_all("a", class_="result-title hdrlnk")
    #finds all time tags that contain date time of post
        post_dates = soup.find("time", class_="result-date")
    #variable that passes date time info
        #post_datetime = post_dates['datetime']
    #loops through titles
        number = 0
        for title in titles:
    # create variable for post urls
          post_href =  title.get('href')   
    #open job post href
          post_details = urllib.request.urlopen(post_href).read() 
    #read post details
          soup_post_details = BeautifulSoup(post_details, "html.parser") 
    #find job description from section tag
          job_description=soup_post_details.find("section",id="postingbody")    
     #removes divs     
        #job_description.div.clear()     
    #prints craiglist city site label
          print("\n\n",postLocation,soup.title.string)
    #prints job title
          print(resultCount,number,jobTitle,title.text)
          number = number +1
    #prints date
          #print(postDate,post_datetime)
    #for link to live post
          print(postLink,title.get('href'))
    #print job decscription    
          print("\n",postDescription,job_description)
    
def main():
    findJobs()

main()
