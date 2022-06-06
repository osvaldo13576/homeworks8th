# importamos librerías para estadísticas y gráficos
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as stats
import os
# establecemos el directorio de trabajo
os.chdir('/home/osvaldo13576/Documentos/Github/homeworks8th/Seguridad Radiológica/pract_03/figuras/')
# realizamos nuestro vector de distancias  (eje x)
d = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 250])
# establecemos nuestro set de datos #
# primer set: medidas con capuchón (eje y)
set1_con = np.array([4540, 1180, 610, 477, 289, 216, 171, 129, 153, 141, 94, 98])/1000
set2_con = np.array([4540, 1200, 540, 379, 272, 180, 148, 103, 95, 84, 89, 66])/1000
set3_con = np.array([5060, 1200, 710, 387, 294, 192, 160, 127, 85, 82, 63, 57])/1000
# segundo set: medidas sin capuchón
set1_sin = np.array([4220, 1240, 590, 355, 287, 217, 164, 117, 110, 89, 82, 71])/1000
set2_sin = np.array([4950, 1400, 700, 425, 381, 243, 188, 167, 107, 98, 85, 61])/1000
set3_sin = np.array([4810, 1350, 650, 438, 328, 228, 160, 129, 122, 100, 94, 64])/1000
# calculamos la media de los 3 sets con capuchón (eje y)
media_con = np.mean(np.array([set1_con, set2_con, set3_con]), axis=0)
# calculamos la media de los 3 sets sin capuchón
media_sin = np.mean(np.array([set1_sin, set2_sin, set3_sin]), axis=0)
# calculamos la desviación estándar de los 3 sets con capuchón
desv_con = np.std(np.array([set1_con, set2_con, set3_con]), axis=0)
# calculamos la desviación estándar de los 3 sets sin capuchón
desv_sin = np.std(np.array([set1_sin, set2_sin, set3_sin]), axis=0)
# graficamos los resultados contra la distancia y mostramos los resultados, establecemos tamaño y guardamos el gráfico como pdf
plt.figure(figsize=(5.5,4))
plt.errorbar(d, media_con, yerr=desv_con, fmt='o', label='Con capuchón', capsize=6,color='#C70039',markersize=3)
plt.errorbar(d, media_sin, yerr=desv_sin, fmt='o', label='Sin capuchón',capsize=6,color='#98ca41',markersize=3)
plt.xlabel('Distancia $[cm]$')
plt.ylabel('Exposición $[mR/h]$')
plt.legend();plt.title(label='Exposición vs Distancia')
plt.savefig('pract_03_code0.pdf')
plt.show()

###################
plt.figure(figsize=(5.5,4))
plt.errorbar(d, media_sin, yerr=desv_sin, fmt='o', label='Sin capuchón',capsize=6,color='#98ca41',markersize=3)
plt.xlabel('Distancia $[cm]$')
plt.ylabel('Exposición $[mR/h]$')
plt.legend();plt.title(label='Exposición vs Distancia')
plt.savefig('pract_03_sin.pdf')
plt.show()

###################

plt.figure(figsize=(5.5,4))
plt.errorbar(d, media_con, yerr=desv_con, fmt='o', label='Con capuchón', capsize=6,color='#C70039',markersize=3)
plt.xlabel('Distancia $[cm]$')
plt.ylabel('Exposición $[mR/h]$')
plt.legend();plt.title(label='Exposición vs Distancia')
plt.savefig('pract_03_con.pdf')
plt.show()
# calculamos la distancia entre las dos medias
print(np.abs(media_con - media_sin))
print("con tapa: ", desv_con)
print("sin tapa: ", desv_sin)

# realizamos la gráfica de los resultados
plt.figure(figsize=(5.5,4))
plt.plot(1/d**2, (media_con), label='Con capuchón', marker='o', color='#C70039',markersize=3)
plt.plot(1/d**2, (media_sin), label='Sin capuchón', marker='o', color='#98ca41',markersize=3)
plt.xlabel('$1/r^2$ $[cm^{-2}]$')
plt.ylabel('Exposición $[mR/h]$')
plt.legend();plt.title(label='Exposición vs Distancia')
plt.savefig('pract_03_code0_rep_r2.pdf')
plt.show()

