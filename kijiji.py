class kijiji:
    import mechanize
    import json
    global nav
    global json
    nav = mechanize.Browser()
    nav.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    def __init__(self,cfg):
        self.base_url = cfg['base_url']
        self.login_url= cfg['login_url']
        self.ads_url  = cfg['ads_url']
        self.username = cfg['username']
        self.password = cfg['password']
    
    def login(self):
        global nav
        nav.open(self.base_url + self.login_url)
        nav.select_form(id='login-form')
        nav.form['emailOrNickname']=self.username
        nav.form['password']=self.password
        nav.submit()

    def get_ads(self):
        global nav
        global json
        nav.open(self.base_url + self.ads_url)
        return json.loads(nav.response().read())['ads']
