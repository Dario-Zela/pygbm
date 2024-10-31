import numpy as np

"""
pygmb - Python library to simulate geometric brownian motion.

To use the code set up the simulation parameters via the GBMSimulator class
.. code-block:: python

    # Import GBMSimulator
    from pygbm.gbm_simulator import GBMSimulator

    # Parameters for GBM
    y0 = 1.0
    mu = 0.05
    sigma = 0.2

    # Initialize simulator
    simulator = GBMSimulator(y0, mu, sigma)

Finally, to run the simulation call the simulate_path method on the time span and the number of steps the simulation is going to take

.. code-block:: python
    # Parameters for the simulation
    T = 1.0
    N = 100

    # Simulate path
    t_values, y_values = simulator.simulate_path(T, N)
"""

class GBMSimulator:

    """
    The class used to encapsulate the parameters for the simulation and solve the GBM equation.
    """

    def __init__(self, y0, mu, sigma):
        """
        Sets up the physics of the enviroment the simulation will run in

        :param y0: Starting location of the simulation.
        :type y0: float

        :param mu: The drift of the simulation.
        :type mu: float

        :param sigma: The diffusion of the simulation.
        :type sigma: float
        """

        self.y0 = y0
        self.mu = mu
        self.sigma = sigma

    def browninan(self, dt, N_steps):
        B = np.random.normal(0, np.sqrt(dt), size=N_steps)
        return B

    def simulate_path(self, T_Final, N_steps):
        """
        Runs the simulation on the input given by the user
        
        :param T: The lenght of time should the program simulate.
        :type T: float

        :param N: The number of simualtion steps.
        :type N: float
        """
        
        dt = T_Final / N_steps
        Y = np.exp((self.mu - self.sigma ** 2 / 2) * dt + self.sigma * self.browninan(dt, N_steps))
        Y = self.y0 * np.cumprod(Y)
        T = np.linspace(0, T_Final, N_steps)
        return T, Y