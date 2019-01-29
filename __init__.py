"""
Pism Component

A Ice Model, Version: x.x.x

Please write some more documentation.

Written by component_cookiecutter

----
"""

import logging
import os

from pyesm.component import Component


class Pism(Component):
    """ A docstring for your component """
    DOWNLOAD_ADDRESS = "http://some/address/of/a/project"
    NAME = "pism"
    VERSION = "x.x.x"
    TYPE = "ice"

    def _resolution(self, res_key=None):
        """
        Defines the resolution and generates the following attributes
        """
        Resolutions = {None:
                        {"LateralResolution": None,
                        "VerticalResolution": None,
                        "Timestep": None,
                        "_nx": None,
                        "_ny": None,
                        "_nz": None,
                        "_ngridpoints": None,
                        }
                      }
        for key, value in Resolutions[res_key].items():
            setattr(self, key, value)
