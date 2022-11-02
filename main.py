import requests, json



data = {
    "title": "A new Post",
    "content": "Ojoshu"
}

response = requests.post("http://127.0.0.1:8000/create/", data=json.loads(data))

print(response.json())