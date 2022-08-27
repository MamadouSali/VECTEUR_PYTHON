import math
def distance(xA , yA ,xB ,yB):
    calculator_avec_racine = f'√{(xB - xA)**2 + (yB - yA)**2}'
    calculator_sans_racine = math.sqrt((xB - xA)**2 + (yB - yA)**2)
    return calculator_avec_racine , calculator_sans_racine


    


