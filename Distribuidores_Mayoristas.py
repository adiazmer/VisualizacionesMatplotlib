# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:48:19 2021

@author: Ariel
"""

#Importo librerias
import matplotlib.pyplot as plt


#Crer un dataset con un diccionario
ventas_dist = {'Gonzales': 123238.80,
        'Martinez': 432432.59,
        'Geraldo': 888211.3,
        'Gastaldi': 1897726.12,
        'Pumar LLC': 232323.77,
        'Rubens': 111567.12,
        'Barroso': 137351.96,
        'Gimenez': 123112.00,
        'Rodo Hnos': 119112.78,
        'Fernandez': 42111.12}

#Armar lista con valores y keys
ventas = list(ventas_dist.values())
empresas = list(ventas_dist.keys())


#Creo una figure y un Axe
fig, ax = plt.subplots(figsize=(11,6))

#Usar float en vez de notacion cientifica para valores grandes
plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)

#Cambio la escala del eje 
plt.xlim(0,2100000)

#Elimino bordes superior y derecho para un mejor efecto
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#rotacion de titulos del eje X
xlabels=ax.get_xticklabels()
plt.setp(xlabels,rotation=45)

#Grilla controlada por ejes
ax.yaxis.grid(color='black', linestyle='dashed', alpha=0.2)
ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.1)

#configuro estilo de la flecha para apuntar datos
arrowprops = {"arrowstyle":"wedge,tail_width=0.5", 
              "alpha":0.7, 
              "color":'g'}

#Estilo caja 
bbox={"boxstyle":"larrow", 
      "alpha":0.7, 
      "color":'g'}

#Estilo de tipo de letra
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 11,
        }

#Funcion de anotacion
plt.annotate('Visitar el Lunes por favor!', 
             xy=(300000,9),
             xycoords="data",
             xytext=(400000, 9), 
             textcoords='data',
             size=14, 
             bbox=bbox,
             )

#Rotilar eje Y
#de tipo de letra, ver arriba para mas detalles
plt.ylabel('Distribuidores', fontdict=font)

#Titulo y supertitulo 
fig.suptitle('Wholesale Distributor S.A. - Actividad Comercial',
             x=0.125, 
             y=0.98, 
             ha='left', 
             fontsize=18, fontdict=font)

plt.title('Performance Distribuidores Marzo 2022', 
          loc='left', 
          fontsize=14)

#Anotacion libre de texto
plt.text(-0.5,
         -3, 
         'Datos:Relevamiento Plot:adiazmerlo@gmail.com', 
         ha='left', 
         fontsize = 11, 
         alpha=0.9, fontdict=font)

#Plot de barras horizontales
ax.barh(empresas, ventas,label="Ventas en USD")

#Leyenda
ax.legend(loc='lower right', frameon=False)

ax.legend(fancybox=True, 
          framealpha=1, 
          shadow=True, 
          borderpad=1)

#Visualizar plot
plt.show()
