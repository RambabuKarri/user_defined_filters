from django import template
register=template.Library()



@register.filter()
def swap(data):
    return data.swapcase()


@register.filter()
def remove(data,arg):
    return data.replace(arg,'')


@register.filter()
def count(data,arg):
    c=0
    for i in range(len(data)):
        if data[i:i+len(arg):]==arg:
            c+=1
    return c


@register.filter()
def swapping(data):
    a=data.split()
    s=[]
    for i in range(len(a)):
        if i==0 or i==-1:
            s.append(i)
        else:
            s.append(i.lower())
    return join()
