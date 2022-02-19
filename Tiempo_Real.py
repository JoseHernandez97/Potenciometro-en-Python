from matplotlib import collections
import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 

def getSerialData(self, Samples, SerialConnection, lines, lineValueText, lineLabel):
    value = float(SerialConnection.readline().strip())
    data.append(value)
    lines.set_data(range(Samples), data)
    lineValueText.set_text(lineLabel+ ' = ' + str(round(value, 2)))

serialPort='COM7' # Aqui es necesario Saber a Que puerto esta conectado el Arduino
baudRate= 9600

try:
    SerialConnection= serial.Serial(serialPort, baudRate)
except:
    print(' No se pudo establecer la coneccion ')


Samples= 100 
data= collections.deque([0] * Samples, maxlen=Samples)
SampleTime= 100

xmin= 0
xmax= Samples
ymin=0
ymax=6

fig= plt.figure(figsize=(13,6))
ax= plt.axes(xlim=(xmin, xmax),ylim=(ymin, ymax))
plt.title('Lectura en tiempo real')
ax.set_xlabel('Samples')
ax.set_ylabel('Valor de Voltaje')

lineLabel='Voltaje'
lines = ax.plot([], [], label=lineLabel)[0]
lineValueText = ax.text(0.85, 0.95, ' ' , transform=ax.transAxes)

anim= animation.FuncAnimation(fig, getSerialData, fargs=(Samples,SerialConnection, lines, lineValueText, lineLabel), interval=SampleTime)
plt.show()

SerialConnection.close() 


