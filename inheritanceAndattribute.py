class A:
    z = -1

    def f(self, x):
        return B(x - 1)


class B(A):
    n = 4

    def __init__(self, y):
        print("EXE", y, self)
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)


class C(B):
    def f(self, x):
        print("aaa")
        return x


b = B(1)
print(b.z, b.z.z, b.z.z.z)





a = A()
b.n = 5
print(C(2).n)  # 4


print(a.z, C.z)  # True