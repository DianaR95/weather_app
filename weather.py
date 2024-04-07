import json

import emoji
import requests


def get_current_weather(url:str, key: str, city: str = "Bucharest"):
    try:
        response = requests.get(url + city, headers={"key": key})
        if response.status_code == 200:
            weather_dict = json.loads(response.text)
            if weather_dict.get('error'):
                raise Exception("Orasul nu exista in baza noastra de date")
            return weather_dict
        else:
            raise Exception(f"Something wrong with the api \n"
                            f"Code: {response.status_code}\n"
                            f"Message: {response.text}")
    except Exception as e:
        print(e)


def summary_weather(url: str, key: str, city: str = "Bucharest"):
    try:
        response = requests.get(url + city, headers={"key": key})
        if response.status_code == 200:
            curr_weather_dict = json.loads(response.text)
            local_info = curr_weather_dict['current']['condition']['text']
            local_temp = curr_weather_dict['current']['temp_c']
            return local_info, local_temp

    except Exception as e:
        print(e)

    finally:
        if local_temp >= 25:
            print(emoji.emojize(f"Outside is :fire:, there are {local_temp} C degrees."))
        elif local_temp <25:
            print(emoji.emojize(f"Outside is :check_mark:, there are {local_temp} C degrees."))
        else:
            print("Couldn't find data about weather.")

        if "sun" or "clear" in local_info:
            print(emoji.emojize(f"Weather is :sun:, can go for a walk."))
        elif "cloud" in local_info:
            print(emoji.emojize(f"Weather is :cloud:, better get an :closed_umbrella:."))
        elif "rain" in local_info:
            print(emoji.emojize(f"Weather is :cloud_with_lightning_and_rain:, you definetly need an :closed_umbrella:."))
        else:
            print("Couldn't find data about weather.")
