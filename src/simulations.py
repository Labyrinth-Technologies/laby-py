import requests
import json
import os
from utils import load_config

if os.environ.get('LABY_ENV') == 'dev':
    from _constants_dev import *
else:
    from constants import *

class Simulation():
    def __init__(self, api_key, project_id, simulation_agent_id, config_path, remote=False):
        self.api_key = api_key
        self.project_id = project_id
        self.simulation_agent_id = simulation_agent_id
        self.config = load_config(config_path)
        self.remote = remote
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def run(self):
        if not self.simulation_agent_id:
            json_data = {"project_id": self.project_id}
            if self.config:
                json_data["config"] = self.config
            else:
                print("Guided config creation not yet implemented")
                return

            response = requests.post(CREATE_SIMULATION_AGENT_ENDPOINT, json=json_data, headers=self.headers)
            
            if response.status_code != 200:
                print(f"Error creating simulation agent: HTTP {response.status_code}")
                return

            try:
                data = response.json()
            except json.JSONDecodeError:
                print("Error decoding JSON response from the API")
                return

            self.simulation_agent_id = data.get('simulation_agent_id')
            if not self.simulation_agent_id:
                print("No simulation_agent_id returned from the API")
                return

        json_data = {"simulation_agent_id": self.simulation_agent_id}
        response = requests.post(CREATE_SIMULATION_ENDPOINT, json=json_data, headers=self.headers)
        if response.status_code != 200:
            print(f"Error creating simulation: HTTP {response.status_code}")
            return

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Error decoding JSON response from the API")
            return

        self.simulation_id = data.get('simulation_id')
        if not self.simulation_id:
            raise ValueError("No simulation_id returned from the API")

        return {"simulation_agent_id": self.simulation_agent_id, "simulation_id": self.simulation_id}