from ace.samples import wang04
from ace import model
from ace import ace
import numpy as np



# Example from the paper

# x = [np.random.uniform(-1, 1, size = 300), np.random.uniform(-1, 1, size = 300),
# np.random.uniform(-1, 1, size = 300), np.random.uniform(-1, 1, size = 300), np.random.uniform(-1, 1, size = 300)]
# e = np.random.normal(0, 1, size = 300)
# y = np.log(4 + np.sin(4*x[0]) + np.absolute(x[1]) + np.power(x[2],2) + np.power(x[3], 3) + x[4] + 0.1*e)

# ace_model = model.Model()
# ace_model.build_model_from_xy(x, y)

# ace.plot_transforms(ace_model.ace, fname = 'transforms.pdf')



# Polynomial function of f and g

x = [np.random.uniform(-10, 10, size = 300)]
e = np.random.normal(0, 1, size = 300)
y = np.power(0.5 * np.power(x[0], 2) - x[0] - 10.0 + 0.1*e, 1.0/3)

print(x)
print(y)

ace_model = model.Model()
ace_model.build_model_from_xy(x, y)

ace.plot_transforms(ace_model.ace, fname = 'transforms.pdf')



# General fuction of f and g

# x = [np.random.uniform(-1, 1, size = 500)]
# e = np.random.normal(0, 1, size = 500)
# y = np.log(4 + np.sin(x[0]) + 0.1*e)


# ace_model = model.Model()
# ace_model.build_model_from_xy(x, y)

# ace.plot_transforms(ace_model.ace, fname = 'transforms.pdf')
