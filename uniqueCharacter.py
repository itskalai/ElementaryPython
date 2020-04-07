#Brute force unique character 


def isUniq(str):
  for ch in range(len(str)):
    for chnxt in range(ch+1,len(str)):
      #anytime two characters are the same, return false
      if str[ch] == str[chnxt]:
        print(str[ch],str[chnxt])
        return False
  return True
  
#Driver code 
str = input()
if (isUniq(str)):
   print("The characters of in the string", str, "are unique!")
else: 
  print("The characters of in the string", str, "are not unique.")
  
