import requests
req=requests.get('https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue')
#check status code
print(req)
#print contecnt of request
print(req.content)
