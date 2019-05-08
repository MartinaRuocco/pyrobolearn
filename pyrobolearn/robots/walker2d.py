#!/usr/bin/env python
"""Provide the Walker2D Mujoco model.
"""

import os

from pyrobolearn.robots.robot import Robot

__author__ = "Brian Delhaisse"
__copyright__ = "Copyright 2018, PyRoboLearn"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Brian Delhaisse"
__email__ = "briandelhaisse@gmail.com"
__status__ = "Development"


class Walker2D(Robot):
    r"""Walker 2D Mujoco Model

    References:
        [1] description: https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet/gym/pybullet_data/mjcf
    """

    def __init__(self,
                 simulator,
                 position=(-0.5, 0, 0.1),
                 orientation=(0, 0.707, 0, 0.707),
                 fixed_base=False,
                 scale=1.,
                 urdf=os.path.dirname(__file__) + '/mjcfs/walker2d.xml'):
        # check parameters
        if position is None:
            position = (-0.5, 0., 0.1)
        if len(position) == 2:  # assume x, y are given
            position = tuple(position) + (0.1,)
        if orientation is None:
            orientation = (0, 0.707, 0, 0.707)
        if fixed_base is None:
            fixed_base = False

        super(Walker2D, self).__init__(simulator, urdf, position, orientation, fixed_base, scale)
        self.name = 'walker2D'


# Test
if __name__ == "__main__":
    from itertools import count
    from pyrobolearn.simulators import BulletSim
    from pyrobolearn.worlds import BasicWorld

    # Create simulator
    sim = BulletSim()

    # create world
    world = BasicWorld(sim)

    # create robot
    robot = Walker2D(sim)

    # print information about the robot
    robot.print_info()

    # run simulation
    for i in count():
        # step in simulation
        world.step(sleep_dt=1./240)
