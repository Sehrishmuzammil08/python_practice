# Python For Loop

## 1. Introduction to For Loop

A **for loop** is a programming structure used to repeat a block of code for each value in a sequence.

### The for loop is mainly used when:

* The number of repetitions is known.
* We want to repeat something a fixed number of times.
* We want to go through characters of a string.
* We want to generate numbers using `range()`.

Unlike a `while` loop, a `for` loop is usually cleaner and easier when the number of iterations is predictable.

---

## 2. What is a For Loop?

A **for loop** repeatedly executes a block of code for each value in a sequence.

A sequence can be:

* Numbers generated using `range()`
* Characters of a string
* Other collections of values

The loop automatically takes one value at a time from the sequence.

---

## 3. Syntax of For Loop

`for variable in sequence:`

    `# code block`

### Explanation:

* `for` → keyword that starts the loop
* `variable` → stores the value during each iteration
* `in` → connects the variable with the sequence
* `sequence` → produces values, such as `range()` or a string
* `:` → starts the loop block
* Indented code → executes for each value in the sequence

> **Important:** Proper indentation is mandatory in Python.

---

## 4. Using range() with For Loop

The most common way to use a `for` loop is with the `range()` function.

`range()` generates numbers automatically.

### Example 1: Basic range(stop)

`for i in range(5):`

    `print(i)`

### Output:

```
0
1
2
3
4
```

### Explanation:

* `range(5)` generates numbers starting from `0`.
* It stops before `5`.
* It generates: `0, 1, 2, 3, 4`.
* The loop runs 5 times.
* The stop value is excluded.

> **Important:** The stop value in `range()` is always excluded.

---

## 5. range(start, stop)

We can provide both a starting and stopping value.

### Syntax:

`range(start, stop)`

### Example: Print Numbers from 1 to 5

`for num in range(1, 6):`

    `print(num)`

### Output:
```
1
2
3
4
5
```

### Explanation:

* Start = `1`
* Stop = `6`
* Stop value `6` is excluded.
* Therefore, it prints numbers from `1` to `5`.

---

## 6. range(start, stop, step)

We can also specify how much the value should increase or decrease each time.

### Syntax:

`range(start, stop, step)`

### Example: Print Even Numbers from 0 to 10

`for even in range(0, 11, 2):`

    `print(even)`

### Output:
```
0
2
4
6
8
10
```

---

## 7. Looping Through a String

A `for` loop can be used to go through each character of a string one by one.

### Example:

`for letter in "Python":`

    `print(letter)`

### Output:
```
p
y
t
h
o
n
```

---

## 8. The break Statement

The `break` statement **immediately stops the loop**, even if the loop still has more values to process.

### Example:

`for i in range(10):`

    `if i == 4:`

        `break`

    `print(i)`

### Output:

```
0
1
2
3
```

### How it works:

* The loop starts normally.
* When `i == 4`, `break` is executed.
* The loop ends immediately.
* `4` is not printed.

### Remember:

`break` → **Stops the entire loop**

---

## 9. The continue Statement

The `continue` statement **skips the current iteration** and moves to the next iteration.

Unlike `break`, `continue` does not stop the loop completely.

### Example:

`for i in range(5):`

    `if i == 2:`

        `continue`

    `print(i)`

### Output:

```
0
1
3
4
```

### How it works:

* The loop starts normally.
* When `i == 2`, `continue` is executed.
* The current iteration is skipped.
* The loop continues with the next value.
* Therefore, `2` is not printed.

### Remember:

`continue` → **Skips the current iteration**

---

## 10. Break vs Continue

| Statement  | Purpose                                            |
| ---------- | -------------------------------------------------- |
| `break`    | Completely stops the loop                          |
| `continue` | Skips the current iteration and continues the loop |

---

## 11. For Loop Flow

Example:

`for i in range(3):`

    `print(i)`

### Execution Steps:

1. `range(3)` creates: `0, 1, 2`
2. `i = 0` → `print(0)`
3. `i = 1` → `print(1)`
4. `i = 2` → `print(2)`
5. Loop ends because there are no more values.


---

## 12. Important Rules of For Loop

* A colon `:` is required after the `for` statement.
* Proper indentation is mandatory.
* The stop value in `range()` is excluded.
* `break` stops the loop completely.
* `continue` skips the current iteration.
* The loop variable receives a new value during each iteration.

---

## 13. Common Student Mistakes in For Loops

* 1. Forgetting the Colon

* 2. Wrong Indentation

* 3. Thinking range(5) Includes 5

* 4. Using `=` Instead of `==`

* 5. Confusing break and continue


## 14. When Should You Use For Loop?

Use a **for loop** when:

* The number of repetitions is known.
* You want to use `range()`.
* You want to iterate through a string.
* Cleaner and shorter code is needed.
* You want to process each value in a sequence.

---


> **Key Point:** A `for` loop is especially useful when the number of iterations is known or when we want to process each value in a sequence.
