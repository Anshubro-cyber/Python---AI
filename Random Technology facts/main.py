import requests
url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to retrieve a fact.")

while True:
    input("Press Enter to get a random fact (or type 'exit' to quit): ")
    if input().lower() == 'exit':
        break
    get_random_fact()