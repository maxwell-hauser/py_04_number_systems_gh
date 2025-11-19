#!/usr/bin/env python3
"""
Chapter 4: Number Systems
Demonstrates different number system bases: Binary (2), Octal (8), Decimal (10), Hexadecimal (16)
"""

def any_base_to_decimal(number_str, base):
    """Convert a number from any base to decimal"""
    return int(number_str, base)

def decimal_to_any_base(decimal_num, base):
    """Convert decimal to any base (2-16)"""
    if decimal_num == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    result = ""
    num = abs(int(decimal_num))
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result

def is_valid_number(number_str, base):
    """Check if a number is valid for the given base"""
    valid_digits = "0123456789ABCDEF"[:base]
    return all(c.upper() in valid_digits for c in number_str)

def demonstrate_positional_notation(number_str, base):
    """Show the positional notation breakdown"""
    print(f"\nPositional notation for ({number_str})_{base}:")
    decimal_value = 0
    power = len(number_str) - 1
    
    for digit in number_str:
        digit_val = int(digit, base)
        place_value = digit_val * (base ** power)
        decimal_value += place_value
        print(f"  {digit} × {base}^{power} = {digit_val} × {base**power} = {place_value}")
        power -= 1
    
    print(f"  Total: {decimal_value}")
    return decimal_value

def main():
    print("=" * 60)
    print("CHAPTER 4: Number Systems")
    print("=" * 60)
    
    # Example 1: Different number bases
    print("\n--- Example 1: Number System Bases ---")
    decimal = 111
    print(f"Decimal (base 10): {decimal}")
    print(f"Binary (base 2):   {decimal_to_any_base(decimal, 2)}")
    print(f"Octal (base 8):    {decimal_to_any_base(decimal, 8)}")
    print(f"Hex (base 16):     {decimal_to_any_base(decimal, 16)}")
    
    # Example 2: Binary to Decimal with positional notation
    print("\n--- Example 2: Binary to Decimal Conversion ---")
    binary = "1101111"
    result = demonstrate_positional_notation(binary, 2)
    print(f"Result: ({binary})_2 = ({result})_10")
    
    # Example 3: Octal to Decimal
    print("\n--- Example 3: Octal to Decimal Conversion ---")
    octal = "27"
    print(f"Octal number: ({octal})_8")
    result = any_base_to_decimal(octal, 8)
    print(f"Calculation: (2 × 8^1) + (7 × 8^0)")
    print(f"           = (2 × 8) + (7 × 1)")
    print(f"           = 16 + 7")
    print(f"           = {result}")
    
    # Example 4: Hexadecimal to Decimal
    print("\n--- Example 4: Hexadecimal to Decimal Conversion ---")
    hex_num = "2F"
    print(f"Hexadecimal: ({hex_num})_16")
    print(f"Note: F in hex = 15 in decimal")
    result = any_base_to_decimal(hex_num, 16)
    print(f"Calculation: (2 × 16^1) + (15 × 16^0)")
    print(f"           = 32 + 15")
    print(f"           = {result}")
    
    # Example 5: Valid vs Invalid numbers
    print("\n--- Example 5: Number Validity Check ---")
    test_cases = [
        ("1011", 2, "Binary"),
        ("478", 8, "Octal"),
        ("345", 6, "Base-6"),
        ("ABC", 16, "Hexadecimal")
    ]
    
    for number, base, name in test_cases:
        valid = is_valid_number(number, base)
        status = "✓ Valid" if valid else "✗ Invalid"
        print(f"({number})_{base} in {name}: {status}")
        if valid:
            decimal = any_base_to_decimal(number, base)
            print(f"  Decimal value: {decimal}")
    
    # Example 6: Decimal to various bases
    print("\n--- Example 6: Decimal to Multiple Bases ---")
    decimal = 255
    print(f"Decimal: {decimal}")
    print(f"Binary:      {decimal_to_any_base(decimal, 2):>16} (base 2)")
    print(f"Octal:       {decimal_to_any_base(decimal, 8):>16} (base 8)")
    print(f"Hexadecimal: {decimal_to_any_base(decimal, 16):>16} (base 16)")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Binary (base 2): digits 0-1")
    print("- Octal (base 8): digits 0-7")
    print("- Decimal (base 10): digits 0-9")
    print("- Hexadecimal (base 16): digits 0-9, A-F")
    print("- Formula: N = Σ(digit × base^position)")
    print("=" * 60)

if __name__ == "__main__":
    main()
