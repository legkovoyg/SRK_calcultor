import numpy as np
import matplotlib.pyplot as plt
from time import time
from SRK_equation import SRK_Flash
from openpyxl import Workbook
from input_data_for_equations import *

Fluid = []
for i in range(N):
    Fluid.append(
        [
            component_name[i],
            z[i],
            mass[i],
            Pkr[i],
            Tkr[i],
            Vkr[i],
            w[i],
            cpen[i],
            T_boil[i],
            density_liq_phase[i],
        ]
    )

T = np.array(373.15)
P = np.array(10)

v = SRK_Flash(Fluid, BIPs=None)
(
    W,
    Z_v,
    Z_l,
    x_i,
    y_i,
    Stable,
    m,
    enthalpy,
    enthalpy_w,
    enthalpy_l,
    Cp,
    Cp_w,
    Cp_l,
    Cv,
    Cv_w,
    Cv_l,
    volume,
    VolumeMy_y,
    VolumeMy_x,
    density,
    density_y,
    density_x,
) = v.vle(P, T)
print(f"W = {W} \n" f"Zv = {Z_v}\n" f"Zl = {Z_l}\n")
