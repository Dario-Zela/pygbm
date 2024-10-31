import numpy as np

class GBMSimulator:

    def __init__(self, y0, mu, sigma):
        self.y0 = y0
        self.mu = mu
        self.sigma = sigma

    def browninan(self, dt, N_steps):
        B = np.random.normal(0, np.sqrt(dt), size=N_steps)
        return B

    def simulate_path(self, T_Final, N_steps):
        dt = T_Final / N_steps
        Y = np.exp((self.mu - self.sigma ** 2 / 2) * dt + self.sigma * self.browninan(dt, N_steps))
        Y = self.y0 * np.cumprod(Y)
        T = np.linspace(0, T_Final, N_steps)
        return T, Y