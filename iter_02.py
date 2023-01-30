class KIDS:
    def __iter__(self):
        self.a=1
        return self

    def ___next__(self):
        x=self.a
        self.a+=1
        return x

z=KIDS()
y=iter(z)

print(next(y))