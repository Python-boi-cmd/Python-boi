import random
from colorama import Fore, Back, Style

(score) = 0

x = random.randint(0,10)
y = random.randint(0,10)
print(f"What is {x} + {y}")
z = int(input("Answer here: "))
if (z) == (x) + (y):
    print(f"{Fore.BLUE}{Back.LIGHTGREEN_EX}Correct! Your score increased by 1!")
    (score) += 1
    print("")
else:
    print(f"{Fore.LIGHTRED_EX}{Back.LIGHTBLACK_EX}Wrong. the correct answer was {x + y}!")
a = random.randint(0,10)
b = random.randint(0,10)
print(f"{Fore.RESET}{Back.RESET}What is {a} * {b}?")
c = int(input("Answer Here: "))
if (c) == (a) * (b):
    print("")
    print(f"{Fore.BLUE}{Back.LIGHTGREEN_EX}Correct! Your score has updated!")
    score += 1
else:
    print(f"{Fore.LIGHTRED_EX}{Back.LIGHTBLACK_EX}Wrong, the correct  answer was {a * b}. Your score in total was {score}!")
r = random.randint(0,10)
f = random.randint(0,10)
print(f"{Fore.RESET}{Back.RESET}What is {r} * {f}?")
t = int(input("Answer Here: "))
if (t) == (r) * (f):
    (score) += 1
    print(f"{Fore.BLUE}{Back.LIGHTGREEN_EX}Correct! Your score in total was {score}!")
else:
    print(f"{Fore.LIGHTRED_EX}{Back.LIGHTBLACK_EX}Wrong, the correct answer was {r * f}")
    print(f"Your score in total is {score}")

o = random.randint(0,5)
p = random.randint(0,10)
print(f"{Fore.RESET}{Back.RESET}What is {p} - {o}")
i = int(input("Answer Here: "))
if (i) == (p) - (o):
    score += 1
    print(f"{Fore.BLUE}{Back.LIGHTGREEN_EX}Correct, your score is {score}!")
else:
    print(f"{Fore.LIGHTRED_EX}{Back.LIGHTBLACK_EX}Wrong.")
n = random.randint(1,10)
m = random.randint(1,10)
print(f"{Fore.RESET}{Back.RESET}What is {n} / {m}?")
b = input("Answer Here: ")
if (b) == (n) / (m):
    print(f"{Fore.BLUE}{Back.GREEN}Correct!")
else:
    print(f"{Fore.LIGHTRED_EX}{Back.LIGHTBLACK_EX}Wrong, the correct answer was {n / m}! Your score was {score}.")

q = random.randint(0,10)
e = random.randint(0,10)
print(f"{Fore.RESET}{Back.RESET}What is {q} - {e}? (could possibly include negative answers)")
s = int(input("Answer here: "))
if (s) == (q - e):
    score += 1
    print(f"{Fore.LIGHTBLUE_EX}{Back.GREEN}Correct! Your score is {score}")
else:
    print(f"Wrong, the correct answer is {q - e}. Your score is {score}")