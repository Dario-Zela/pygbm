Usage
=====

.. _installation:

Installation
------------

To use pygbm, first install it using pip:

.. code-block:: console

   (.venv) $ pip install pygbm

Run a simulation
----------------

To create a simulation in a python script the ``GBMSimulator`` class must be used:

.. automodule:: gbm_simulator
    :members:


For example:

.. code-block:: cython
    from pygbm.gbm_simulator import GBMSimulator
    import matplotlib.pyplot as plt

    # Parameters for GBM
    y0 = 1.0
    mu = 0.05
    sigma = 0.2
    T = 1.0
    N = 100

    # Initialize simulator
    simulator = GBMSimulator(y0, mu, sigma)

    # Simulate path
    t_values, y_values = simulator.simulate_path(T, N)

    # Plot the simulated path
    plt.plot(t_values , y_values , label ="GBM Path")
    plt.xlabel(" Time ")
    plt.ylabel("Y(t)")
    plt.title("Simulated Geometric Brownian Motion Path")
    plt.legend()
    plt.show()

Run a simulation in the CLI
----------------

To create a simulation in the CLI, the following syntax can be used:

.. code-block:: console

   (.venv) $ pygbm simulate --y0 1.0 --mu 0.05 --sigma 0.2 --T 1.0 --N 100 --output gbm_plot.png

The `--y0`, `--mu`, and `--sigma` arguments are required, while the program will default a `--T` to 10, `--N` to 100 and `output` to "output.png"