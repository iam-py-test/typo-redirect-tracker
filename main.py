import os
import requests
from urllib.parse import urlparse

typodomains = ["gogle.net","youtuba.com","discordap.com","discordapp.cam"]
safeends = ["google.com","youtube.com","discordapp.com","discord.com","duckduckgo.com","www.godaddy.com"]

redirecturls = []
enddomains = []
alivedomains = []

for domain in typodomains:
  try:
    req = requests.get("http://{}".format(domain),headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5","DNT":"1"})
    if urlparse(req.url).netloc not in safeends:
      alivedomains.append(domain)
      enddomains(urlparse(req.url).netloc)
      for reddomain in req.history:
        redirecturls.append(reddomain)
      redirecturls.append(req.url)
  except:
    print("Domain {} is dead".format(domain))

redirecturlsout = open("redirecturls.txt","w")
enddomainsout = open("enddomains.txt","w")
alivedomainsout = open("alivedomains.txt","w")
for entry in redirecturls:
  redirecturlout.write("{}\n".format(entry))
for entry in enddomains:
  enddomainsout.write("{}\n".format(entry))
for entry in alivedomains:
  alivedomainsout.write("{}\n".format(entry))
redirecturlout.close()
enddomainsout.close()
alivedomainsout.close()
print("All done")
