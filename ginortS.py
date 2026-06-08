input_string = input().strip()

lowercase = []
uppercase = []
odd_digits = []
even_digits = []


for char in input_string:
    if char.islower():
        lowercase.append(char)
    elif char.isupper():
        uppercase.append(char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            odd_digits.append(char)
        else:
            even_digits.append(char)

lowercase.sort()
uppercase.sort()
odd_digits.sort()
even_digits.sort()

result = ''.join(lowercase + uppercase + odd_digits + even_digits)

print(result)


