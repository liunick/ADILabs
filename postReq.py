import urllib.request

def getRes(url, vals):
    newVals = urllib.parse.urlencode(vals)
    data = newVals.encode('ascii')
    conn = urllib.request.Request(url, data)
    res = urllib.request.urlopen(conn)
    print (res.read())

urlADI = "http://apply.to.labs.adicu.com/2016"
valsADI = {"javascript": "3", "python": "4", "uni": "nl2523", "url": "https://gist.github.com/liunick/dfd61a2702d1c78cc6b9", "hours": "0.4", "song": "Never be Like You - Flume"}
getRes(urlADI, valsADI)
