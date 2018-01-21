import mechanize
import json
import yaml

with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

base_url="https://www.kijiji.ca"
login_url="/t-login.html"
ads_url="/my/ads?format=sparse"
ad_view_url="/v-view-details.html?adId=%s"
username= cfg['username']
password= cfg['password']
nav=mechanize.Browser()
nav.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


def login():
    url = base_url + login_url
    nav.open(url)
    nav.select_form(id='login-form')
    nav.form['emailOrNickname']=username
    nav.form['password']=password
    nav.submit()

def fetch_ads():
    url = base_url + ads_url
    nav.open(url)
    return json.loads(nav.response().read())['ads']

def show_ad(id):
    url = base_url + ad_view_url % id
    nav.open(url)
    print nav.response().read()

login()
ads = fetch_ads()

for ad in ads:
    print ad + " : " + ads[ad]['title']
ad_id = raw_input("enter the ad id to show")
print ads[ad_id]
