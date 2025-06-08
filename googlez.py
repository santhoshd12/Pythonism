import requests
apikey="your api key"

cx = "your cx"

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key" : apikey,
        "cx" : cx,
        "q" : query
    }

    response = requests.get(url=url,params=params)
    result = response.json()

    print("Status Code:", response.status_code)
    items = result.get("items", [])
    for item in items:
        title = item.get("title", "No title")
        print(title)
    # print(result["items"][0])


google_search("Drone delivery system")
