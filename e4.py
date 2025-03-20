print("Ingrese un texto o un numero:")
str = input().replace(" ", "").lower()
rts = str[::-1].replace(" ", "").lower()

if str == rts:
    print("Palindromo")
else:
    print("No Palindromo")
