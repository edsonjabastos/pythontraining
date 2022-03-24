print(
    '''
                                    o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                  o
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
'''
)
print("Bem vindo ao Game of Crown!")
print("Sua missão aqui é embarcar em uma aventura para conquistar a coroa e governar os Sete Reinos!")

choice1 = input('Você precisa viajar do norte para King\'s Landing. Qual caminho você vai escolher pelo "mar" ou pela "estrada"?')
if choice1 == "mar":
    choice2 = input('Ao chegar nas docas, o capitão te cobra um valor desonesto para te levar para King\'s Landing. Você "mata" o capitão ou "paga" o preço?')
    if choice2 == "mata":
        choice3 = input('Quando você chega em King\'s Landing, você vai ao "castelo" matar o rei ou faz "estrategia" para conseguir aliados políticos para conseguir a coroa?')
        if choice3 == "estrategia":
            print("Após 1 ano você consegue seus objetivos e conquista o reino! Parabéns você ganhou!")
        else:
            print("Você morre nos portões quando os guardas veem sua espada. Game Over!")
    else:
        print('Você embarca no navio mas quando em mar aberto o capitão de te mata para roubar o ouro que você tem guardado. Game Over!')
else:
    print('No segundo dia de viagem você é morto por bandidos na estrada. Game over!')