import numpy as np
from scipy.optimize import minimize_scalar
from scipy import interpolate
from scipy.ndimage import interpolation
import matplotlib.pyplot as plt


# load the data and remove nans
# theoretical data
x = np.load('C://Users//user//Downloads//I_q_IPA_model.npy')
# experimantal data (larger), there are nans here
y_exp = np.load('C://Users//user//Downloads//I_q_IPA_exp.npy')
y = y_exp#[~np.isnan(y_exp).any(axis=1), :]
# scale x to fit y
x_scaled = x/(x.max()/y.max())
plt.plot(x[:, 0],x_scaled[:, 1], 'o', y[:, 0], y[:, 1], '-')
plt.legend(['Theoretical scaled', 'Empirical'])
plt.show()

#find the function to describe the data!
f1 = interpolate.interp1d(y[:, 0], y[:, 1], fill_value='extrapolate', kind= 'linear')
#f2 = interpolate.interp1d(y[:, 0], y[:, 1], fill_value='extrapolate', kind = 'quadratic')
## interpolate
x_new_lin = f1(x[:, 0])
# Visualize the data
plt.plot(y[:, 0], y[:, 1], 'o', x[:, 0], x_new_lin, '-')
plt.title('Interpolation of the empirical data')
plt.legend(['Empitical data', 'Linear interpolation'])
plt.show()