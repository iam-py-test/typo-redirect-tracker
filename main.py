import requests
from urllib.parse import urlparse

typodomains = ["gogle.net","youtuba.com","discordap.com","yotube.com","yutube.com","googheusercontent.com","wyoutube.com","gmsail.com","gmailgmail.com","gmailc.om","googlesite.ws","gooooooooogle.com","pay-pal.club","githu.com","fecebook.com","youutube.com","casebook.com","dacebook.com","gacebook.com","forums.malwarebytes.co","bleepingxomputer.com","bleepingvomputer.com"]
safeends = ["google.com","youtube.com","discordapp.com","discord.com","duckduckgo.com","www.godaddy.com","googleusercontent.com","googleanalytics.com","googletagmanager.com","gmail.com","malwarebytes.com","gstatic.com","jquery.com","malwarebytes.org","paypal.com","github.com","microsoft.com","raw.githubusercontent.com","githubusercontent.com","facebook.com","www.facebook.com","forums.malwarebytes.com","bleepingcomputer.com"]

redirecturls = []
enddomains = []
alivedomains = []

for domain in typodomains:
  try:
    req = requests.get("http://{}".format(domain),headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.5","DNT":"1"})
    enddomain = urlparse(req.url).netloc
    if enddomain not in safeends:
      alivedomains.append(domain)
      enddomains.append(enddomain)
      for reddomain in req.history:
        redirecturls.append(reddomain.url)
      redirecturls.append(req.url)
  except Exception as err:
    print("Domain {} is dead".format(domain))
    print(err,domain)

redirecturlsout = open("redirecturls.txt","w")
enddomainsout = open("enddomains.txt","w")
alivedomainsout = open("alivedomains.txt","w")
for entry in redirecturls:
  redirecturlsout.write("{}\n".format(entry))
for entry in enddomains:
  enddomainsout.write("{}\n".format(entry))
for entry in alivedomains:
  alivedomainsout.write("{}\n".format(entry))
redirecturlsout.close()
enddomainsout.close()
alivedomainsout.close()
print("All done")
