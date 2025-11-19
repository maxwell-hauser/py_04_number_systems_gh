# Chapter 4: Number Systems

## Overview

This chapter explores various number systems used in computing and digital electronics. Understanding different bases is essential for working with computer systems, as they use multiple representations for efficiency and readability.

## Key Concepts

### Number System Fundamentals

#### Base (Radix)
- **Definition:** The number of unique digits used in a number system
- **Positional Notation:** Each position represents a power of the base
- **General Form:** (d_n × base^n) + (d_(n-1) × base^(n-1)) + ... + (d_1 × base^1) + (d_0 × base^0)

### The Four Major Number Systems

#### 1. Decimal (Base-10)
- **Digits:** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Base:** 10
- **Usage:** Human counting, everyday mathematics
- **Example:** 365₁₀ = (3×10²) + (6×10¹) + (5×10⁰) = 300 + 60 + 5

#### 2. Binary (Base-2)
- **Digits:** 0, 1
- **Base:** 2
- **Usage:** Fundamental computer representation, digital logic
- **Prefix:** 0b (e.g., 0b1010)
- **Example:** 1011₂ = (1×2³) + (0×2²) + (1×2¹) + (1×2⁰) = 8 + 0 + 2 + 1 = 11₁₀

#### 3. Octal (Base-8)
- **Digits:** 0, 1, 2, 3, 4, 5, 6, 7
- **Base:** 8
- **Usage:** Unix/Linux file permissions, compact binary representation
- **Prefix:** 0o (e.g., 0o755)
- **Example:** 127₈ = (1×8²) + (2×8¹) + (7×8⁰) = 64 + 16 + 7 = 87₁₀
- **Binary Grouping:** Each octal digit represents 3 binary bits

#### 4. Hexadecimal (Base-16)
- **Digits:** 0-9, A-F (where A=10, B=11, C=12, D=13, E=14, F=15)
- **Base:** 16
- **Usage:** Memory addresses, color codes, compact binary notation
- **Prefix:** 0x (e.g., 0xFF)
- **Example:** 2A3₁₆ = (2×16²) + (10×16¹) + (3×16⁰) = 512 + 160 + 3 = 675₁₀
- **Binary Grouping:** Each hex digit represents 4 binary bits

## Binary-Octal-Hex Relationship

### Quick Conversion Guide

```
Binary (4 bits) → Hex (1 digit)
Binary (3 bits) → Octal (1 digit)

Example:
Binary:  1111 0101 1010 0011
Hex:     F    5    A    3     = 0xF5A3
         
Binary:  001 111 010 110 100 011
Octal:   1   7   2   6   4   3  = 0o172643
```

### Conversion Table

| Decimal | Binary | Octal | Hexadecimal |
|---------|--------|-------|-------------|
| 0       | 0000   | 0     | 0           |
| 1       | 0001   | 1     | 1           |
| 2       | 0010   | 2     | 2           |
| 3       | 0011   | 3     | 3           |
| 4       | 0100   | 4     | 4           |
| 5       | 0101   | 5     | 5           |
| 6       | 0110   | 6     | 6           |
| 7       | 0111   | 7     | 7           |
| 8       | 1000   | 10    | 8           |
| 9       | 1001   | 11    | 9           |
| 10      | 1010   | 12    | A           |
| 11      | 1011   | 13    | B           |
| 12      | 1100   | 14    | C           |
| 13      | 1101   | 15    | D           |
| 14      | 1110   | 16    | E           |
| 15      | 1111   | 17    | F           |

## Learning Objectives

By the end of this chapter, you should be able to:
- Understand positional notation and its application to any base
- Work with binary, octal, decimal, and hexadecimal number systems
- Recognize the relationship between binary, octal, and hexadecimal
- Convert numbers between different bases (covered in detail in Chapter 5)
- Explain why different number systems are used in computing

## Python Example

Run the interactive example:

```bash
python ch04_number_systems.py
```

### What the Example Demonstrates

1. **Positional Notation:** Understanding place values in different bases
2. **Base Conversion:** Converting between binary, octal, decimal, and hex
3. **Binary Representation:** How numbers are stored in computers
4. **Hexadecimal Usage:** Memory addresses and compact notation
5. **Octal in Practice:** File permissions and legacy systems
6. **Number Validation:** Checking if digits are valid for a given base

### Sample Output

```
============================================================
CHAPTER 4: Number Systems
============================================================

--- Example 1: Decimal Number in Different Bases ---
Decimal: 255
Binary:  0b11111111 (8 bits)
Octal:   0o377
Hex:     0xFF

--- Example 2: Positional Notation Breakdown ---
Decimal 1234:
  1×10³ + 2×10² + 3×10¹ + 4×10⁰
  1000 + 200 + 30 + 4 = 1234
...
```

