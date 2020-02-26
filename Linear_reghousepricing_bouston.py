import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics


# load the boston dataset
boston = datasets.load_boston(return_X_y=False)

boston

# define feature matrix (x) and response vector (y)
X = boston.data
Y = boston.target

# spliting X and Y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=1)

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train,Y_train)

# regiression coefficients
print('coefficients: \n', reg.coef_)

# varience score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test,Y_test)))

# plot for residual error

# setting plot style
plt.style.use('fivethirtyeight')

## plotting residual error in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - Y_train,
            color = "green", s=10, label='Train data')

## plotting residual error in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - Y_test,
            color = "blue", s=10, label='Test Data')

## plotting line for zero residual error 
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2) 

## plotting lengend
plt.legend(loc = 'upper right')

## plot title
plt.title("Residual errors")

plt.show()