aN = int(input())
aList =list(map(int,input().strip().split()))
digits_vowels_Count1=[2,2,1,2,2,2,1,2,2,2,1,3,2,3,4,3,3,4,4,4,1,3,2,3,3]
digits_vowels_Count2= [3,2,3,3,3,1,3,2,3,3,3,2,3,3,3,1,3,2,3,3,3,2,3,3,3]
digits_vowels_Count3= [1,3,2,3,3,3,2,3,3,3,1,3,2,3,3,3,2,3,3,3,2,4,3,4,4]
digits_vowels_Count4= [4,3,4,4,4,2,4,3,4,4,4,3,4,4,4,2,4,3,4,4,4,3,4,4,4,2]
digits_as_String1 = ["zero","one","two","three","four","five","six","seven","eight","nine"]
digits_as_String2 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
digits_as_String3 = ["twentyone","twentytwo","twentythree","twentyfour","twentyfive","twentysix","twentyseven","twentyeight","twentynine","thirty"]
digits_as_String4 = ["thirtyone","thirtytwo","thirtythree", "thirtyfour","thirtyfive","thirtysix","thirtyseven","thirtyeight","thirtynine","forty"]
digits_as_String5 = ["fortyone","fortytwo","fortythree","fortyfour","fortyfive","fortysix","fortyseven","fortyeight","fortynine","fifty"]
digits_as_String6 = ["fiftyone","fiftytwo","fiftythree","fiftyfour","fiftyfive","fiftysix","fiftyseven","fiftyeight","fiftynine","sixty"]
digits_as_String7 = ["sixtyone","sixtytwo","sixtythree","sixtyfour","sixtyfive","sixtysix","sixtyseven","sixtyeight","sixtynine","seventy"]
digits_as_String8 = ["seventyone","seventytwo","seventythree","seventyfour","seventyfive","seventysix","seventyseven","seventyeight","seventynine","eighty"]
digits_as_String9 = ["eightyone","eightytwo","eightythree","eightyfour","eightyfive","eightysix","eightyseven","eightyeight","eightynine","ninety"]
digits_as_String10= ["ninetyone","ninetytwo","ninetythree","ninetyfour","ninetyfive","ninetysix","ninetyseven","ninetyeight","ninetynine","hundred"]
digits_vowels_Count = digits_vowels_Count1+digits_vowels_Count2+digits_vowels_Count3+digits_vowels_Count4
digits_as_String = digits_as_String1+digits_as_String2+digits_as_String3+digits_as_String4+digits_as_String5+digits_as_String6+digits_as_String7+digits_as_String8+digits_as_String9+digits_as_String10
sum_of_Vowels = 0
for a in range(aN):
    for b in str(aList[a]):
        sum_of_Vowels = sum_of_Vowels +  digits_vowels_Count[int(b)]
no_of_Pairs = 0
for c in range(aN-1):
    for d in range(c+1,aN):
        if(aList[c]+aList[d] == sum_of_Vowels):
            no_of_Pairs+=1
if(no_of_Pairs>100):
    print("greater 100")
else:
    print(digits_as_String[no_of_Pairs],end='')