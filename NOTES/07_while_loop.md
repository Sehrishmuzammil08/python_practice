# Python While Loop

## 1. Introduction to Loops

A **loop** is a programming structure that allows a block of code to execute repeatedly based on a condition. Loops help automate repetitive tasks instead of writing the same code multiple times.

### Loops are commonly used when:

* Repeating an action multiple times
* Processing items in a sequence
* Waiting for a condition to change

### Main Types of Loops in Python:

* `for` loop
* `while` loop

---

## 2. What is a While Loop?

A **while loop** repeatedly executes a block of code as long as a specified condition remains `True`.

The condition is checked before every iteration:

* If the condition is `True` → the loop runs.
* If the condition is `False` → the loop stops.

A `while` loop is useful when the number of repetitions is **not fixed in advance**.

---

## 3. Syntax of While Loop

```python
while condition:
    # code block
```

### Explanation:

* `while` → keyword that starts the loop
* `condition` → Boolean expression (`True` / `False`)
* `:` → starts the loop block
* Indented code → executes repeatedly while the condition is `True`

> **Important:** Proper indentation is mandatory in Python.

---

## 4. Example: Print Numbers from 1 to 5

```python
num = 1

while num <= 5:
    print(num)
    num = num + 1
```

### Output:

```text
1
2
3
4
5
```

### How it works:

1. `num` starts at `1`.
2. The condition `num <= 5` is checked.
3. The number is printed.
4. `num` increases by `1`.
5. The process repeats.
6. When `num` becomes `6`, the condition becomes `False` and the loop stops.

---

## 5. Countdown Program

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Time's up!")
```

### Output:

```text
5
4
3
2
1
Time's up!
```

### Important:

`count -= 1` is a short form of:

```python
count = count - 1
```

---

## 6. Break Statement

The `break` statement **immediately stops the loop**, even if the loop condition is still `True`.

It is commonly used for:

* Taking user input
* Searching for a value
* Stopping a loop when a condition is met

### Example:

```python
while True:
    num = int(input("Enter number (0 to stop): "))

    if num == 0:
        break

    print("You entered:", num)
```

### How it works:

* `while True` creates an infinite loop.
* The user enters numbers.
* If the user enters `0`, `break` stops the loop.
* Otherwise, the entered number is printed.

---

## 7. Continue Statement

The `continue` statement **skips the current iteration** and moves to the next loop cycle.

Unlike `break`, `continue` **does not stop the loop completely**.

### Example:

```python
num = 0

while num < 5:
    num += 1

    if num == 3:
        continue

    print(num)
```

### Output:

```text
1
2
4
5
```

Here, `3` is skipped because `continue` moves directly to the next iteration.

---

## 8. Break vs Continue

| Statement  | Purpose                                            |
| ---------- | -------------------------------------------------- |
| `break`    | Completely stops the loop                          |
| `continue` | Skips the current iteration and continues the loop |

---

## 9. Common Mistakes in While Loops

### 1. Forgetting to Update the Variable

If the loop variable is not updated, the condition may never become `False`, causing an **infinite loop**.

### 2. Wrong Indentation

Python requires correct indentation. Incorrect indentation can cause errors.

### 3. Incorrect Condition

An incorrect condition may:

* Prevent the loop from running
* Cause an infinite loop

---

## Summary

In this topic, we learned:

* What a `while` loop is
* How a `while` loop works
* Syntax of a `while` loop
* How to create a countdown
* `break` statement
* `continue` statement
* Common mistakes in `while` loops

> **Key Point:** A `while` loop is especially useful when the number of iterations is unknown and depends on a condition.
