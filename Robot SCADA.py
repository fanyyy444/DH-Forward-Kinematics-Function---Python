import numpy as np
import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH

print("Numeric example: SCARA robot")
dh_params = [
    [np.pi/4, 0, 1, 0],        # Articulación 1: rotacional
    [np.pi/4, 0, 1, np.pi],    # Articulación 2: rotacional con torsión de 180°
    [0, 1, 0, 0],              # Articulación 3: prismática (d = 1)
]

H_class = ForwardKinematicsDH.numeric(dh_params)
print("End-effector transformation matrix:")
print(H_class)


print("\nSymbolic example: SCARA robot")  #imprime texto especificando la matriz del robot SCARA
q1, q2 = sp.symbols('q1 q2')         # Ángulos articulares
l1, l2 = sp.symbols('l1 l2')         # Longitudes de eslabones
d3 = sp.symbols('d3')                # Se define el desplzamiento como d3

dh_params_sym = [
    [q1, 0, l1, 0],          # Articulación 1: θ=q1, d=0, a=l1, α=0
    [q2, 0, l2, sp.pi],      # Articulación 2: θ=q2, d=0, a=l2, α=π
    [0, d3, 0, 0],           # Articulación 3: θ=0, d=d3, a=0, α=0
]

H_sym_class = ForwardKinematicsDH.symbolic(dh_params_sym)

#Simplifica la matriz para que se vea los más parecida al resultado original
H_sym_simplificada = sp.simplify(H_sym_class)

print("End-effector transformation matrix (simplificada):")
sp.pprint(H_sym_simplificada, use_unicode=True)
