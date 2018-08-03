import json
import requests
import os
import logging

from typing import Dict

logger = logging.getLogger(__name__)

db_url = "https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD"
expected_size = 82501846
path_db_local = "./db.json"


def asd():
    # with open("./rows.json")
    pass


def download_if_file_is_missing():
    if not os.path.exists(path_db_local):
        logger.info("Local cache is missing. Loading from internet")
        data_string = download_db()
        logger.info("Saving data to cache '{}'".format(path_db_local))
        with open(path_db_local, "w") as f:
            json.dump(data_string, f)

    else:
        logger.info("Loading data from local cache '{}'".format(path_db_local))

    if os.stat(path_db_local).st_size != expected_size:
        raise Exception("Size of the cached is incorrect. Data may be corrupted.")

    with open(path_db_local) as f:
        data_json = json.load(f)

    print(len(data_json))


def download_db() -> Dict:
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

    download_if_file_is_missing()
