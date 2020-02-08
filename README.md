# BitJoy
Bit and Logical Gates Abstraction

## About
Repository to 'Padrões de Projeto' subject at university. A height level Bit and logical circuits abstractions.

## Usage
### Starting
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


### Adders
For arithmetic operators, the class `Adder` has two method to make additions:  
`half`: to [half-adder](https://www.gatevidyalay.com/half-adder/)  
`full`: to [full-adder](https://www.gatevidyalay.com/full-adder/)  
