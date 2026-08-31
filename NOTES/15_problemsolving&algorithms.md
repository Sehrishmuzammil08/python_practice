# Problem Solving & Algorithms 

## 1. Introduction to Problem Solving

### What is Problem Solving?
Problem solving in programming is the process of:
1. Understanding a problem
2. Planning a solution
3. Writing the solution as an algorithm
4. Implementing the solution in code
5. Testing and improving the solution

### Real-Life Analogy
Imagine making tea:
1. Boil water
2. Add tea leaves
3. Add sugar
4. Pour into cup
5. Serve

These steps form an algorithm because they are **ordered instructions**.

---

## 2. Understanding Algorithms

### What is an Algorithm?
An algorithm is a **step-by-step procedure** used to solve a problem.

### Characteristics of a Good Algorithm
A good algorithm should:
1. Be clear and understandable
2. Have definite steps
3. Solve the problem correctly
4. Finish in finite time
5. Be efficient

---

## 3. Steps in Problem Solving

### Step 1: Understand the Problem
Questions to ask:
- What is the input?
- What is the expected output?
- What rules or conditions exist?

**Example**

Problem: Calculate the area of a rectangle.

- **Input:** Length, Width
- **Output:** Area
- **Formula:** `Area = Length × Width`

### Step 2: Plan the Solution
Break the problem into smaller tasks.

**Example Plan**
1. Get length from user
2. Get width from user
3. Multiply length and width
4. Display area

### Step 3: Design the Algorithm

**Pseudocode Example**
```
START
INPUT length
INPUT width
area = length × width
DISPLAY area
END
```

### Step 4: Implement in Code
```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)
```

### Step 5: Test the Solution

**Test Case**
```
Input: Length = 5, Width = 4
Expected Output: Area = 20
```

---

## Quick Recap
- Problem solving follows a fixed cycle: **understand → plan → design (algorithm) → implement (code) → test**.
- An algorithm is just an ordered set of clear, finite, correct, and efficient steps.
- Before writing any code, always ask: *what's the input, what's the expected output, and what are the rules?*
- Designing the algorithm (often as pseudocode) **before** coding makes the actual implementation much faster and less error-prone.
- Always test with a known input/output pair to confirm the solution actually works.
