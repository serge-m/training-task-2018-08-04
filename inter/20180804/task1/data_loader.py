import json
import requests
import os
import logging

from typing import Dict

logger = logging.getLogger(__name__)

"""
Dataset:
https://catalog.data.gov/dataset/air-quality-measures-on-the-national-environmental-health-tracking-network
"""

path_db_local = "./db.json"


def load_data_to_dictionary(db_url="https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD",
                            expected_size=82501846):
    if not os.path.exists(path_db_local):
        _download_to_file(db_url, path_db_local)
    else:
        logger.info("Loading data from local cache '{}'".format(path_db_local))

    if expected_size is not None and os.stat(path_db_local).st_size != expected_size:
        raise Exception("Size of the cached is incorrect. Data may be corrupted.")

    with open(path_db_local) as f:
        data_json = json.load(f)

    return data_json


def _download_to_file(db_url: str, path_db_local: str):
    logger.info("Local cache is missing. Loading from the internet")
    data_json = _load_from_internet(db_url)
    logger.info("Saving data to cache '{}'".format(path_db_local))
    with open(path_db_local, "w") as f:
        json.dump(data_json, f)


def _load_from_internet(db_url: str) -> Dict:
    logger.info("Downloading database from '{}'...".format(db_url))
    response = requests.get(db_url)
    response.raise_for_status()
    result = response.json()
    logger.info("Downloading successful")
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s|%(name)-20.20s|%(levelname)-5.5s|%(message)s")
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    load_data_to_dictionary()
