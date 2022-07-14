from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

labels = 'CARRO','CARROS','CARROS ','CARROS',
sizes =[40,30,15,20]

figl, axl = plt.subplots()

axl.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

axl.axis('equal')

plt.show()