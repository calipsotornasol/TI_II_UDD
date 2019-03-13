# pizzas.py
i = int(input('¿Cuántas pizzas individuales desea?: '))
m = int(input('¿Cuántas pizzas mediandas desea?: '))
f = int(input('¿Cuántas pizzas familiares desea?: '))
total = 4600*i + 7850*m + 10750*f
print('Total a pagar:', total)
