from F2Depine import soga

def F(x):
    if x <= 10/3:
        return 0
    elif x>= 10/3 and x <= 20/3:
        return 3
    else:
        return 0

pulso_rectangular = soga.CondicionesIniciales("cerrado", 10, 60, F, range(100)) #10 es el largo de la soga , 60 es v_f
anim = pulso_rectangular.animate(1000)
