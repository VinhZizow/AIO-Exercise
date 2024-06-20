import math

def calc_loss(y, y_hat, n, p):
    y_root = y**(1/n)
    y_hat_root = y**(1/n)
    different = y_root - y_hat_root
    loss = different**p
    return loss
    
def md_nre(y, y_hat, n, p, m):
    result = 0
    for i in range(1,m+1):
        coef = 1/i
        loss = calc_loss(y, y_hat, n, p )
        result += coef*loss
    return result

y=1
y_hat = 1.1
n=5
p=4
m=6
result = md_nre(y, y_hat, n, p, m)

print(result)
        

    