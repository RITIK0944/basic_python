# def dot(adress):
#     return adress.replace(".","[.]")
# adress="1.3.4.5"
# print(dot(adress))
def dot(adrress):
    ans=" "
    i=0
    for i in (adrress):

        if i==".":

            ans+="[.]"
        else:
            ans+=i
    return ans
adrress="1.1.1.1.1"
print(dot(adrress))
    
