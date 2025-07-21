# Console 
print("Let's talk about the Setting, Characters, and Context for Moroccan and Colombian women!\n")

print("Settings: Morocco is a country in Northern Africa and Colombia is in South America and both are developing countries. In the data ectraction process, data was taken between 1992-2003 for Morocco and 1990-2015 for Colombia.\n")

print("Characters: large majority of Moroccan women work in the agricultural industry and Colombian women live in urban areas due to work. Sharing education about women' rights in Morocco can prompt better access for work and participation in politics.\n")

print("Context: Colombia Total Fertility Rate (TFR): 1.7 & Morocco TFR: 2.2. More reproductive freedoms for Colombian women.\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# print Research Question 
print("After the initial gathering of data, the formulated research question is: What caused more urban migration for unmarried women in Colombia and Morocco? What can be some causes?\n")

#Findings of the Research Question 
print("Here are the findings and what may cause unmarried Colombian and Moroccan women to move to urban areas. \n")

print("In the 1990s, there was a spike in violence against women in rural areas in Colombia.\n")

print("The service sector was rapidly increasing, therefore a lot of women moved to urban areas for employment and fleeing from violence.\n")

print("In the 1990s, Morocco faced decreasing agriculutral productivity causing more women and families to move to urban areas for employment and education.") 

# For VNC
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")

# Add Step 1 code here:
listOfcountries = lwd["country_name"].unique()
#print(util.vformat_list(listOfcountries))

#selecting two countries for comparison 
oneCountryBooleanList = lwd["country_name"] == "Morocco"
secondCountryBooleanList = lwd["country_name"] == "Colombia"
#print(oneCountryBooleanList)

#  extracting data
oneCountryData = lwd.loc[oneCountryBooleanList]
secondCountryData = lwd.loc[secondCountryBooleanList]

#print (oneCountryData)
# x and y variables 
plt.xlabel("Women living in urban areas (%)")
plt.ylabel("Women never married (%)") 

# different colors for different countries 
plt.scatter(x="DM_urban_p", y="DM_nvr_marr_p", data = oneCountryData, color = 'blue')
plt.scatter(x="DM_urban_p", y="DM_nvr_marr_p", data = secondCountryData, color = 'red')

# limit statements 
plt.ylim(10, 50)
plt.xlim(45, 85)

# loc at top right hand cornor and made a legend 
plt.legend(('Morocco', 'Colombia'))
plt.show()
