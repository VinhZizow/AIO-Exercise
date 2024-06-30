# 1 Tính n!
def giai_thua(n):
    result= 1
    for i in range(1, n+1):
        result= result*i
    return result
# 2 Tính sinx
def cal_sinx(x, n):
    sinx= 0
    for i in range(n+1):
        he_so_dau = (-1)**i
        tu_so = x**(2*i+1)
        mau_so = giai_thua(2*i+1)
        sinx = sinx + (he_so_dau*(tu_so/mau_so))
    return sinx

# 3 Tính cosx
def cal_cosx(x, n):
    cosx= 0
    for i in range(n+1):
        he_so_dau = (-1)**i
        tu_so = x**(2*i)
        mau_so = giai_thua(2*i)
        cosx += (he_so_dau*(tu_so/mau_so))
    return cosx

# 4 Tính sinhx
def cal_sinhx(x, n):
    sinhx= 0
    for i in range(n+1):
        tu_so = x**(2*i+1)
        mau_so = giai_thua(2*i+1)
        sinhx += (tu_so/mau_so)
    return sinhx

# 5 Tính coshx
def cal_coshx(x, n):
    coshx= 0
    for i in range(n+1):
        tu_so = x**(2*i)
        mau_so = giai_thua(2*i)
        coshx += (tu_so/mau_so)
    return coshx


x = 3.14
n = 10

print(f'Kiem tra giai thua n: {giai_thua(n)}')
print(f'Gia tri sinx: {cal_sinx(x, n)}')
print(f'Gia tri cosx: {cal_cosx(x, n)}')
print(f'Gia tri sinhx: {cal_sinhx(x, n)}')
print(f'Gia tri coshx: {cal_coshx(x, n)}')        
