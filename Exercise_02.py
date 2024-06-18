import math
# Kiem tra có phải là số
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True 

def activatiion_function(x, act_func_name):
    if is_number(x)==True:
        def relu(x):
            if x<=0:
                result=0
            else:
                result=x
            return float(result)
        def sig(x):
            return 1.0/(1+math.e**(-x))
        def relu(x):
            if x<=0:
                result=0
            else:
                result=x
            return float(result)
        result= None
        if act_func_name == 'relu':
            result = relu(x)
        elif act_func_name == 'sig':
            result = sig(x)
        elif act_func_name == 'relu':
            result = relu(x)
        return result
    
print(activatiion_function(x= 5, act_func_name='sig'))
    


