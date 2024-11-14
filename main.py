yesno = ['yes','y','no','n']
YorN = input('Would you like to calculate your circut? y/n\n')
while YorN not in yesno:
  YorN = input('Please enter yes or no.\n')

NumConvert = 0
SorP = ''

S = ['series', 's']
P = ['parallel','p']
if YorN == 'yes' or YorN == 'y':
  a = True
  while a == True:
   SorP = input('Is your circut series or parallel?\n').lower()
   if SorP in S or SorP in P:
     print ('Excellent!')
     a = False
   elif SorP not in P or SorP not in S:
      print ('Please enter a valid answer.')

  no = False
  while no == False:
    resNumber = input('Please input the amount of resistors in your circut.\n')
    try:
      NumConvert = int(resNumber)
      if NumConvert > 0:
        no = True
      else:
        print("You need a minimun of 1 resistor.")
    except:
      print('Please enter a whole number.')

resistorList = []
for x in range(NumConvert):
  isNum = False
  while isNum == False:
    try:
      resistor = float(input(f"Enter resistor {x+1} here:\n"))
      resistorList.append(resistor)
      isNum = True
    except:
      print("Only numbers please.\n")

if SorP in S: 

  Smath = sum(resistorList)
  print('The total resistance ',Smath,' Ohms')
elif SorP in P:
  for x in range(NumConvert):
    resistorList[x]  = 1/resistorList[x]
  Pmath = 1/sum(resistorList)
  print('The total resistance ',Pmath,' Ohms')

print ('Please check folder just made for more information!')
#resistorList = []
writeFile = open("ExtraInfo.txt","a")
if SorP == "s" or SorP == "series":
  writeFile.write("\nType - Series\n")
elif SorP == "p" or SorP == "parallel":
  writeFile.write("\nType - Parallel\n")

for x in range(NumConvert):
  writeFile.write(f" Resistor {x + 1} - {resistorList[x]}\n ")
if SorP == "p" or SorP == "parallel":
  #for x in range(len(resistorList)):
    #resistorList[x] = 1/resistorList[x]

  writeFile.write(f"The total resistance is {1/sum(resistorList)} Ohms\n -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
  writeFile.close()

if SorP == "s" or SorP == "series":
 
  writeFile.write(f"The total resistance of your cirut is {sum(resistorList)} Ohms\n -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
  writeFile.close()



if YorN == 'no' or YorN == 'n':
  print ('Come again later!')
