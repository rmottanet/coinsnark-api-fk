# -*- coding: utf-8 -*-
import time
import requests

def fetch_data(url, max_retries=3, delay=5, headers=None):
    retries = 0
    while retries < max_retries:
        try:
            if headers:
                response = requests.get(url, headers=headers)
            else:
                response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.HTTPError:
            retries += 1
            if retries < max_retries:
                print(f"Retrying after {delay} seconds...")
                time.sleep(delay)
            else:
                raise RuntimeError("Max retries exceeded. Unable to fetch data.")
