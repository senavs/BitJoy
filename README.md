# BitJoy
Bit, Bytes and Logical Gates Abstraction

## About
Repository to 'Padrões de Projeto' subject at university. A height level Bit/Bytes and logical circuits abstractions.

## Usage
### Starting with Bit
Importing and instantiating Bit class.
```python
from dtypes import Bit

zero = Bit(0)
# NegativeBit(0)
one = Bit(1)
# PositiveBit(1)
```
Creating a bit passing `0` in the `__init__` method, it will create another class: `NegativeBit`. The same away, passing `1`, it will create a `PositiveBit`.

### Logical Gates
There is also support to logical operators (called logical gates or logical circuits).
```python
from operators import LogicalOperator
```
- NOT
```python
LogicalOperator.not_(zero)
# PositiveBit(1)
LogicalOperator.not_(one)
# NegativeBit(0)
```
- OR
```python
LogicalOperator.or_(zero, zero)
# NegativeBit(0)
LogicalOperator.or_(zero, one)
# PositiveBit(1)
LogicalOperator.or_(one, zero)
# PositiveBit(1)
LogicalOperator.or_(one, one)
# PositiveBit(1)
```
- AND
```python
LogicalOperator.and_(zero, zero)
# NegativeBit(0)
LogicalOperator.and_(zero, one)
# NegativeBit(0)
LogicalOperator.and_(one, zero)
# NegativeBit(0)
LogicalOperator.and_(one, one)
# PositiveBit(1)
```
There is also support to others Logical Gates:  
`nand_`, `xor_` and `xnor_`

### Bytes
There is also a Bytes class.
```python
from dtypes import Bytes
```
Passing a list of Bit to the Bytes' constructor to creating a bytes instance. *NOTE that bytes only have 8 bits. So passing more or less it'll throw an error.*
```python
bits = [Bit(0), Bit(0), Bit(0), Bit(0), Bit(1), Bit(1), Bit(0), Bit(0)]
b = Bytes(bits)
# Bytes(0, 0, 0, 0, 1, 1, 0, 0)
```
To creating a easy bytes, use `int_to_bytes` function from `utils` to help.
```python
from utils.functions import int_to_bytes

b1 = int_to_bytes(10)
# Bytes(0, 0, 0, 0, 1, 0, 1, 0)
b2 = int_to_bytes(175)
# Bytes(1, 0, 1, 0, 1, 1, 1, 1)
```
- Adding Bytes
Bytes class also has support to `+` operand with `__add__` method.
```python
b1_b2 = b1 + b2
# Bytes(1, 0, 1, 1, 1, 0, 0, 1)
```
- Casting
Bytes supports casting with other number types: `int`, `bin`, `oct` and `hex`.
```python
int(b1_b2)
# 185

bin(b1_b2)
'0b10111001'

oct(b1_b2)
'0o271'

hex(b1_b2)
'0xb9'
```

### Adders
For arithmetic operators, the class `Adder` has two method to make additions:  
`half`: to [half-adder](https://www.gatevidyalay.com/half-adder/)  
`full`: to [full-adder](https://www.gatevidyalay.com/full-adder/)  
