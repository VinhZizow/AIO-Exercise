import math
import random

def for_loop_mean(n):
    mean=0
    for i in range(n):
        mean=mean+i
    mean = mean/n
    return mean

def mae(n):
    mae=0
    for i in range(n):
        y= random.random()
        y_hat= random.random()
        absolute_error = abs(y-y_hat)
        mae=mae+absolute_error
    mae = mae/n
    return mae

def mse(n):
    mse=0
    for i in range(n):
        y= random.random()
        y_hat= random.random()
        squared_error = abs(y-y_hat)**2
        mse=mse+squared_error
    mse = mse/n
    return mse

def rmse(n):
    rmse=math.sqrt(mse(n))
    return rmse


n=10
print(f'MAE:{mae(n)}')
print(f'MSE:{mse(n)}')
print(f'RMSE:{rmse(n)}')

    