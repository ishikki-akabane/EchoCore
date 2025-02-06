import requests


class EchoClient:
    def __init__(self, token):
        self.token = token
        self.plugin_url = "https://raw.githubusercontent.com/ishikki-akabane/EchoCore/main/plugins"


    def setup_plugins(self):
        response = requests.get(f"https://testing.vercel.app/download?download={self.token}")
        if response.status_code == 200:
            plugins_list = response["result"]
            file_list = []

            free_plugins = plugins_list["free-plugins"]
            for plugin_id in free_plugins:
                file_url = f"{self.plugin_url}/{plugin_id}"
                file_list.append(file_url)

            return file_list