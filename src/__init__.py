# Version of the laby package
__version__ = "0.1.0"

# Import main functions for easier access
from .main import main
from .simulations import run_simulations

# Define what should be imported with "from laby import *"
__all__ = ['main', 'run_simulations']