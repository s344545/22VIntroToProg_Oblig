# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:35:21 2022

@author: saris
"""


input_file = open('oil.txt', 'r')
lines = input_file.readlines()
input_file.close()

date= []; oil= []; volume= []
comma= ','; space= ' ';
volume_modified=[]; oil_modified=[]
        

  
oilDictF = {}

def oilVolumeFunc(lines):
    
    for i in range(1, 19):     
        date.append(lines[i][:10])
        volume.append(lines[i][16:-1])
        
        if i == 8 or i == 15: 
          oil.append(lines[i][11:15])

        #elif i != 8 or i != 15: 
        else:
         oil.append(lines[i][11:17]) 
         
        
   
    for i in range(0,18):
         if comma not in volume[i]:
           volume_modified.append(volume[i])
         elif comma in volume[i]:
            for v in range(0,6):
             if volume[i][v] == comma:
                 volume[i] = volume[i][v:]
                 volume_modified.append(volume[i].replace(',', ''))
         else:
            print('No need for editing the content on volume list .. ')
            
 
    for k in range(0,18): 
         if comma not in oil[k]:
             oil_modified.append(oil[k])   
         elif comma in oil[k]:
          itemo = oil[k].replace(',' , '')
          oil_modified.append(itemo)                    
         else:
          print('No need for editing the content on oil list .. ')
            
        
    for i in range(0,18):
      oilDictF[date[i]] = [oil_modified[i], volume_modified[i]]
      
    
    print('#########################################################################################') 
    print('\n  This program will display information about oil based on date provided ..')
    print('  Now you might type in the date for the desired information ..')
    print('  Information to be displayed were recorded from  2022/02/07 to 2022/03/04..')
    print('  Based on the date provided you can either access the number of oil \n contracts or oil prices on that desired date..')
    print('  So, please type in a date within this range of days ... ')
    print('  Please, first type in the year (4 Intgers) followed by a slash "/" ..')
    print('  Then, type in the month (2 Intgers) again followed by a slash "/" ..')
    print('  Lastly, type in the desired day (2 Intgers) number again followed by a slash "/" ..\n')
    print('#########################################################################################')
    oil_Date = input('Type in the date now (Example: 2022/02/28):  ')
     
    while True:
       if oil_Date not in oilDictF :
         print('\nInvalid input, please type in again a date in the right format ..')
         oil_Date = input('Type in a date now (Example: 2022/02/28):  ')
       else:  
        value = input('Please type in either Price or Contracts: ').capitalize()
        while value not in ('Price', 'Contracts') :
            print('\nInvalid input or date was not registered, please type in again either Price or Contracts ..')
            value = input('Please type in here either Price or Contracts: ').capitalize()
        if value == 'Price':    
            print('\n\nThe oil price was {} $ on {}.' 
                  .format(oilDictF[oil_Date][0], oil_Date)) 
        else:
            print('\n\nThere were {} oil contracts on {}.' 
                  .format(oilDictF[oil_Date][1],oil_Date)) 
        oil_Date = input('Type in a new date to access information (Example: 2022/02/28):  ')  

oilVolumeFunc(lines)