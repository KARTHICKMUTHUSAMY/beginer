a=input()
if(a=='A' or a=='a' or a=='E' or a=='e' or a=='I' or a=='i' or a=='O' or a=='o' or a=='U' or a=='u'):
	print("Vowel")
elif((a>='a' and a<='z') or (a>='A' and a<='Z')):
    print("Consonant")
else:
	print("invalid")
