# iniciamos la biblioteca de matplotlib y matematicas
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import os

os.chdir('/home/osvaldo13576/Documentos/Github/homeworks8th/Img_biomed/tarea1_mod3/codes/')
# definimos unas constantes
gamma = 42.57*10**(6)
hbar = 1.055*10**(-34)
T = 309.15
k = 1.381*10**(-23)
B00 = np.array([1.5,3,7])
B0 =np.linspace(0,7,50)
N_up = 3*(10**(6))*np.exp(-B0*(gamma*hbar)/(k*T))
N_up0 = 3*(10**(6))*np.exp(-B00*(gamma*hbar)/(k*T))
N_up0_N_down0 = np.exp(-B00*(gamma*hbar)/(k*T))
# realizamos la gráfica B0 vs N_up
# establecemos que la gráfica sean puntos
fig = plt.figure()
ax = plt.subplot(1, 1, 1)
ax.scatter(B00,N_up0,s=100,c='c')
plt.plot(B0,N_up)

n = ['$B_0$=1.5[T]','$B_0$=3[T]','$B_0$=7[T]']

for i, txt in enumerate(n):
    ax.annotate(txt, (B00[i], N_up0[i]))
#ax = fig.add_subplot(111)
# establecemos los límites de la gráfica
plt.ylim(2999977,3*10**(6))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1e-5'))
# mostramos todos los decimales en el eje y
plt.xlabel('Campo magnético $B_0$ (T)')
# le asignamos una etiqueta a cada punto 

plt.ylabel('$N_{up}$')
plt.title('Número de protones antiparalelos $N_{up}$')
plt.savefig('B0_vs_N_up.pdf')
plt.show()
#guardamos la gráfica como pdf

print(N_up0)
print(N_up0_N_down0)