## Real-World Applications

### Binary Applications
- **Computer Memory:** All data stored as binary
- **Logic Circuits:** Digital gates operate on binary values
- **Boolean Algebra:** True/False represented as 1/0
- **Network Protocols:** IP addresses, subnet masks

### Octal Applications
- **Unix/Linux Permissions:** chmod 755 (rwxr-xr-x)
- **Legacy Systems:** Older computer systems and documentation
- **Digital Electronics:** Some early computer designs
- **Compact Binary:** Easier to read than long binary strings

### Hexadecimal Applications
- **Memory Addresses:** 0x00400000
- **Color Codes:** #FF5733 (web colors: RRGGBB)
- **MAC Addresses:** 00:1A:2B:3C:4D:5E
- **Assembly Language:** Machine code representation
- **Debugging:** Memory dumps and error codes
- **File Formats:** Magic numbers and headers

### Decimal Applications
- **User Interfaces:** Human-readable numbers
- **Financial Calculations:** Money and accounting
- **Scientific Notation:** Large and small numbers
- **Everyday Computing:** File sizes, statistics

## Why Multiple Number Systems?

### Binary: Computer's Native Language
- Electronic circuits naturally have two states
- Simple and reliable digital logic
- Basis for all digital computing

### Hexadecimal: Human-Friendly Binary
- Compact representation (1 hex digit = 4 binary bits)
- Easier to read and write than long binary strings
- Direct mapping to binary makes conversion trivial
- Standard in programming and debugging

### Octal: Historical and Specialized Use
- Simpler than hex but more compact than binary
- Used in Unix/Linux permissions
- Each digit represents 3 bits
- Common in older systems (PDP-8, etc.)

### Decimal: Human Standard
- What we learn from childhood
- Natural for human communication
- Interface between humans and computers

## Common Questions

**Q: Why is hexadecimal more popular than octal in modern computing?**  
A: Hexadecimal aligns perfectly with byte boundaries (2 hex digits = 1 byte), making it ideal for memory addresses and data representation in 8, 16, 32, and 64-bit systems.

**Q: How do I know which number system is being used?**  
A: By convention: 0b for binary, 0o for octal, 0x for hexadecimal, or subscript notation like ₂, ₈, ₁₆. Decimal usually has no prefix.

**Q: Can we have a base-3 or base-7 number system?**  
A: Yes! Any positive integer can be a base. However, powers of 2 (like 2, 8, 16) are most useful in computing due to their relationship with binary.

**Q: Why do programmers joke that "there are 10 types of people"?**  
A: Because in binary, "10" means 2 in decimal! The joke is: "There are 10 types of people: those who understand binary and those who don't."

## Number System Comparison

| Feature | Binary | Octal | Decimal | Hexadecimal |
|---------|--------|-------|---------|-------------|
| **Base** | 2 | 8 | 10 | 16 |
| **Digits** | 0-1 | 0-7 | 0-9 | 0-9, A-F |
| **Compactness** | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Human Friendly** | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Computer Native** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐⭐ |
| **Bits per Digit** | 1 | 3 | ~3.32 | 4 |

## Key Takeaways

- Different number systems use different bases (radix)
- Binary (base-2) is fundamental to all computing
- Hexadecimal (base-16) is the most common compact notation
- Octal (base-8) is used in Unix/Linux permissions
- 📐 Positional notation applies to all number systems
- Easy conversion exists between binary, octal, and hex
- Each system has specific use cases and advantages

## Practice Exercises

1. Convert decimal 100 to binary, octal, and hexadecimal
2. What is the decimal value of 0xFF?
3. Convert binary 11010110 to octal and hexadecimal
4. Express the hexadecimal color code #A52A2A in binary
5. If a Unix file has permissions 644, what does this mean in binary?
6. What is the largest 8-bit binary number in hexadecimal?
7. Count from 0 to 20 in binary
8. Write your age in binary, octal, and hexadecimal

## Further Study

- Learn detailed conversion techniques in Chapter 5
- Study binary arithmetic in Chapter 8
- Explore computer memory organization
- Investigate floating-point representation (Chapter 9)
- Learn about ASCII and character encoding (Chapter 11)

---

**Course Navigation:**  
← Previous: [Chapter 3 - Digital Signals](../ch3_digital_signals/) | Next: [Chapter 5 - Number System Conversions](../ch5_conversions/) →
