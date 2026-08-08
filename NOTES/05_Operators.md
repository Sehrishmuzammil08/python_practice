# Python Operators — Notes

**Operators** are `symbols used to perform operations on variables and values`in Python. 
The values operators act on are called **operands**.

Example: In 5 + 3, '+' is the operator and 5 and 3 are operands.
---

## 1. Arithmetic Operators
Used to perform mathematical calculations.

| Operator | Definition | Example | Output |
|----------|------------|---------|--------|
| `+` | Adds two values | `5 + 3` | `8` |
| `-` | Subtracts second value from first | `5 - 3` | `2` |
| `*` | Multiplies two values | `5 * 3` | `15` |
| `/` | Divides first value by second, returns a float | `5 / 3` | `1.666...` |
| `//` | Floor division — divides and removes the decimal part | `5 // 3` | `1` |
| `%` | Modulus — returns the remainder of division | `5 % 3` | `2` |
| `**` | Exponentiation — raises first value to the power of second | `5 ** 3` | `125` |

---

## 2. Comparison (Relational) Operators
Compare two values and always return `True` or `False`.

| Operator | Definition | Example | Output |
|----------|------------|---------|--------|
| `==` | Checks if two values are equal | `5 == 3` | `False` |
| `!=` | Checks if two values are not equal | `5 != 3` | `True` |
| `>` | Checks if left value is greater | `5 > 3` | `True` |
| `<` | Checks if left value is smaller | `5 < 3` | `False` |
| `>=` | Checks if left value is greater than or equal | `5 >= 5` | `True` |
| `<=` | Checks if left value is smaller than or equal | `5 <= 3` | `False` |

> **Note:** `=` assigns a value, while `==` compares values.

---

## 3. Logical Operators
Combine multiple conditions to make decisions.

| Operator | Definition | Example | Output |
|----------|------------|---------|--------|
| `and` | True only if both conditions are true | `(5 > 3) and (2 > 1)` | `True` |
| `or` | True if at least one condition is true | `(5 > 3) or (2 < 1)` | `True` |
| `not` | Reverses the boolean result | `not(5 > 3)` | `False` |

---

## 4. Assignment Operators
Used to store or update values in variables.

| Operator | Definition | Example | Result |
|----------|------------|---------|--------|
| `=` | Assigns a value to a variable | `x = 10` | `x = 10` |
| `+=` | Adds and assigns (`x = x + b`) | `x += 3` | `x = 13` |
| `-=` | Subtracts and assigns (`x = x - b`) | `x -= 2` | `x = 11` |
| `*=` | Multiplies and assigns (`x = x * b`) | `x *= 2` | `x = 22` |
| `/=` | Divides and assigns (`x = x / b`) | `x /= 3` | `x = 7.33` |

---

## 5. Identity Operators
Check whether two variables refer to the **same object** in memory.

| Operator | Definition | Example | Output |
|----------|------------|---------|--------|
| `is` | Checks if both refer to the same object | `a = [1,2]; b = a; a is b` | `True` |
| `is not` | Checks if they refer to different objects | `a = [1,2]; b = [1,2]; a is not b` | `True` |


a == b   # checks values

a is b   # checks same object

---

## 6. Membership Operators
Check whether a value exists inside a sequence (string, list, etc.).

| Operator | Definition | Example | Output |
|----------|------------|---------|--------|
| `in` | Checks if a value exists in the sequence | `"P" in "Python"` | `True` |
| `not in` | Checks if a value does not exist in the sequence | `"z" not in "Python"` | `True` |

---

## Order of Precedence
- ()   Parentheses
- **  Exponentiation
- *, /, //, %
- +, -
- Comparison operators
- Logical operators
- 
Example
result = 2 + 3 * 4
print(result)

Output:

14

Multiplication is performed before addition.

---

## Summary
- **Arithmetic** → perform calculations
- **Comparison** → return `True`/`False`
- **Logical** → combine conditions
- **Assignment** → store/update variables
- **Identity** → compare memory locations
- **Membership** → check existence in a sequence
