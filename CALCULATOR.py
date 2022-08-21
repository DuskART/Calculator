power = 1

def plus(a, b):
    c = a + b
    return c

def minus(a, b):
    c = a - b
    return c

def krat(a, b):
    c = a * b
    return c

def deleno(a, b):
    c = a / b
    return c

def mocnina(a, b):
    c = a ** b
    return c

while power == 1:
    print("dobrý den, toto je proper kalkulačka")
    a = int(input("zvolte první číslo: "))
    navazat = "a"
    while navazat == "a":
        funkce = input("co chcete dělat? + - / * **(mocnit): ")
        b = int(input("zvolte druhé číslo: "))

        if funkce == "+":
            vysledek = plus(a, b)
        elif funkce == "-":
            vysledek = minus(a, b)
        elif funkce == "/":
            vysledek = deleno(a, b)
        elif funkce == "*":
            vysledek = krat(a, b)
        elif funkce == "**":
            vysledek = mocnina(a, b)

        print(f"Vas vysledek je {vysledek}")
        navazat = input("navazat a/n: ")
        a = vysledek

