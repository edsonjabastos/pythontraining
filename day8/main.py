# def greet():
#     print("good morning!")
#     print("good evening!")
#     print("good night!")


# greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Edson")


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What clock is it now in {location}")


# greet_with("Edson", "PL city")

# def greet_with(name, location, time):
#     print(f"Hello {name}")
#     print(f"What clock is it now in {location}")


# greet_with("Edson", "PL city")


def greet_withkw(name="Edson", location="PL city", nick="Edin"):
    print(f"Hello! {name}")
    print(f"Cê ta aí em {location}, né {name}")
    print(f"Cê é de lá mesmo {nick}")

# greet_withkw("seboso","rústico","vegeta")
greet_withkw()