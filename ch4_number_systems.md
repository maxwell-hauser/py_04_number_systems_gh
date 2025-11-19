# Chapter 4: Number Systems

_Originally created 14 January, 2021 by Maxwell Hauser — Updated 5 October, 2025_

_Builds upon material from Chapter 3: Digital Signals._

---

## Number Systems

Numbers can be represented in different bases (also called **radix**).

Consider the following number in decimal:
```
356 = 6      + 50     + 300
    = 6*10^0 + 5*10^1 + 3*10^2
```

356 has a base of 10, or more commonly called **decimal**.

In general, a number $N$ can be represented in the form:

$$N = (a_n \times r^n) + (a_{(n-1)} \times r^{(n-1)}) + ... + (a_2 \times r^2) + (a_1 \times r^1) + (a_0 \times r^0) + (a_{(-1)} \times r^{(-1)}) + (a_{(-2)} \times r^{(-2)}) + ... + (a_{(-m)} \times r^{(-m)})$$

where $r$ is the base or radix, and $a_i$ are the digits (coefficients) in that base.

- For example, the binary number 1011.01 can be represented as:
    ```
    (1*2^3)
    + (0*2^2)
    + (1*2^1)
    + (1*2^0)
    + (0*2^-1)
    + (1*2^-2)
    = 8 + 0 + 2 + 1 + 0 + 0.25
    = 11.25 (decimal)
    ```

- Another example is the hexadecimal number 2F.3:
    ```
    (2*16^1) + (15*16^0) + (3*16^-1)
    = 32 + 15 + 0.1875
    = 47.1875 (decimal)
    ```

- $(1011.01)_2$ is a valid binary number because it only uses the digits 0 and 1, which are the only valid digits in base 2.

- $(2F.3)_{16}$ is a valid hexadecimal number because it uses the digits 0-9 and the letters A-F (where A=10, B=11, C=12, D=13, E=14, F=15), which are the valid digits in base 16.

- $(356)_{10}$ is a valid decimal number because it uses the digits 0-9, which are the valid digits in base 10.

- $(478)_8$ is not a valid octal number because it uses the digit 8, which is not a valid digit in base 8 (valid digits are 0-7).

- The following formula can be used to convert a number in a given base to decimal by evaluating the sum:
    > <img src="img/ch4_img1.png" alt="Description" width="400" />

### Examples

**Example 1:** Convert $(27.35)_8$ to base 10.

$$(27.35)_8 = (2 \times 8^1) + (7 \times 8^0) + (3 \times 8^{-1}) + (5 \times 8^{-2})$$
$$= 16 + 7 + 0.375 + 0.078125$$
$$= (23.453125)_{10}$$

**Example 2:** Convert $(1101111)_2$ to decimal.

$$(1101111)_2 = 1 \times 2^0 + 1 \times 2^1 + 1 \times 2^2 + 1 \times 2^3 + 0 \times 2^4 + 1 \times 2^5 + 1 \times 2^6$$
$$= 1 + 2 + 4 + 8 + 32 + 64$$
$$= (111)_{10}$$

**Example 3:** Convert $(345)_6$ to decimal.

$$(345)_6 = (3 \times 6^2) + (4 \times 6^1) + (5 \times 6^0)$$
$$= 108 + 24 + 5$$
$$= (137)_{10}$$

4. Convert (123.45)7 to decimal:
    ```
    (123.45)7 = (1*7^2) + (2*7^1) + (3*7^0) + (4*7^-1) + (5*7^-2)
    = 49 + 14 + 3 + 0.571428 + 0.102041
    = 66.673469 (decimal)
    ```

5. Convert (234.56)9 to decimal:
    ```
    (234.56)9 = (2*9^2) + (3*9^1) + (4*9^0) + (5*9^-1) + (6*9^-2)
    = 162 + 27 + 4 + 0.555555 + 0.012345
    = 193.568901 (decimal)
    ```

---

## Summary

1. Numbers can be represented in different bases (radix).
2. Common bases include:
   - Decimal (base 10): digits 0-9
   - Binary (base 2): digits 0-1
   - Octal (base 8): digits 0-7
   - Hexadecimal (base 16): digits 0-9, A-F
3. To convert from any base to decimal, multiply each digit by the base raised to its position power and sum the results.
4. A number is valid in a base only if all its digits are less than the base.
