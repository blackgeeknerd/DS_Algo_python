import http.client

conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")

payload = "{}"

conn.request("GET", "/v0/topstories.json?print=pretty", payload)

res = conn.getresponse()
data = res.read()
print(data)