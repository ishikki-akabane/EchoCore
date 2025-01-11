import requests


class EchoClient:
    def __init__(self, token):
        self.token = token


    def setup_plugins(self):
        response = requests.get(f"https://testing.vercel.app/download={self.token}")
        if response.status_code == 200:
            plugins_list = response["result"]
            file_list = []
            for plugin_id in plugins_list:
                file_url = f"https://raw.githubusercontent.com/ishikki-akabane/EchoCore/main/{plugin_id}"
                file_list.append(file_url)

            return file_url