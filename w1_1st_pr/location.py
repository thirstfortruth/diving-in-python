import requests

def get_location_info():
    try:
        return requests.get("htps://jsonplaceholder.typicode.com/posts/1").json()
    except requests.exceptions.InvalidSchema:
        print("failed")


if __name__ == "__main__":
    print(get_location_info())

