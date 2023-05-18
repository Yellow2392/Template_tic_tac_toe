import http.client

conn = http.client.HTTPConnection("127.0.0.1",5001)

conn.request("GET","\players")

response = conn.getresponse()

print("Status:", response.status)

print("Response: ", response.read().decode())

conn.close()