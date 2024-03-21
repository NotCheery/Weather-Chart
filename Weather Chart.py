'''Lab 13'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\tislam8\Downloads\atlanta_weather.csv") #reads CSV file
#print(data)

#DATA PLOT
months = data['Month'] #reads month column
h_temp = data['High'] #reads high column
l_temp = data['Low'] #reads low column

print(months)

#Plots and labels the plotting
plt.plot(months, h_temp, 'b--o', label='High') 
plt.plot(months, l_temp,'g:^', label= 'Low')

plt.title("Atlanta - Monthly Temperature", fontsize=20) #title
plt.xlabel('Month', fontsize=16) #x-label
plt.ylabel('Temperature (Fahrenheit)', fontsize=16) #y-label
plt.legend(fontsize=20)

#Annotate highest temp of the year
plt.annotate('Highest of the year', arrowprops = dict(facecolor = 'red'), xy=('Jul', 88), xytext=('May', 73))
plt.show() #outputs the graph



    