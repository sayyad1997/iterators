try:
    my_list=[45,675,343,5343]
    x=iter(my_list)

    for i in range (len(my_list)):
        print(next(x))

except StopIteration:
    print("enter more values in list")




try:
    x=[12,24,345,23,64,5433]
    y=iter(x)

    for i in range(len(x)):
        print(next(y))
except StopIteration:
    print("plz enter the more values in the list")
finally:
    print("good !!!")