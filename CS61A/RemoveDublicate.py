Remove duplicate chars from a string ("AAABBB" -> "A B")
i=0
str="AAABaBBCbCCc"
str2=""
while i in range (len(str)):
    s=str[i]
    if  s.lower() in str2.lower(): 
        i=i+1
    else:
        str2=str2+str[i]

******************************************
'Hassan' 
