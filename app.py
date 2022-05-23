import requests
from humanfriendly import format_timespan
import dateparser
import datetime
import time
import logging

from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def bold(input_text):
    # This function converts normal characters to their bold Unicode counterparts
    # so they can be used to format tweets.

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    bold_chars = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

    output = ""

    for character in input_text:
        if character in chars:
            output += bold_chars[chars.index(character)]
        else:
            output += character

    return output


def main():
    # Hook into the twitter api using the create_api method from config.py
    api = create_api()

    # determine an initial TimeOffset
    TimeOffset = str(datetime.datetime.now())

    logger.info("Beginning WR Search...")
    logger.info(f"Initial Time: {TimeOffset}.")

    # Start the main loop
    while True:
        # Define the parameters we will use to query the KZ api
        # Note because the API is weird, we have to explicitly define the mode otherwise we miss results
        skz_parameters = {
            "has_teleports": False,
            "place_top_at_least": 1,
            "stage": 0,
            "modes_list_string": "kz_simple",
            "created_since": TimeOffset,
            "tickrate": 128,
        }
        kzt_parameters = {
            "has_teleports": False,
            "place_top_at_least": 1,
            "stage": 0,
            "modes_list_string": "kz_timer",
            "created_since": TimeOffset,
            "tickrate": 128,
        }
        vnl_parameters = {
            "has_teleports": False,
            "place_top_at_least": 1,
            "stage": 0,
            "modes_list_string": "kz_vanilla",
            "created_since": TimeOffset,
            "tickrate": 128,
        }
        # Update the TimeOffset
        TimeOffset = str(datetime.datetime.now())
        # Query the KZ api
        try:
            skz_response = requests.get(
                "https://kztimerglobal.com/api/v2/records/top/recent",
                params=skz_parameters,
            )
            kzt_response = requests.get(
                "https://kztimerglobal.com/api/v2/records/top/recent",
                params=kzt_parameters,
            )
            vnl_response = requests.get(
                "https://kztimerglobal.com/api/v2/records/top/recent",
                params=vnl_parameters,
            )
            logger.info("KZ API successfully queried.")
        except:
            logger.info("KZ API query unsuccessful.")

        # Store the recent records
        skz_recent_records = skz_response.json()
        kzt_recent_records = kzt_response.json()
        vnl_recent_records = vnl_response.json()

        logger.info(f"New TimeOffset: {TimeOffset}.")

        # Define an empty list that we will use to contain the relevant details from our respoonse
        simplified_recent_records = []

        # Run through each record in recent_records
        for d in skz_recent_records:
            player_name = d["player_name"]
            map_name = d["map_name"]
            mode = "SKZ"
            run_time = format_timespan(d["time"])
            run_date = str(
                dateparser.parse(d["created_on"], settings={"TIMEZONE": "UTC"})
            )
            # Append the information parsed from the json to the list
            simplified_recent_records.append(
                [player_name, map_name, mode, run_time, run_date]
            )
        for d in kzt_recent_records:
            player_name = d["player_name"]
            map_name = d["map_name"]
            mode = "KZT"
            run_time = format_timespan(d["time"])
            run_date = str(
                dateparser.parse(d["created_on"], settings={"TIMEZONE": "UTC"})
            )
            # Append the information parsed from the json to the list
            simplified_recent_records.append(
                [player_name, map_name, mode, run_time, run_date]
            )
        for d in vnl_recent_records:
            player_name = d["player_name"]
            map_name = d["map_name"]
            mode = "VNL"
            run_time = format_timespan(d["time"])
            run_date = str(
                dateparser.parse(d["created_on"], settings={"TIMEZONE": "UTC"})
            )
            # Append the information parsed from the json to the list
            simplified_recent_records.append(
                [player_name, map_name, mode, run_time, run_date]
            )

        # If the list is non-empty, then tweet out a formatted tweet detailing information about the record
        if simplified_recent_records:
            for i in range(len(simplified_recent_records)):
                tweet_text = (
                    "\U0001F30D"
                    + f"[{bold(simplified_recent_records[i][2])}]"
                    + f" {bold(simplified_recent_records[i][0])} set a new global record on {bold(simplified_recent_records[i][1])}"
                    + f" with a time of {bold(simplified_recent_records[i][3])}."
                    + "\n \n"
                    + f"Map leaderboard: kzstats.com/maps/{simplified_recent_records[i][1]}"
                )
                try:
                    api.update_status(tweet_text)
                    logger.info(
                        f"Successfully tweeted {simplified_recent_records[i][2]} global record on {simplified_recent_records[i][1]}"
                    )
                except:
                    logger.info(
                        f"Failed to tweet global record on {simplified_recent_records[i][1]}"
                    )

        # Sleep for 5 minutes before checking again for new records
        logger.info("Sleeping for 5 minutes...")
        time.sleep(300)


if __name__ == "__main__":
    main()
