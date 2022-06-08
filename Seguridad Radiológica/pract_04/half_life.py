# importamos librerías para estadísticas, gráficos y lectura de archivos csv
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
# establecemos el directorio de trabajo
directorio = '/home/osvaldo13576/Documentos/Github/homeworks8th/Seguridad Radiológica/pract_04/'
os.chdir(directorio) 

#importamos el archivo de datos csv
data = pd.read_csv('Practica4_vidamedia.csv')
# realizamos el vector de datos de la segunda, tercera y cuarta columna
data1 = np.array(data.iloc[:,0])
data2 = np.array(data.iloc[:,1])
data3 = np.array(data.iloc[:,2])
# calculamos el promedio de los tres sets de datos
mean_data = np.mean(np.array([data1, data2, data3]), axis=0)
# calculamos el desvío estándar de los tres sets de datos
std_data = np.std(np.array([data1, data2, data3]), axis=0)
# creamos el vector de tiempo
t0 = 1/6 # 10 minutos en horas
t1 = 9*t0 + 13/60 + (40+37)/60# tiempo 1er equipo
t2 = 19 + t1+20*t0 #al dia siguiente....
# el tiempo es acumulativo!
t3 = t2+6*t0+1
t = np.array([0, t0, 2*t0, 3*t0, 4*t0, 5*t0, 6*t0, 7*t0, 8*t0, 9*t0, 9*t0 + 13/60, t1, t1+t0,t1+2*t0, t1+3*t0, t1+4*t0, t1+5*t0, t1+6*t0, t1+7*t0, t1+8*t0, t1+9*t0,t1+10*t0,t1+11*t0,t1+12*t0,t1+13*t0,t1+14*t0,t1+15*t0,t1+16*t0,t1+17*t0,t1+18*t0,t1+19*t0,t1+20*t0, t2+t0,t2+4*t0,t2+5*t0,t2+6*t0,t2+6*t0+(53/60),t2+6*t0+1,t3+t0,t3+2*t0+(3/60),t3+2*t0+(11/60),t3+2*t0+(2/6),t3+2*t0+(3/6),t3+2*t0+(41/60)])



#graficamos los datos promedio, con grid
plt.figure(figsize=(5.5,4))
plt.plot(t, mean_data, 'ro',markersize=3)
plt.xlabel('Tiempo $[h]$')
plt.ylabel('Actividad $[\mu Ci]$')
plt.title('Promedio de la actividad')
plt.grid()
plt.savefig('mean.pdf')
plt.show()

#hacemos el ajuste de curva de la actividad promedio 
p = np.polyfit(t, np.log(mean_data), 1)
# del ajuste obtenemos su R cuadrado
R2_test = 1 - (np.sum((np.log(mean_data) - np.polyval(p, t))**2)/np.sum((np.log(mean_data) - np.mean(np.log(mean_data)))**2))
#buscamos la pendiente y la ordenada al origen
m = p[0]
b = p[1]

#graficamos el resultado del ajuste de curva en semilogy
plt.figure(figsize=(9.5,4))
plt.semilogy(t, np.exp(m*t+b), '-r', label='Ajuste')
plt.semilogy(t, mean_data, 'o', label='Actividad',markersize=3)
plt.xlabel(r'Tiempo $[h]$')
plt.ylabel(r'Actividad $[\mu Ci]$')
plt.title('Actividad en el tiempo (pendiente = %.3f, ordenada al origen = %.3f)' % (m, b))
plt.legend(loc='best')
plt.grid()
# guardamos la gráfica
plt.savefig('fit.pdf')
plt.show()

# creamos un vector de 0 a 30 horas
t_r = np.linspace(0,30,100)
Ac = np.exp(b)*np.exp(t_r*m)
#graficamos los datos con barras de error
plt.figure(figsize=(15,10))
plt.plot(t_r,Ac,label = 'Interpolación')
plt.errorbar(t, mean_data, yerr=std_data, fmt='o', color='black', label='Datos',capsize=15,markersize=3)
#modificamos el tamañp de la xlabel y ylabel
plt.xlabel('Tiempo $[h]$', fontsize=30)
plt.ylabel('Actividad $[\mu Ci]$', fontsize=30)
plt.title('Promedio de la actividad', fontsize=30)
plt.grid()
plt.savefig('mean_bar.pdf')
plt.show()




sys.stdout = open("info.txt", "w")
print('vector de tiempo = ', t)
print('vector de datos = ', mean_data)
print('duración del experimento = ', t[-1], ' horas')
# imprimimos los resultados
print('################')
print('La pendiente es: ', m)  
print('La ordenada al origen es: ', b)
print('R cuadrado (prueba): ', R2_test)
print('La actividad inicial es: ', np.exp(b), '10e-6 Ci')
print('La constante de decaimiento es: ', -m, '[1/h]')
print('La vida media es: ', -np.log(2)/m, '[h]')
sys.stdout.close()