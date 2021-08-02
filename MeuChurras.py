pessoas = int(input('Quantas pessoas vão participar do seu churras? '))

print("""Sobre bebidas alcólicas:
Digite [ 1 ] se não bebem.
Digite [ 2 ] se bebem pouco.
Digite [ 3 ] se bebem moderadamente.
Digite [ 4 ] se bebem bastante.
Digite [ 5 ] se cada pessoa for trazer sua bebida.""")
bebidas = int(input('Qual das opições se encaixam com o seu grupo? '))

print("""Quais acompanhamentos vc vai querer?
Digite [ 1 ] para Pão de Alho.
Digite [ 2 ] para Linguiça.
Digite [ 3 ] para Coraçãozinho.
Digite [ 4 ] para Coxinha da Asa.
Digite [ 5 ] para Tulipa.
Digite [ 6 ] para Quijo Coalho.
Digite [ 0 ] para churrasco sem acompanhamentos""")
adicionais = int(input('Qual das opições seu churras vai ter? '))

quantidade_de_carne = float(0.500 * pessoas)
pao = float(0.200 * pessoas)
linguica = float(0.200 * pessoas)
coracao = float(0.200 * pessoas)
asa = float(0.200 * pessoas)
tulipa = float(0.200 * pessoas)
coalho = float(0.200 * pessoas)
cerveja = int(3 * pessoas)
refrigerante = int(1 * pessoas)

if adicionais > 0:
    quantidade_de_carne = float(0.300 * pessoas)

if bebidas == 1 and adicionais == 1:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Pão de Alho'.format(pessoas, quantidade_de_carne, pao))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 1:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Pão de Alho'.format(pessoas, quantidade_de_carne, pao))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 1:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Pão de Alho'.format(pessoas, quantidade_de_carne, pao))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 1:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Pão de Alho'.format(pessoas, quantidade_de_carne, pao))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 1:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Pão de Alho'.format(pessoas, quantidade_de_carne, pao))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')

elif bebidas == 1 and adicionais == 2:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Linguiça'.format(pessoas, quantidade_de_carne, linguica))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 2:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Linguiça'.format(pessoas, quantidade_de_carne, linguica))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 2:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Linguiça'.format(pessoas, quantidade_de_carne, linguica))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 2:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Linguiça'.format(pessoas, quantidade_de_carne, linguica))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 2:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Linguiça'.format(pessoas, quantidade_de_carne, linguica))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')
elif bebidas == 1 and adicionais == 3:

    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coraçãozinho'.format(pessoas, quantidade_de_carne, coracao))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 3:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coraçãozinho'.format(pessoas, quantidade_de_carne, coracao))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 3:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coraçãozinho'.format(pessoas, quantidade_de_carne, coracao))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 3:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coraçãozinho'.format(pessoas, quantidade_de_carne, coracao))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 3:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coraçãozinho'.format(pessoas, quantidade_de_carne, coracao))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')
elif bebidas == 1 and adicionais == 4:

    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coxinha da asa'.format(pessoas, quantidade_de_carne, asa))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 4:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coxinha da asa'.format(pessoas, quantidade_de_carne, asa))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 4:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coxinha da asa'.format(pessoas, quantidade_de_carne, asa))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 4:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coxinha da asa'.format(pessoas, quantidade_de_carne, asa))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 4:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Coxinha da asa'.format(pessoas, quantidade_de_carne, asa))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')
elif bebidas == 1 and adicionais == 5:

    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Tulipa'.format(pessoas, quantidade_de_carne, tulipa))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 5:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Tulipa'.format(pessoas, quantidade_de_carne, tulipa))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 5:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Tulipa'.format(pessoas, quantidade_de_carne, tulipa))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 5:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Tulipa'.format(pessoas, quantidade_de_carne, tulipa))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 5:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Tulipa'.format(pessoas, quantidade_de_carne, tulipa))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')
elif bebidas == 1 and adicionais == 6:

    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Queijo Coalho'.format(pessoas, quantidade_de_carne, coalho))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 6:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Queijo Coalho'.format(pessoas, quantidade_de_carne, coalho))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 6:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Queijo Coalho'.format(pessoas, quantidade_de_carne, coalho))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 6:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Queijo Coalho'.format(pessoas, quantidade_de_carne, coalho))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 6:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne, mais {:.3f} Kg de Queijo Coalho'.format(pessoas, quantidade_de_carne, coalho))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')

elif bebidas == 1 and adicionais == 0:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne.'.format(pessoas, quantidade_de_carne))
    print('Já que seu grupo não bebe, vocês irão precisar de {} litros de refrigerante.'.format(refrigerante))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 2 and adicionais == 0:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne.'.format(pessoas, quantidade_de_carne))
    print('Já que seu grupo bebe pouco, vocês irão precisar de pelo menos {} latas de cerveja para todos.'.format(cerveja))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 3 and adicionais == 0:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne.'.format(pessoas, quantidade_de_carne))
    print('Já que seu grupo bebe moderadamente, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 2), (pessoas / 2)))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 4 and adicionais == 0:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne.'.format(pessoas, quantidade_de_carne))
    print('Já que seu grupo bebe bastante, vocês irão precisar de pelo menos {} latas / {} caixas de cerveja para todos.'.format((cerveja * 4), pessoas))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')

elif bebidas == 5  and adicionais == 0:
    print('Seu churras para {} pessoas, vai precisar de {:.3f} Kg de carne.'.format(pessoas, quantidade_de_carne))
    print('Com essas quantidades, todos os seus convidados sairão satisfeitos.')
    print('Você não precisa se preocupar com a bebida, pois cada pessoa trará o que for beber.')

else:
    print('OPIÇÃO INVALIDA, TENTE NOVAMENTE')
    
