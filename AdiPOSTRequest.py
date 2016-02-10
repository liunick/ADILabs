import httplib, urllib
adiParamThing = urllib.urllengcode({
    "javascript" : '3',
    "python" : '4',
    "uni" : 'nl2523',
    "url" :
    'hours' : '0.3',
    'song' : '',
    })

adiConnThing = httplib.HTTPConnection("http://apply.to.labs.adicu.com/2016");
adiConnThing.request("POST", "http://apply.to.labs.adicu.com/2016", adiParamThing);
adiResponseFromThing = adiConnThing.getresponse();
print adiResponse.status, response.reason;
adiConnThing.close();
