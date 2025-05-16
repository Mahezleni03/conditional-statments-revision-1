char = input("Enter a single letter :").lower()

if char in 'aeiou':
    print(char,"is a vowel")
elif char.isalpha():
    print(char,"is a consana")
else:
    print("INVALID INPUT! Please enter a alphabet")