# start

# 1:

# a:
Ninety_nine:tuple[int]=(99)
print(Ninety_nine)

# b:
tup:tuple[int,int,int]=(99,88,77)
print(tup)

# c:

def tup (t:tuple[int,int,int]):
    return len(t)

print(tup((5,8,90)))

# d:
def tup_two (tup1:tuple[int,int,int],tup2:tuple[int,int,int]):
    return tup1+tup2
print(tup_two((12,45,78),(1,67,89)))

# e:

def tup_three(tup1:tuple[int],tup2:tuple[int])-> tuple[int]:
    a: list = []
    for i in tup1:
        if i in tup2:
            a.append(i)
    x=tuple(a)
    return x

print(tup_three((1,2,3,4),(3,4,5,6)))

# f:


def tup_four(tup1:tuple[int],tup2:tuple[int]):
    a:list[int]=[]
    for i in tup1:
        if i not in tup2:
            a.append(i)

    for i in tup2:
        if i not in tup1:
            a.append(i)

    re: tuple[int] = a
    return re

print(tup_four((1,2,3,4),(3,4,5,6)))






# g:
#
def tup_in(tup4:tuple[int],index):
       if index in tup4:
           return index
       else:
           None

print(tup_in((1,2,3,4,78),6))



# h:
def tup_sort(t:tuple[int,int,int,int,int,int]):
    return sorted(t)

print(tup_sort((567,56,4,12,67,89)))

# # i:
def tup_k(u:tuple[int,int,int]):
    return u*3

print(tup_k((1,5,9)))
#
# j:
def tup_num(tup7:tuple[int,], num=int):
    list7:list[int]=[]
    for x in tup7:
        if x != num:
            list7.append(x)
    tuple1:tuple[int]=list7
    return tuple1



print(tup_num((1,2,5,7,10,10) ,10))


# k:
def tup_2(tup:tuple[int])->tuple[int]:
    list1:list[int]=[]
    list2:list[int]=[]
    for i in tup:
        list1.append(i)
    for u in list1:
        if not u in list2:
            list2.append(u)

    tup9:tuple[int]=list2
    return tup9

print(tup_2((1,8,90,45,1)))

# m:

mi:list[str]=[]
while True:
    m_name: str = str(input("waht is name?"))
    if m_name== "done":
        break
    mi.append(m_name)
print(mi)

sr:tuple[str]=mi

mg:list[int]=[]
while True:
    m_g: int = int(input("waht is g?"))
    if m_g==-999:
        break
    mg.append(m_g)
print(mg)
sw:tuple[str]=mg
list_tuple: tuple[tuple[any]] = tuple(zip(sr,sw))
print(list_tuple)

# 2:
# ב tuple זה רשימה שאין בה אפשרות לבצע שינויים אלה היא נסגרת ובטוחה בערכים הקיימים בה , ולכן נעדיף להשתמש בה בזמן שאנו יודעים שזו הרשימה שאנו רוצים ואין שינוי והיא בטוחה שלא יקרה חלילה ברשימה הזו  שינוי

# מתורגם באנגלית:
# In a tuple, this is a list in which it is not possible to make these changes, it closes and is safe in the values
# ​​that exist in it, so we prefer to use it while we know that this is the list we want and there is no change and it is certain that, God forbid, a change will not happen in this list


# 3:

# כי ב tuple יש אפשרות לציין בתוכו רשימה או מילון ואפשר לבצע שיניוים בתוך רשימה או המילון ולעשות את כל הפעלות שאפשריות ברשימה ובמילון אבל מחוץ לה אין אפשרות
# וגם אם יהיה רשימה שאין בה ערך עדיין תהיה רשימה ריקה , כי אין אפשרות לשנות אבל מבחינת ה tuple רשימה זה חלק מאינדקס שלה חלק מערך שלה ולכן אין אפשרות לשנות

# מתורגם באנגלית:
# because in a tuple it is possible to specify a list or a dictionary inside it and you can make changes inside
# the list or the dictionary and do all the operations possible in the list and the dictionary but outside of it there is no option
# stopp
