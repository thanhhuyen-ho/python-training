import math

# 1. 2 * (3 + 4)
q1 = 2 * (3 + 4)
print("1.", q1)

# 2. 2 * 3 + 4
q2 = 2 * 3 + 4
print("2.", q2)

# 3. 2 + 3 * 4
q3 = 2 + 3 * 4
print("3.", q3)

# 4. Square root and square tools
sqrt_9 = math.sqrt(9)
square_5_a = 5 ** 2
square_5_b = pow(5, 2)
sqrt_16_pow = 16 ** 0.5
print("4. sqrt(9) =", sqrt_9, "| 5**2 =", square_5_a, "| pow(5,2) =", square_5_b, "| sqrt via **0.5 =", sqrt_16_pow)

# 5. Type of 1 + 2.0 + 3
q5 = 1 + 2.0 + 3
print("5.", q5, "type:", type(q5))

# 6. Truncate and round floating point
num = 3.56789
truncated1 = int(num)
truncated2 = math.trunc(num)
rounded = round(num, 2)
floored = math.floor(num)
print("6. int:", truncated1, "| trunc:", truncated2, "| round:", rounded, "| floor:", floored)

# 7. Convert int to float
i = 7
converted = float(i)
auto_convert = i + 2.5   # implicit promotion
true_div = i / 2
print("7. float(i):", converted, "| auto:", auto_convert, "| true division:", true_div)

# 8. Display integer in octal, hex, binary
n = 255
print("8. oct:", oct(n), "| hex:", hex(n), "| bin:", bin(n))

# 9. Convert base strings to int
bin_to_int = int("1111", 2)
oct_to_int = int("17", 8)
hex_to_int = int("FF", 16)
print("9. bin->int:", bin_to_int, "| oct->int:", oct_to_int, "| hex->int:", hex_to_int)
