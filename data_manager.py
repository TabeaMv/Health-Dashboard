from fitbitclient import FitBitClient
from datetime import date
from pathlib import Path
import json


class DataManager(FitBitClient):
    
    def __init__(self, client: FitBitClient, storage_dir="historical_data"):
        self.client = client
        self.storage_dir = Path(storage_dir)


    # def get_last_saved_date(self, endpoint_name):
    #     endpoint_path = self.storage_dir / f"{endpoint_name}.json"
    #     if endpoint_path.exists():
    #         with open(endpoint_path, "r") as f:
    #             endpoint_data = json.load(f)
    #         print(endpoint_data[-1]["date"])


    def fetch_new_endpoint_data(self, endpoint_name, start_date, end_date):
        print(self.client.data_access(endpoint_name, start_date, end_date))
        


    def write_new_endpoint_data(self, endpoint_name, data):
        pass


def main():
    tabea_fitbit = FitBitClient.from_file()
    # tabea_fitbit = DataManager.from_auth_code()
    manager = DataManager(tabea_fitbit)
    # manager.fetch_historical_steps(date(2023, 11, 22), date.today())
    # endpoints = ["activity", "heartrate", "location", "nutrition",
    #              "oxygen_saturation", "profile", "respiratory_rate",
    #              "settings", "sleep", "social", "temperature", "weight"]
    manager.fetch_new_endpoint_data("sleep", "2025-09-01", "2025-09-08")


if __name__=='__main__':
    main()