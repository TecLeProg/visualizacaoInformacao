#!/usr/bin/env python
# coding: utf-8

# # Projeto de Visualização da Informação

# Nome: Alessandro Antônio Nascimento

# RGM: 23361611
# 

# Instituição: Universidade de Franca

# Curso: Ciências da Computação

# # Gráfico Quantitativo - Em barras

# Este gráfico apresenta o TOP 3: Os estados com maior quantidade de casos confirmados de COVID-19 no Brasil até 10/06/2020.

# In[1]:


import matplotlib.pyplot as plt 
import numpy as np
estados = ('São Paulo', 'Rio de Janeiro', 'Ceará',)
indice = np.arange(len(estados))
casos_confirmados = [156316,74373,71947]
plt.bar(indice, casos_confirmados, color=["blue","green","red"])
plt.xticks(indice, estados, fontsize='14', rotation='45')
plt.ylabel('Total de Casos Confirmados', fontsize='14')
plt.title('Top 3: Os estados com maior quantidade de casos confirmados de COVID-19 no Brasil até 10/06/2020', fontsize='16')
plt.grid(True)
plt.show ()


# # Gráfico Temporal - Em linhas

# Este gráfico apresenta o total de casos confirmados de COVID-19 de Fevereiro até Junho nos estados de SP, RJ e CE.

# In[2]:


import matplotlib.pyplot as plt
meses = [2,3,4,5,6]
sp = [2,2339,28698,109698,156316]
rj = [0,708,9453,53388,74373]
ce = [0,401,7861,48489,71947]
plt.plot(meses, sp, c='r', ls='-', lw="2", marker='^', ms=10, fillstyle='full', label='São Paulo')
plt.plot(meses, rj, c='b', ls='-', lw="2", marker='o', ms=10, fillstyle='full', label='Rio de Janeiro')
plt.plot(meses, ce, c='g', ls='-', lw="2", marker='^', ms=10, fillstyle='top', label='Ceará')
plt.legend()
eixoX = ['29/02/2020', '31/03/2020', '30/04/2020', '31/05/2020', '10/06/2020']
plt.xticks([2,3,4,5,6], eixoX, rotation='60')
plt.ylabel('Total de Casos Confirmados', fontsize='14')
plt.title('Casos Confirmados de COVID-19 de Fevereiro até Junho nos estados de SP, RJ e CE ', fontsize='16')
plt.grid(True)
plt.show()


# # Gráfico Hierárquico - Treemaps

# Este gráfico apresenta o total de Casos Confirmados de COVID-19 até 10/06/2020 por regiões.

# In[1]:


import plotly.express as px
import pandas as pd
estados = ["RO","AC","AM","RR","PA","AP","TO","MA","PI","CE","RN","PB","PE","AL","SE","BA","MG","ES","RJ","SP","PR","SC","RS","MS","MT","GO","DF"]
regioes = ["Norte","Norte","Norte","Norte","Norte","Norte","Norte","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Nordeste","Sudeste","Sudeste","Sudeste","Sudeste","Sul","Sul","Sul","Centro-Oeste","Centro-Oeste","Centro-Oeste","Centro-Oeste"]
casos_confirmados = [9850,8746,52849,6594,63405,14623,6529,53508,8823,71947,13234,24032,41935,18176,10615,32685,17501,23391,74373,156316,7934,12594,13619,2853,4762,7380,19433]
df = pd.DataFrame(dict(estados=estados,regioes=regioes,casos_confirmados=casos_confirmados))
df["all"] = "all" 
fig = px.treemap(df,path=[regioes,estados],values=casos_confirmados)
fig.update_layout(
title="Total de Casos Confirmados de COVID-19 até 10/06/2020 por regiões",
font=dict(
family="Arial, monospace",
size=16,
color="#7f7f7f"))
fig.show()


# In[ ]:




