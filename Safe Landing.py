massCraft, massFuel, h, v = [int(x) for x in raw_input().split()]
burningRates = [int(x) for x in raw_input().split()]

def calcGrav(height):
    return 1.622 * ((1737100 ** 2) / ((1737100 + height)**2))

dM = 0
m = massCraft + massFuel
g = calcGrav(h)
dV = 0
Vexhaust = 2800

dt = 0.1


while h > 0:
    if len(burningRates) > 0 or massFuel <= 1 :
        burningRate = burningRates.pop(0)
    else:
        burningRate = 0
    for i in [float(j) / 100 for j in range(1, 101)]:
        h = h - v * dt
        
        if h <= 0:
            break
        
        if massFuel > 0:
            dM = burningRate * dt
        else:
            dM = 0
        dV = Vexhaust * (dM / m)
        m = m - dM
        massFuel = massFuel - dM
        g = calcGrav(h)
        v = v + g * dt - dV
print v
    
    