# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 14:57:25 2022

@author: saris
"""
##############################################################################
###########################  First Text File #################################
##############################################################################

input_file = open('oil_raw_data.txt', 'r')
lines = input_file.readlines()


##############################################################################
#############################  First List Set ################################
##############################################################################


date = []; oil = []; volume = []; comma = ','; space = ' ';
volume_modified = []; oil_modified = []; date_modified = []
oilDict = {}; oilDictF = {}

##############################################################################
#############################  Second List Set ###############################
##############################################################################


date2 = []; oil2 = []; volume2 = []; comma = ','; space = ' ';
volume_modified2 = []; oil_modified2 = []; date_modified = []


##############################################################################
###########################  Second Text File ################################
##############################################################################


input_file2 = open('oil.txt', 'r')
lines2 = input_file.readlines()
output_file = open('oil.txt', 'w')



##############################################################################
#############################  Main Function #################################
##############################################################################

def oilInputFunc():
 #oilFunc = True:
 oilInput = str(input('Please type in either 1, 2, 3 or press Enter to quit:  '))

# while True:
 if oilInput not in ('1','2','3', ''):
   print('\nInvalid input ..')
   oilInput = input('Please type in either 1, 2, 3 or press Enter to quit : ')

###############################################################################
#############################  First Function #################################
###############################################################################

 elif oilInput == '1':
         for i in range(1, 20):

             date.append(lines[i][2:12])
             volume.append(lines[i][22:-1])

             if i == 8 or i == 15:
                 oil.append(lines[i][16:20])

             # elif i != 8 or i != 15:
             else:
                 oil.append(lines[i][16:22])

         for i in range(0, 19):

             if comma not in volume[i]:
                 volume_modified.append(volume[i])

             else:
                 itemv = volume[i].replace(',', '')
                 volume_modified.append(itemv)

         for k in range(0, 19):
             if comma not in oil[k]:
                 oil_modified.append(oil[k])
             elif comma in oil[k]:
                 itemo = oil[k].replace(',', '')
                 oil_modified.append(itemo)
             else:
                 print('No need for editing the content on oil list .. ')

         for d in range(0, 19):
             date_modified.append(date[d][-4:] + "/" + date[d][:2] + "/" + date[d][-7:-5])

         output_file = open('oil.txt', 'w')
         output_file.write('date, oil, volume \n')
         for i in range(0, 19):
             output_file.write('{},{},{}\n'.format(date_modified[i], oil_modified[i], volume_modified[i]))

###############################################################################
#############################  Second Function ################################
###############################################################################

 elif oilInput == '2':
         for i in range(1, 20):

             date.append(lines[i][2:12])
             volume.append(lines[i][22:-1])

             if i == 8 or i == 15:
                 oil.append(lines[i][16:20])

             # elif i != 8 or i != 15:
             else:
                 oil.append(lines[i][16:22])

         for i in range(0, 19):

             if comma not in volume[i]:
                 volume_modified.append(volume[i])

             else:
                 itemv = volume[i].replace(',', '')
                 volume_modified.append(itemv)

         for k in range(0, 19):
             if comma not in oil[k]:
                 oil_modified.append(oil[k])
             elif comma in oil[k]:
                 itemo = oil[k].replace(',', '')
                 oil_modified.append(itemo)
             else:
                 print('No need for editing the content on oil list .. ')

         for d in range(0, 19):
             date_modified.append(date[d][-4:] + "/" + date[d][:2] + "/" + date[d][-7:-5])

         output_file = open('oil.txt', 'w')
         output_file.write('date, oil, volume \n')
         for i in range(0, 19):
             output_file.write('{},{},{}\n'.format(date_modified[i], oil_modified[i], volume_modified[i]))

         for i in range(0, 19):
             # oilDict[oil_modified[i]] = date_modified[i]
             oilDict[float(oil_modified[i])] = date_modified[i]

         print('#######################################################################')
         print('\n  This program will display information about oil prices')
         print('  Now you only have two options to procede in this process ..')
         print('  Please type in Max if you would like to access info about \n maximum oil price')
         print(' Or you may instead type in Min if you would like to access \n info about minimum oil price')
         print('#######################################################################')
         Max_min = input('Please either insert Max or Min:  ').capitalize()

         while Max_min not in ('Max', 'Min'):
             print('\nInvalid input ..')
             Max_min = input('Please either insert Max or Min:  ').capitalize()
         # else:
         if Max_min == 'Max':
             #  oilDict =
             print('\n\nMaximum oil price was on {}, and the price was {} $ .'
                   .format(oilDict[max(oilDict)], max(oilDict)))

             # elif Max_min == 'Min':
         else:
             print('\n\nMinimum oil price was on {}, and the price was {} $ .'
                   .format(oilDict[min(oilDict)], min(oilDict)))


###############################################################################
#############################  Third Function #################################
###############################################################################

 elif oilInput == '3':
    for i in range(1, 20):
    
        date.append(lines[i][2:12])
        volume.append(lines[i][22:-1])
    
        if i == 8 or i == 15:
            oil.append(lines[i][16:20])
    
        # elif i != 8 or i != 15:
        else:
            oil.append(lines[i][16:22])
    
    for i in range(0, 19):
    
        if comma not in volume[i]:
            volume_modified.append(volume[i])
    
        else:
            itemv = volume[i].replace(',', '')
            volume_modified.append(itemv)
    
    for k in range(0, 19):
        if comma not in oil[k]:
            oil_modified.append(oil[k])
        elif comma in oil[k]:
            itemo = oil[k].replace(',', '')
            oil_modified.append(itemo)
        else:
            print('No need for editing the content on oil list .. ')
    
    for d in range(0, 19):
        date_modified.append(date[d][-4:] + "/" + date[d][:2] + "/" + date[d][-7:-5])
    
    output_file = open('oil.txt', 'w')
    output_file.write('date, oil, volume \n')
    for i in range(0, 19):
        output_file.write('{},{},{}\n'.format(date_modified[i], oil_modified[i], volume_modified[i]))
    
    output_file.close()
     
     
###########################################################################

###########################################################################

############################################################################ 
    
    input_file2 = open('oil.txt', 'r')
    lines2 = input_file2.readlines()

    
    for i in range(1, 19):     
            date2.append(lines2[i][:10])
            volume2.append(lines2[i][16:-1])
            
            if i == 8 or i == 15: 
              oil2.append(lines2[i][11:15])

            #elif i != 8 or i != 15: 
            else:
             oil2.append(lines2[i][11:17]) 
             
            
       
    for i in range(0,18):
             if comma not in volume2[i]:
               volume_modified2.append(volume2[i])
             elif comma in volume2[i]:
                for v in range(0,6):
                 if volume2[i][v] == comma:
                     volume2[i] = volume2[i][v:]
                     volume_modified2.append(volume2[i].replace(',', ''))
             else:
                print('No need for editing the content on volume list .. ')
                
     
    for k in range(0,18): 
             if comma not in oil2[k]:
                 oil_modified2.append(oil2[k])   
             elif comma in oil2[k]:
              itemo = oil2[k].replace(',' , '')
              oil_modified2.append(itemo)                    
             else:
              print('No need for editing the content on oil list .. ')
                
            
    for i in range(0,18):
          oilDictF[date2[i]] = [oil_modified2[i], volume_modified2[i]]
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
             if oil_Date not in oilDictF:
                 print('\nInvalid input, please type in again a date in the right format ..')
                 oil_Date = input('Type in a date now (Example: 2022/02/28):  ')
             else:
                 value = input('Please type in either Price or Contracts: ').capitalize()
                 while value not in ('Price', 'Contracts'):
                     print(
                         '\nInvalid input or date was not registered, please type in again either Price or Contracts ..')
                     value = input('Please type in here either Price or Contracts: ').capitalize()
                 if value == 'Price':
                     print('\n\nThe oil price was {} $ on {}.'
                           .format(oilDictF[oil_Date][0], oil_Date))
                 else:
                     print('\n\nThere were {} oil contracts on {}.'
                           .format(oilDictF[oil_Date][1], oil_Date))
                 oil_Date = input('Type in a new date to access information (Example: 2022/02/28):  ')


###############################################################################
#############################  EXIT ###########################################
###############################################################################

 elif oilInput == "":  
     pass
    
  
    












oilInputFunc()

input_file.close()
input_file2.close()
output_file.close()

      
 