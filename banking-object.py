class dog:
    kind = 'kanine'
    def __init__(self, name):
        self.name = name

d = dog('Chika')
o = dog('Dahi')

print(d.kind)
print(d.name)
print(o.kind)
print(o.name)
