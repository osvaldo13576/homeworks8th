# importamos librerías para estadísticas y gráficos
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as stats
import os
import sys
# establecemos el directorio de trabajo
os.chdir('/home/osvaldo13576/Documentos/Github/homeworks8th/Seguridad Radiológica/pract_03/codes/')
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
plt.ylabel('Rapidez de exposición $[mR/h]$')
plt.legend();plt.title(label='Rapidez de exposición vs Distancia')
plt.grid()
plt.savefig('pract_03_code0.pdf')
plt.show()

###################
plt.figure(figsize=(5.5,4))
plt.errorbar(d, media_sin, yerr=desv_sin, fmt='o', label='Sin capuchón',capsize=6,color='#98ca41',markersize=3)
plt.xlabel('Distancia $[cm]$')
plt.ylabel('Rapidez de exposición $[mR/h]$')
plt.legend();plt.title(label='Rapidez de exposición vs Distancia')
plt.grid()
plt.savefig('pract_03_sin.pdf')
plt.show()

###################

plt.figure(figsize=(5.5,4))
plt.errorbar(d, media_con, yerr=desv_con, fmt='o', label='Con capuchón', capsize=6,color='#C70039',markersize=3)
plt.xlabel('Distancia $[cm]$')
plt.ylabel('Rapidez de exposición $[mR/h]$')
plt.legend();plt.title(label='Rapidez de exposición vs Distancia')
plt.grid()
plt.savefig('pract_03_con.pdf')
plt.show()
# realizamos un ajuste lineal de los datos
# vector de distancias inverso al cuadrado
d_inv2 = 1/d**2
p_con = np.polyfit(d_inv2, media_con, 1)
p_sin = np.polyfit(d_inv2, media_sin, 1)
# del ajuste obtenemos su R cuadrado
R_con = 1-np.sqrt(np.sum((media_con[::-1] - np.polyval(p_con, d_inv2[::-1]))**2)/len(media_con[::-1]))
R_sin = 1-np.sqrt(np.sum((media_sin[::-1] - np.polyval(p_sin, d_inv2[::-1]))**2)/len(media_sin[::-1]))
#buscamos la pendiente de la recta y su ordenada al origen
m_con = p_con[0]
b_con = p_con[1]
m_sin = p_sin[0]
b_sin = p_sin[1]
#graficamos los datos de ajuste de curva
plt.figure(figsize=(9.5,4)) 
plt.plot(1/d**2, media_con, 'o',label='Con capuchón',  color='#C70039', markersize=3)
plt.plot(1/d**2, media_sin, 'o',label='Sin capuchón',  color='#98ca41', markersize=3)
plt.plot(1/d**2, np.polyval(p_con, 1/d**2), '-', color='#C70039', label='Con capuchón (ajuste)')
plt.plot(1/d**2, np.polyval(p_sin, 1/d**2), '-.', color='#98ca41', label='Sin capuchón (ajuste)' )
plt.xlabel('$1/r^2$ $[cm^{-2}]$')
plt.ylabel('Rapidez de exposición $[mR/h]$')
plt.legend();plt.title(label='Rapidez de exposición vs $1/$Distancia$^2$')
plt.grid()
plt.savefig('pract_03_code0_rep_r2.pdf')
plt.show()


# realizamos la gráfica de los resultados
plt.figure(figsize=(5.5,4))
plt.plot(1/d**2, (media_con), label='Con capuchón', marker='o', color='#C70039',markersize=3)
plt.plot(1/d**2, (media_sin), label='Sin capuchón', marker='o', color='#98ca41',markersize=3)
plt.xlabel('$1/r^2$ $[cm^{-2}]$')
plt.ylabel('Rapidez de exposición $[mR/h]$')
plt.legend();plt.title(label='Rapidez de exposición vs Distancia')
plt.grid()
plt.savefig('pract_03_code0_rep_r2_.pdf')
plt.show()

# vamos a tomar los vectores con las medidas media y de sus elementos totales, vamos a comprobar la ley de inversos cuadrados 8)
# vamos a dividir el primer elemento por el segundo, el segundo por el tercero, etc, en un ciclo for (10 ciclos en total)
sqrt_X2_X1_con = np.zeros(11)
sqrt_X2_X1_sin = np.zeros(11)
d1_d2  = np.zeros(11)
for i in range(11):
    sqrt_X2_X1_con[i] = np.sqrt(media_con[i+1]/media_con[i])
    sqrt_X2_X1_sin[i] = np.sqrt(media_sin[i+1]/media_sin[i])
    d1_d2[i] = d[i]/d[i+1]
    #terminamos el ciclo for

#error de las medidas promedio sin con respecto a mediadas con
error_medidas = 100*np.abs(media_sin-media_con)/media_sin

#error del cociente de las distancias d1/d2 con respecto a sqrt(X_2/X_1)_con y sqrt(X_2/X_1)_sin
error_d1_d2_con = 100*np.abs(d1_d2-sqrt_X2_X1_con)/d1_d2
error_d1_d2_sin = 100*np.abs(d1_d2-sqrt_X2_X1_sin)/d1_d2

# mostramos los datos relevantes
sys.stdout = open("info.txt", "w")
print('vector de distancia = ', np.round(d,2))
print('vector de 1/distancia^2 = ', 1/d**2)
print('vector de media con capuchón = ', np.round(media_con,2))
print('vector de media sin capuchón = ', np.round(media_sin,2))
print('vector de desv_con = ', desv_con)
print('vector de desv_sin = ', desv_sin)
print('vector de sqrt_X2_X1_con = ', np.round(sqrt_X2_X1_con,3))
print('vector de sqrt_X2_X1_sin = ', np.round(sqrt_X2_X1_sin,3))
print('vector de d1_d2 (con las medidas del vector de distancia)= ', np.round(d1_d2,3))
print('R cuadrado con capuchón = ', np.round(R_con,4))
print('R cuadrado sin capuchón = ', np.round(R_sin,4))
print('m_con (pendiente)= ', m_con)
print('b_con (ordenada al origen)= ', b_con)
print('m_sin (pendiente)= ', m_sin)
print('b_sin (ordenada al origen)= ', b_sin)
print('error de las medidas promedio_sin con respecto a mediadas_con = ', np.round(error_medidas,2))
print('error del cociente de las distancias d1/d2 con respecto a sqrt(X_2/X_1)_con = ', np.round(error_d1_d2_con,2))
print('error del cociente de las distancias d1/d2 con respecto a sqrt(X_2/X_1)_sin = ', np.round(error_d1_d2_sin,2))
print('número de datos = ', len(d))
print('número de errores error_d1_d2_con = ', len(error_d1_d2_con))
sys.stdout.close()

# imprimimos el error_d1_d2_con considerando los dos primeros decimales
#print('error del cociente de las distancias d1/d2 con respecto a sqrt(X_2/X_1)_con = ', np.round(error_d1_d2_con,2))