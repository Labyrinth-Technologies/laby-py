import click
from simulations import run_simulations

@click.group()
def main():
    pass

@main.command()
def run():
    """Run simulations"""
    click.echo("Running simulations...")
    run_simulations()

if __name__ == "__main__":
    main()