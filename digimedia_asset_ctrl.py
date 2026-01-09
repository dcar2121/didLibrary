import os
import json

class MediaAssetManager:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

    def save_asset(self, asset_name, asset_data):
        asset_path = os.path.join(self.storage_path, f"{asset_name}.json")
        with open(asset_path, 'w') as asset_file:
            json.dump(asset_data, asset_file)

    def load_asset(self, asset_name):
        asset_path = os.path.join(self.storage_path, f"{asset_name}.json")
        if os.path.exists(asset_path):
            with open(asset_path, 'r') as asset_file:
                return json.load(asset_file)
        else:
            raise FileNotFoundError(f"Asset '{asset_name}' not found.")

    def list_assets(self):
        return [f[:-5] for f in os.listdir(self.storage_path) if f.endswith('.json')]

# Example usage
if __name__ == "__main__":
    manager = MediaAssetManager("media_assets")
    manager.save_asset("example_asset", {"title": "Example", "description": "This is an example asset."})
    print(manager.load_asset("example_asset"))
    print(manager.list_assets())
