import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"


def fetch_random_user_freeapi():
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"][
            "username"
        ]  # username is inside data->login->username
        country = user_data["location"]["country"]
        return user_name, country
    else:
        # raise is to raise a error
        raise Exception("Failed to fetch userdata")


def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"username: {username}\n country: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
