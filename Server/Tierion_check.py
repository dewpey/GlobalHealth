import urllib.parse
import urllib.request

url = 'https://api.tierion.com/v1/records/NSY0Dng9qkyRgEB9QmqQKw'
url_1 = 'https://api.tierion.com/v1/records/cOsnFKqw1EKmYK3NMijTJg'



headers = { "X-Username" : "blurjoe@gmail.com" ,  "X-Api-Key" : "X0dvxIiNXXq5k7RBNYDmPrVoxEeJ+Y+umsUMS7FcgWk=", "content-type": "application/json" }
values = {}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
the_page= None
with urllib.request.urlopen(req) as response:
   the_page = response.read()

print(the_page)
