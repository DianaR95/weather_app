import json

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

