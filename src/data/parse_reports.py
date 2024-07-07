import json
import re, os
import numpy as np
import pandas as pd
from dotenv import find_dotenv, load_dotenv


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    # Remove non-alphabetical characters
    # TODO: add more
    text = re.sub(r'[^a-z\s]', '', text)
    return text


# obtaining zap reports
directory = "C:\\Users\\Hammer\\PycharmProjects\\zapdppipeline\\data\\raw"


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        file = os.path.join(directory, filename)
        with open(file, 'r', encoding='utf-8') as json_file:
            json_parser = json.loads(json_file.read())
            df = pd.json_normalize(json_parser)
            scan_requests = []
            scan_responses = []

            for index, row in df.iterrows():
                sites = df.site.iloc[index]
                for site in sites:
                    for key, value in site.items():
                        if type(value) == list:
                            for val in value:
                                alert_desc = ""
                                for key3, val3 in val.items():
                                    if key3 == 'alert':
                                        alert_desc += val3
                                    if key3 == 'desc':
                                        alert_desc += val3
                                    if type(val3) == list:
                                        model_request = ""
                                        model_response = ""
                                        for vale in val3:
                                            for key4, val4 in vale.items():
                                                if key4 == 'response-header':
                                                    model_response += val4
                                                if key4 == 'response-body':
                                                    model_response += val4
                                                if key4 == 'request-header':
                                                    model_request += val4
                                                if key4 == 'request-body':
                                                    model_request += val4

                                        scan_requests.append(model_request)
                                        scan_responses.append(model_response + alert_desc)

    else:
        continue

print(scan_requests)