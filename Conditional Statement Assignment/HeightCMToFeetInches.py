cm = int(input('Enter height in Centimeter: '))

fi = cm/2.54

feet = fi//12

inches = fi - (12*feet)

print('Height in CM is: ', cm)
print('Height in Feet and Inches is: ', feet, 'feet ', inches, 'inches')