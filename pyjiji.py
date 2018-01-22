import yaml
from kijiji import kijiji

with open("config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

k=kijiji(cfg)
k.login()
ads = k.get_ads()

for ad in ads:
    print ad + " : " + ads[ad]['title']
ad_id = raw_input("enter the ad id to show")
print ads[ad_id]
