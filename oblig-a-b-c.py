# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:35:52 2022

@author: saris
"""

''' Del (a) '''

# Opening the file and reading the data
input_file = open('oil_raw_data.txt', 'r')
lines = input_file.readlines()
input_file.close()
  
# Storing date, oil and volume in three lists 
date= []; oil= []; volume= []
comma= ','; space= ' ';
        
for i in range(1, 20): 
    
    date.append(lines[i][2:12])
    volume.append(lines[i][22:-1])
    
    if i == 8 or i == 15: 
      oil.append(lines[i][16:20])

    #elif i != 8 or i != 15: 
    else:
     oil.append(lines[i][16:22])  
    
   
          
''' Del (b)  '''

# Removing the blank spaces
volume_modified=[]
for i in range(0,19): 
    
  if comma not in volume[i]:
   volume_modified.append(volume[i])
     
  else:
    itemv = volume[i].replace(',' , '')
    volume_modified.append(itemv)
                  

 # Changing the format to year/month/date 
oil_modified=[]
for k in range(0,19): 
 if comma not in oil[k]:
     oil_modified.append(oil[k])   
 elif comma in oil[k]:
  itemo = oil[k].replace(',' , '')
  oil_modified.append(itemo)                    
 else:
  print('No need for editing the content on oil list .. ')
   
date_modified =[]     
for d in range(0, 19):
 date_modified.append(date[d][-4:] + "/" +date[d][:2]+ "/" + date[d][-7:-5])
  
''' Del (c) '''
# Wrtiting the list to "oil.txt", separated by comma
output_file = open('oil.txt', 'w')
output_file.write('date, oil, volume \n')
for i in range(0,19): 
 output_file.write('{},{},{}\n' .format(date_modified[i],oil_modified[i],volume_modified[i]))
output_file.close()




  
