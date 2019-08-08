import numpy as np

def gradient_descent(X, y, lr=0.01, threshold=1e-4):
    params = np.array([0., 0., 0.])
    #
    #TODO: please write your code here.
    #
    n = len(y)
    output = [0.0 for _ in range(n)]
    for j in range(10000):
        for i in range(n):
            output[i] = params[0]*X[i][0] + params[1]*X[i][1] + params[2]
            delta = y[i] - output[i]
            if abs(delta) < threshold:
                break
            params[0] = params[0] + lr*delta*X[i][0]
            params[1] = params[1] + lr*delta*X[i][1]
            params[2] = params[2] + lr*delta

    return params

#
# Please don't modify any code below.
#
if __name__ == "__main__":
    # Code to generate the data/test case
    n_samples = 10000
    x_1, x_2 = np.random.random(n_samples), np.random.random(n_samples)
    theta_1, theta_2, b = map(float, input().split())
    #print (theta_1, theta_2, b)
    X, y = np.vstack([x_1, x_2]).T, theta_1 * x_1 + theta_2 * x_2 + b
    # Solution
    params = gradient_descent(X, y)
    result = []
    for param in params:
        result.append('{:.02f}'.format(param))
    print(' '.join(result))