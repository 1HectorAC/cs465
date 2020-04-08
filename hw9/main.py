import requests
import json
import time

def make_request(url):
    request = requests.get(url)
    posts = json.loads(request.text)
    return posts[0]

def main():
    url = "http://localhost:8080/api/posts"
    print("Acessing posts on: " + url)
    while True:
        request_info = make_request(url)
        print("Version:", request_info["version"])
        print("   vote_count:", request_info["vote_count"])
        time.sleep(3)

if __name__ == "__main__":
    main()
