''''
Operadores aritméticos em python
O que são?
Os operadores aritméticos executam operações matemáticas, como adição, subtração com operandos.
Print (1+1) adição = 2
Print (1-1) subtração = 0
Print (1*1) multiplicação = 1 
Print (12/3) divisão = 4.0
Print (12//2) divisão inteira = 6

Modulo e exponenciação 
Print (10%3) = 1
Print (2**3) = 8
Obs.: O modulo é o resto da divisão.

Precedência dos operadores:
A definição indica a ordem correta
- Parêntesis 
- Expoentes
- Multiplicações e divisões (da esquerda para a direita)
- Somas e subtrações (da esquerda para a direita)

Operadores de comparação:
O que são?
São operadores utilizados para comparar dois valores

Igualdade
Saldo = 450
Saque = 200
Print (saldo == saque)
>>>> False 
Diferença 
Saldo = 450
Saque = 200
Print (saldo != saque)
>>>> True

Maior que / maior ou igual 
Saldo = 450
Saque = 200
Print (saldo > saque)
>>>> True
Print (saldo >= saque)
>>>> True

Menor que / menor ou igual 
Saldo = 450
Saque = 200
Print (saldo < saque)
>>>> False
Print (saldo <= saque)
>>>> False

Operadores de atribuição:
 Atribuição simples
Saldo = 500 
Print (saldo)
>>>>500




Atribuição com adição 
Saldo = 500
Saldo += 200
Print (saldo)
>>>>700

Atribuição com subtração
Saldo = 500
Saldo -= 200
Print (saldo)
>>>>400

Atribuição com multiplicação 
Saldo = 500
Saldo *= 2
Print (saldo)
>>>>1000

Atribuição com divisão 
Saldo = 500
Saldo /= 5
Print (saldo)
>>>>100.0
Saldo = 500
Saldo //= 5
Print (saldo)
>>>>100




Atribuição com modulo 
Saldo = 500
Saldo %= 480
Print (saldo)
>>>>20

Atribuição com exponenciação 
Saldo = 80
Saldo **= 2
Print (saldo)
>>>>6400

Conhecendo os operadores lógicos
O que são?
São operadores utilizados em conjunto com operadores de comparação, para montar uma expressão logica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos.

Saldo = 1000
Saque = 200
Limite = 100 
Saldo >= saque 
>>>> True 
Saque <= limite
>>>> False

Saldo = 1000
Saque = 200
Limite = 100 
Saldo >= saque and saque <= limite 
>>>> False 
Saldo = 1000
Saque = 200
Limite = 100 
Saldo >= saque or saque <= limite 
>>>> True

Operador de negação (o inverso da sentença)
Obs.: sequencias vazias em python é considerado falso

contatos_emergencia = [] (lista vazia em python é considerado falso)
not 1000 > 1500
>>>> True 
not contatos_emergencia
>>>> True 
not “saque 1500;”
>>>> False 
not “”
>>>> True

Parênteses 
Saldo = 1000
Saque = 250
Limite = 200 
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
>>>> True 

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) 
>>>> True 

Conhecendo os operadores de identidade 
O que são 
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memoria

Curso = “Curso de Python”
Nome_curso = curso
Saldo, limite = 200, 200

Curso is nome_curso
>>>> True
Curso is not nome_curso
>>>> False 
Saldo is limite 
>>>> True 

Conhecendo operadores de associação 
O que são
São operadores utilizados para verificar se um objeto está presente em uma sequencia

Curso = ‘’Curso de Python”
Frutas = [“laranja”, “uva”, ”limão”]
Saques = [1500, 100]

“python” in curso
>>>> True
“maçã” not in frutas
>>>> True
200 in saques
>>>> False

'''