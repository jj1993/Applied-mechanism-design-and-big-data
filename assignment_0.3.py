import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math

def friis_function(const):

    c = 299792458
    f = 2.4
    x_router = 0
    y_router = 0
    x_device = 20
    y_device = 0
    Z = 2
    p_t = 0
    r = math.sqrt((x_device-x_router)^2 + (y_device-y_router)^2 + Z^2)

    p_r = p_t + const * np.log10(c / (4.0 * np.pi * f * r))
    return p_r

#the mean and sigma used for creating the gaussian noise
mu = 0.0
sigma = 1.0

#creating the gaussian package noise
package_noise = np.random.normal(mu, sigma, 1000)


expected = friis_function(20.0)
measure_friis = friis_function(25.0)
measurements = [measure_friis + noise1 for noise1 in package_noise]

normalized_residuals = [(measurement - expected)/1 for measurement in measurements]


#make the histogram plot with the gaussian plotted over it in red
count, bins, ignored = plt.hist(normalized_residuals, 20, normed=True)
plt.show()



