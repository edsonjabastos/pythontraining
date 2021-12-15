print(8 / 3)
print(int(8 / 3)) # quando convertemos um float para int o python apenas dele ta depois das casa decimais
print(round(8 / 3))
print(round(8 / 3, 3))
print(round(7.7777, 3)) # round arredonda e seta casas decimais
print(8 // 3)
print(type(8 // 3))
print(4 / 2) #toda divisão converte para float
print(type(4 / 2))

result = 4 / 2
print(result)
result /= 2
print(result)

score = 0
score += 1 # *, /, +, -
print(score)
# print("your score is " + score)
print("your score is " + str(score))
#f-String
height = 1.8
isCool = True
msg = 'brother'
print(f"your score is {score}, height > {height}, isCool? > {isCool}, message > {msg}")