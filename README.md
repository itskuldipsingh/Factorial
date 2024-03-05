 # Factorial Calculator

**This Python program calculates the factorial of a given number.**

## Getting Started

1. **Make sure you have Python installed.** If not, download it from [https://www.python.org/](https://www.python.org/).
2. **Save this code as [script.py](https://github.com/itskuldipsingh/Factorial/blob/main/script.py).**
3. **Run the program from your terminal or command prompt using:**

   ```bash
   python factorial.py
   ```

## Usage

1. **The program will prompt you to enter a number.**
2. **Type a positive integer and press Enter.**
3. **The program will calculate the factorial of that number and display the result.**

## Example

```
Enter factorial number: 5
5! = 120
```

## Code Explanation

The code works as follows:

1. **Prompts the user for input:**
   ```python
   a = int(input("Enter factorial number: "))
   ```
2. **Initializes variables:**
   ```python
   b = 1  # Counter variable
   c = 1  # Result variable
   ```
3. **Calculates factorial using a while loop:**
   ```python
   while b <= a:
       c *= b
       b += 1
   ```
4. **Prints the result:**
   ```python
   print(f"{a}! = {c}")
   ```

## Additional Notes

- **Factorials grow very quickly.** For large numbers, the program may take some time to calculate the result.
- **For more complex mathematical operations,** consider using libraries like NumPy.
