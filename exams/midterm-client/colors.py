import requests
import json

def main():
    request_data = requests.get('https://reqres.in/api/unknown')
    data = json.loads(request_data.text)
    print(data["data"][0]["name"])
    print(data["data"][1]["name"])

if __name__ == "__main__":
    main()
