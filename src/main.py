import click
from simulations import Simulation 
from utils import load_config

@click.group()
def main():
    pass

@main.command()
@click.option('--simulation_agent_id', default=None, help='The id of the simulation agent to run')
@click.option('--config_path', default=None, help='Path to the simulation agent configuration file')
@click.option('--remote', is_flag=True, default=False, help='Run the simulation remotely, disables localhost')
@click.option('--api_key', required=True, help='Organization API key for authentication')
@click.option('--project_id', required=True, help='Project ID for the simulation')
def run(simulation_agent_id, config_path, remote, api_key, project_id):
    """Run simulations"""
    click.echo("Running simulations...")
    if config_path:
        config = load_config(config_path)
        if "name" not in config:
            print("name is required in the config")
            return
        if "endpoint_url" not in config:
            print("endpoint_url is required in the config")
            return
        if "num_trials" not in config:
            print("num_trials is required in the config")
            return
        if "conversation_initiator" not in config:
            print("conversation_initiator is required in the config, must be 'adversarial_agent' or 'generative_agent'")
            return

    else:
        config = {}

    sim = Simulation(simulation_agent_id=simulation_agent_id, config=config, remote=remote, api_key=api_key, project_id=project_id)
    retval = sim.run()
    click.echo(retval)

if __name__ == "__main__":
    main()