import json
import requests

import constants


def cache_result_to_json(data: dict) -> None:
    with open("cache.json", "a") as f:
        to_dump = {
            data["bin"]: data
        }
        json.dump(to_dump, f, indent=4, ensure_ascii=False)


def get_data(biniin: str) -> dict:
    try:
        with open("cache.json", "r") as f:
            cache = json.load(f)
            if biniin in cache.keys():
                return cache[biniin]
    except FileNotFoundError as e:
        ...

    params = {"bin": biniin, "lang": "ru"}
    response = requests.get(constants.URL, params=params)
    response.raise_for_status()
    obj = response.json()["obj"]
    cache_result_to_json(obj)

    return obj


def format_response(obj: dict, field_names: list[str] = None) -> dict:
    if not field_names:
        return obj
    result = {
        k: v
        for k, v in obj.items()
        if k in field_names
    } if field_names else obj
    return result
