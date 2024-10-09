import requests
import json
import os
from utils import load_config

if os.environ.get('LABY_ENV') == 'dev':
    from _constants_dev import *
else:
    from constants import *

class Simulation():
    def __init__(self, api_key, simulation_agent_id, config_path, remote=False):
        self.api_key = api_key
        self.simulation_agent_id = simulation_agent_id
        self.config = load_config(config_path)
        self.remote = remote
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def run(self):
        if not self.simulation_agent_id:
            try:
                json_data = {} 
                if self.config:
                    json_data["config"] = self.config
                else:
                    json_data["config"] = {
                        "project_id": "329d8d60-2748-412a-abb1-38cb48a45369",
                        "name": "Laby Simulation Agent"
                    }
                response = requests.post(CREATE_SIMULATION_AGENT_ENDPOINT, json=json_data, headers=self.headers)
                response.raise_for_status()
                data = response.json()
                self.simulation_agent_id = data.get('simulation_agent_id')
                if not self.simulation_agent_id:
                    raise ValueError("No simulation_agent_id returned from the API")
            except requests.RequestException as e:
                print(f"Error creating simulation agent: {e}")
                return
            except json.JSONDecodeError:
                print("Error decoding JSON response from the API")
                return
            except ValueError as e:
                print(f"Error: {e}")
                return
            
        return self.simulation_agent_id