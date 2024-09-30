import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline


class ProbabilityDensityDistribution:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._spline = InterpolatedUnivariateSpline(x, y)
        
    def evaluate(self, x):
        return self._spline(x)

    def plot(self):
        plt.plot(self._x, self._y, "o")
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self.evaluate(x))

    def integral(self, x1, x2):
        pass


if __name__=="__main__":
    x = np.linspace(0., 1., 4)
    y = np.exp(x)
    pdf = ProbabilityDensityDistribution(x, y)
    pdf.plot()
    plt.show()