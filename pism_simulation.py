"""
Compute and Post-Processing Jobs for Pism

Written by component_cookiecutter

----
"""

from pyesm.component.component_simulation import ComponentCompute
from pyesm.pism import Pism

class PismCompute(Pism, ComponentCompute):
    """ A docstring. Please fill this out at least a little bit """

    def _compute_requirements(self):
        """ Compute requirements for Pism """
        self.EXECUTEABLE = "pismr"
        self.command = None
        self.num_tasks = None
        self.num_threads = None

