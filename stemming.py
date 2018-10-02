A = ['wanted','wanting','jumped','students','student', 'jumping',"Rick",'astronomy']
C=[]

def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

for w in A:
    B= stem(w)
    C.append(B)

print (C)

def count_elements(lst):
    elements={}
    for elem in lst:
        if elem in elements.keys():
            elements[elem]+=1
        else:
            elements[elem]= 1
    return elements

print(count_elements(C))



