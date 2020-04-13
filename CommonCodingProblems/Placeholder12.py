def allGreater(n, priceMap):
    sortedKeys = sorted(priceMap.keys())
    x1 = sortedKeys[0]
    x2 = sortedKeys[1]
    px1 = priceMap[x1]
    px2 = priceMap[x2]

    priceDist = float(px2-px1)
    x2x1 = float(x2-x1)
    x1xn = float(x1-n)

    price = px1 - priceDist*x1xn/x2x1

    return round(price,2)

def allSmaller(n,priceMap) :
    sortedKeys = sorted(priceMap.keys())
    x1 = sortedKeys[-2]
    x2 = sortedKeys[-1]
    px1 = priceMap[x1]
    px2 = priceMap[x2]

    priceDist = float(px2-px1)
    x2x1 = float(x2-x1)
    xnx2 = float(n-x2)

    price = px2 + priceDist*xnx2/x2x1

    #return price
    return round(price,2)



def inBetween(n,priceMap):
    sortedInstances = sorted(priceMap.keys())

    for i in range(len(sortedInstances)) :
        if n < sortedInstances[i] :
            x1 = sortedInstances[i-1]
            x2 = sortedInstances[i]
            break
    
    px1 = priceMap[x1]
    px2 = priceMap[x2]

    priceDist = float(px2-px1)
    x2x1 = float(x2-x1)
    xnx1 = float(n-x1)

    price = px1 + priceDist*xnx1/x2x1

    return round(price,2)




def interpolate(n, instances, price):
    # Write your code here
    cnts = len(instances)
    priceMap = {}

    for i in range(cnts):
        if price[i] > 0 :
            priceMap[instances[i]] = price[i] 

    allValidInstances = sorted(priceMap.keys())

    if len(allValidInstances) == 1 :
        return str(priceMap[allValidInstances[0]])
    else :
        if n < allValidInstances[0]:
            return str(allGreater(n,priceMap))
        elif n > allValidInstances[-1] :
            return str(allSmaller(n,priceMap))
        elif n in allValidInstances :
            return str(priceMap[n] )
        else :
            return str(inBetween(n,priceMap))
        
        