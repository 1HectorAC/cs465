import click
import requests

def get_request(id):
    url = "https://jsonplaceholder.typicode.com/posts?userId=" + id
    response = requests.get(url)
    print(response.text)

@click.command()
@click.argument("id", type=click.STRING)

def main(id):
    get_request(id)


if __name__ == "__main__":
    main()
