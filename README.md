# URM

An unlimited register machine implementation in Python.


## Introduction

An unlimited register machine (URM) is a Turing-complete model of computation which resembles a rudimentary assembly language. It's often used in theoretical computer science during proofs as a stand-in for Turing machines due to it's more familiar syntax. The code below implements a URM program which computes `r2 = r0 + r1` where `r0`, `r1` and `r2` are the first, second and third registers respectively. In total there are an unlimited number of registers to select from (hence the name).

```py
# r2 = r0 + r1

m 0 2
z 3
s 2
s 3
j 3 1 6
j 0 0 2
x
```

## Instruction Set

This implementation supports just four simple instructions. These instructions are sufficient for Turing completeness.

### Zero 

Sets the value of register `n` to zero.

```
z <n> 
```

### Successor 

Increments the value of register `n` by 1.

```
s <n>
```

### Move

Copies the value of register `n` into register `m`. 

```
m <n> <m>
```

### Jump

Branches execution to instruction `i` if the value of register `n` equals the value of register `m`. 

```
j <n> <m> <i>
```

## API

URM exposes a simple interface for executing URM programs; namely through the `UnlimitedRegisterMachine.execute()` method.

```py
from urm import UnlimitedRegisterMachine

i, registers = UnlimitedRegisterMachine.execute(<register map>, <code>)
```

This method takes in a register map and source code string, and returns a new register map as well as the instruction index at which the program terminated. Here's an example using the addition program shown in the introduction.

```py
from urm import UnlimitedRegisterMachine

addition = '''m 0 2
z 3
s 2
s 3
j 3 1 6
j 0 0 2
x'''

x = 1
y = 2

_, registers = UnlimitedRegisterMachine.execute({ 0: x, 1: y }, addition)
z = registers[2]
```

## Conclusion

URMs are useful constructions for theoretical computer scientists. This Python package aims to make them more concrete for research or fun.
