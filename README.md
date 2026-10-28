# Prime Number Checker

A simple Python program that checks whether an entered whole number is prime.

## How to run

Make sure Python is installed, open a terminal in this folder, and run:

```bash
python "jay,py"
```

Enter a whole number when prompted. The program prints **Prime number** if the number is prime, or **Not a prime number** otherwise.

## How it works

- Numbers less than `2` are not prime.
- For other numbers, the program checks for divisors starting at `2`.
- It only checks divisors up to the square root of the number, which avoids unnecessary checks.

## Example

```text
Enter a whole number: 17
Prime number
```
