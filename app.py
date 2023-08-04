score = 0
paises = {"do Brasil":"Brasilia",
          "da Argentina":"Buenos Aires",
          "da Bolívia":"La Paz",
          "do Chile":"Santiago",
          "da Colômbia":'Bogotá',
          "do Equador":"Quito",
          "da Guiana":"Georgetown",
          "do Paraguai":"Assunção",
          "do Peru":"Lima",
          "do Suriname":"Paramaribo",
          "do uruguai":"Montevidéu",
          "da Venezuela":"Caracas",
          "da Guiana Francesa":"Caiena"}

for pais in paises:
  resposta = input(f"Qual a capital {pais} ")
  if resposta == paises[pais]:
    print("Está correto!")
    score += 1
  else:
    print("Não está correto")

print("Acabou!")
print(f"Sua pontuação final foi {score} de 13!")
