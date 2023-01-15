from urm import UnlimitedRegisterMachine


# A program to compute r2 = r0 + r1

addition = '''
m 0 2
z 3
s 2
s 3
j 3 1 6
j 0 0 2
x
'''.strip()


# Execute the addition program with r0 = x and r1 = y.

x = 1
y = 2

_, registers = UnlimitedRegisterMachine.execute({ 0: x, 1: y }, addition)
z = registers[2]


# Verify the result.

print(f'{x} + {y} = {z}')
