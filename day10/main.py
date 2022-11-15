# Functions with outputs


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    return f"Result: {f_name.title()} {l_name.title()}"


nome_certinho = format_name("eDsoN", "bAsToS")

print(nome_certinho)
