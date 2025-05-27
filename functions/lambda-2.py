f = lambda a, b: a + b
print(f)

def identity(rows, cols):
    return [
        [1 if col == row else 0 for col in range(cols)]
        for row in  range(rows)
    ]

print(identity(3,3))


f = lambda rows, cols: [
    [1 if col == row else 0 for col in range(cols)]
    for row in  range(rows)
]

print(f(3,3))


#code3
f  = lambda a=1, *args : a *  max(args)

print(f(2,1,2,3))