s1="I love ICE CREAM"
rev=s1[::-1]
words=s1.lower().split(" ")
valid=""
for word in words:
    if word.find('e')!=-1:
        valid+=word+" "
  
rep=s1.replace("ICE CREAM","HOCKEY")    
print(rep)
        
print(s1.startswith("I"))
s1.endswith("M")        
print(rev)

