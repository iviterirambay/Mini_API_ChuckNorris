import requests

url="https://api.chucknorris.io/jokes/categories"

json_data=requests.get(url).json()
print(json_data)

while True:
    search=input("Choose the joke category: ")
    if search == "q" or search == "quit":
        break
    url2="https://api.chucknorris.io/jokes/random?category={}".format(search)
    json_jokes=requests.get(url2).json()
    #print(json_jokes)
    print("============================================================")
    print("Here goes the joke...\n",json_jokes["value"])