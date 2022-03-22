# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:26:46 2022

@author: Ariel
"""

#Importar librerias de interes
import pandas as pd
import matplotlib.pyplot as plt

#Variables
eia=pd.read_html('https://www.eia.gov/opendata/qb.php?category=711255&sdid=TOTAL.PAPRPUS.A')
eia_df=eia[0]

#Descripcion del dataset mas estadistica descriptiva general
print(eia_df.info())
print(eia_df.describe())

#Limpiar dataset
oil_production=eia_df[['Period','Value','Series Name']]
oil_production=oil_production.sort_values('Period',ascending=True)
#oil_production.set_index('Period',inplace=True)
#print(oil_production.head())

#Plot
fig,ax = plt.subplots(figsize=(20,10))

plt.plot(oil_production['Period'], oil_production['Value'], color='#074ef5', lw=2.5, 
         label=oil_production['Series Name'].head(1))

ax.legend(loc='lower right', frameon=True)
#ax.legend(fancybox=True,
 #        framealpha=1,
  #       shadow=True,
   #      borderpad=1)

#tick label
ticklabel=ax.get_xticklabels()
plt.setp(ticklabel, rotation=45)

#Grilla
ax.yaxis.grid(color='black', alpha=1, linestyle='-')
#ax.xaxis.grid(color='grey', alpha=0.7, linestyle='dashed')

#Spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

#rotular ejes
#plt.ylabel('Production')
#plt.xlabel('Date')

#axeY_limites
plt.ylim(0,15000)

#Formatos
font={'family':'serif',
     'weight':'normal',
     'color':'black',
     'size':18}

#Suptitle
fig.suptitle('Crude Oil Production',
            x=0.125,
            y=0.95,
            ha='left',
            fontdict=font,
            fontsize=30)

plt.title('Thousand Barrels per Day',
         loc='left',
         fontsize=20)

plt.show()
