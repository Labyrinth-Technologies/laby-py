import click
from simulations import Simulation 
@click.group()
def main():
    pass

@main.command()
@click.option('--simulation_agent_id', default=None, help='The id of the simulation agent to run')
@click.option('--config_path', default=None, help='Path to the simulation agent configuration file')
@click.option('--remote', is_flag=True, default=False, help='Run the simulation remotely, disables localhost')
@click.option('--api_key', required=True, help='Organization API key for authentication')
def run(simulation_agent_id, config_path, remote, api_key):
    """Run simulations"""
    click.echo("Running simulations...")
    sim = Simulation(simulation_agent_id=simulation_agent_id, config_path=config_path, remote=remote, api_key=api_key)
    retval = sim.run()
    click.echo(retval)

if __name__ == "__main__":
    main()