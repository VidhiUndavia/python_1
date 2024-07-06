#find out how many vowel and consonent available in given string

def vowel(str):
    vowel=['a','e','o','i','u']
    vowelcount=0
    consonentcount=0
    spacecount=0
    for i in str:
        if i in vowel:
            vowelcount+=1
        
        elif i==' ':
            spacecount+=1
        else:
            consonentcount+=1
    print("Vowel = ",vowelcount," Consonent = ",consonentcount," Space = ",spacecount)


str=input("Enter the string = ")
vowel(str)