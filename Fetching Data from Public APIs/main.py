import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        joke_data = response.json()
        print("Full JSON response", joke_data)
        return f'{joke_data["setup"]} - {joke_data["punchline"]}'
    except requests.RequestException:
        print("Failed to retrieve a joke!")
        return None


def main():
    print("Welcome to random joke generator!")

    while True:
        user_input = input("Press Enter to get a new joke, type 'q' to exit: ").lower()

        if user_input == 'q':
            print("Goodbye!")
            break

        joke = get_random_joke()
        if joke:
            print(joke)
        else:
            print("No joke available. Try again later.")


if __name__ == "__main__":
    main()
