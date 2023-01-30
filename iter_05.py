try:
    list=[12,454,"rftrtg",776,4]
    x=iter(list)

    for i in range(len(list)):
        print(next(x))

except StopIteration:
    print("enter the more values in list")

finally:
    print("all the best @@@~~~!!@")
