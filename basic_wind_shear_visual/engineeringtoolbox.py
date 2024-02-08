import matplotlib.pyplot as plt
import numpy as np

# shear wind exponent, over smooth terrain
alpha = 0.1
# shear wind exponent, over row crops
# alpha = 0.2

# Initial height
h_0 = 1

# Max height (m)
h_max = 122 
# Changing height
h = np.linspace(h_0, h_max, h_max)

# wind speed at h_0 (m/s)
v_0 = 5

# wind speed as a function of changing height
v = v_0 * (h/h_0)**alpha

plt.scatter(v, h)
plt.plot(v, h)
plt.xlim([0, max(v)+1])
plt.show()
