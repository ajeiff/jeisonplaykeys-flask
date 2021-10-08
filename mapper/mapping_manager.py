import requests
import json


class ListMusicSoundcloud():

    def __init__(self, url):
        self.url = url

    def getstatus(self):
        response = requests.get(url=self.url)
        return response.status_code

    def geturlsong(self):
        response = requests.get(url=self.url)
        payload = response.content.decode("utf-8")
        payload = (payload.split(",")[-3].split("\\")[-2])[1:]
        if payload.startswith("https") and payload.endswith(".wav"):
            return payload
        return None

    def getlistmetadatasongdict(self):
        response = requests.get(url=self.url)
        payload_str = response.content
        list_payload_body_str = (json.loads(payload_str))["body"]
        list_metadata = json.loads(list_payload_body_str)
        return list_metadata


if __name__ == '__main__':
    data = ListMusicSoundcloud("https://kymuvqgv84.execute-api.eu-west-3.amazonaws.com/api/")
    result = data.getlistmetadatasongdict()
    result[0]['file']