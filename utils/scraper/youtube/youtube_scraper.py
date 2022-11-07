from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import json
import time
import re
import requests


class YouTubeScraper:

    def __init__(self, chromedriver_path: str):
        self.chromedriver_path = chromedriver_path
        self.api_url = "https://www.youtube.com/youtubei/v1/next?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"
        self.max_lazyload = 10

    def __initialise_driver(self):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        self.driver = webdriver.Chrome(desired_capabilities=capabilities,
                                       executable_path=self.chromedriver_path,
                                       chrome_options=options)

    def __find_first_lazyload(self, logs: list[dict]) -> dict:
        lazyload_logs = []
        for log in logs:
            str_log = str(log)
            # api pattern
            if re.findall(r"next\?key", str_log):
                lazyload_logs.append(log)
        return lazyload_logs[0]

    def __get_header_and_payload(self, url: str) -> list[dict]:
        self.__initialise_driver()
        action = ActionChains(self.driver)
        self.driver.get(url)
        # wait and load page
        time.sleep(2)
        for i in range(3):
            action.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)
        logs_raw = self.driver.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
        self.driver.close()

        # extract header and __get_header_and_payload
        first_lazyload_request = self.__find_first_lazyload(logs)
        request_data = first_lazyload_request['params']['request']
        header = request_data['headers']
        payload = json.loads(request_data['postData'])

        return header, payload

    def __find_continuation_token(self, response_json: dict):
        tokens = re.findall(r"'token': \'(\S+)'", str(response_json))
        if len(tokens) > 0:
            return tokens[0]
        else:
            return None

    def _scrape_one_lazyload(self, header: dict, payload: dict) -> dict:
        response = requests.post(self.api_url, headers=header, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def scrape(self, yt_url: str) -> list[dict]:
        header, payload = self.__get_header_and_payload(yt_url)

        data = []
        for p in range(1, self.max_lazyload + 1):
            print("Request for lazy load page: {p} ...")
            response_json = self._scrape_one_lazyload(header, payload)
            if len(list(response_json.keys())) > 0:
                data.append(response_json)
                # update token if exist
                token = self.__find_continuation_token(response_json)
                if token:
                    payload['continuation'] = token
                else:
                    break
            else:
                break
        return data