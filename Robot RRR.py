import numpy as np
import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH

# Función para limpiar valores numéricos cercanos a cero
# Esto evita que aparezcan valores como 6.12323399573677e-17 en la matriz

def limpiar_ceros(matriz, umbral=1e-10):
    """
    Convierte a cero cualquier valor absoluto menor que el umbral
    Parámetros:
        matriz: matriz tipo numpy
        umbral: valor mínimo para considerar como cero
    Retorna:
        matriz con ceros limpiados
    """
    matriz_limpia = np.where(np.abs(matriz) < umbral, 0.0, matriz)
    return matriz_limpia


# Numeric example: 3-joint planar robot (all revolute, a1=1, a2=1)
print("Numeric example:")
dh_params = [
    [np.pi/4, 0, 1, 0],
    [np.pi/4, 0, 1, 0],
    [np.pi/4, 0, 1, 0],
]
H_class = ForwardKinematicsDH.numeric(dh_params)
# Se aplica limpieza para eliminar valores numéricos muy pequeños
H_class_limpia = limpiar_ceros(H_class)
# Se imprime la matriz final limpia
print("End-effector transformation matrix:")
print(H_class_limpia)


# symbolic example: 3-joint planar robot 
print("\nSymbolic example: RRR Robot") #imprime texto especificando la matriz del robot RRR
q1, q2, q3= sp.symbols('q1 q2 q3') #se agrego el simbolo para q3
l1, l2, l3 = sp.symbols('l1 l2 l3')  #se agrego el simbolo para l3
dh_params_sym = [
    [q1, 0, l1, sp.pi/2],   # se hizo el cambio de las variables para que coincidan con los valores de la matriz para un robot RRR
    [q2, 0, l2, 0],   # se cambiaron tanto los ángulos q1, q2, las distancias a se quedaron en 0, la distancia l se cambio tanto l1 y l2 y el angulo alpha se agino el valor de pi/2 y 0 para los demas casos
    [q3, 0, l3, 0],   #se agrega la siguiente linea para la articulacion 3 
]
H_sym_class = ForwardKinematicsDH.symbolic(dh_params_sym)
print("End-effector transformation matrix:")
sp.pprint(H_sym_class, use_unicode=True)
