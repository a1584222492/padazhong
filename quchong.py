ls=[11,22,33,[44,44,[33,33],55],22,33]


def qvchong(ls):
    new_list = []
    for i in ls:
        if isinstance(i,list):
            qvchong(i)
            new_list.append(i)
        elif i not in new_list:
            new_list.append(i)
    ls.clear()
    for i in new_list:
        ls.append(i)
    return new_list
a = qvchong(ls)
print(a)

