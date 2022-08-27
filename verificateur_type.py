def verificatueur() :
    xA = input ("xA: ")
    if "." in xA :
        xA = float(xA)
    else:
        xA = int(xA)

    yA = input ("yA: ")
    if "." in yA :
        yA = float(yA)
    else:
        yA = int(yA)

    xB = input ("xB: ")
    if "." in xB :
        xB = float(xB)
    else:
        xB = int(xB)

    yB = input ("yB: ")
    if "." in yB :
        yB = float(yB)
    else:
        yB = int(yB)
    
    return xA,yA,xB,xA