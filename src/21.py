import os
import requests

def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join("myproject", "downloaded_file.txt"), "wb") as file:
            file.write(response.content)
        print(f"File downloaded to: {os.path.join('myproject', 'downloaded_file.txt')}")
    else:
        print("Failed to download the file.")

if __name__ == "__main__":
    url = "https://example.com/downloaded_file.zip"
    download_file(url)
