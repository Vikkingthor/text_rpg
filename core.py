#Importando os outros códigos onde estão os inimigos e o personagem
from personagem import Character, check_name
from inimigos import Enemy, lv1_enemies, random_enemy
import random #random para inimigos aleatórios

#verificação de carácteres ao inserir o nome 
while True:
    name = input("Olá corajoso guerreiro, seja bem vindo a Masmorra eterna.\n Digite seu nome: ")
    if check_name(name):
        break

life = 20
defense = 10
strength = 10
experience= 0
level = 1

char = Character(name, life, defense, strength, experience, level)
#esse bloco até a linha 12 define o char, mas parando para analisar é meio inútil. Sei lá.
chosen_enemy = lv1_enemies()
chosen_enemy = random_enemy(chosen_enemy)
#inimigos aleatórios. Cuidado com o Tombstone.
print(f"\n \nBem vindo(a) a masmorra {char.name}, aqui estão suas estatísticas...\n\n {char}\n\n Boa sorte.")
print(".............................................................................................")
print(f"Player {char.name} encontrou {chosen_enemy.name}...\nPrepare-se para a batalha")
#sistema de batalhas abaixo
def Battle_System(char, chosen_enemy):
    while char.life > 0 and chosen_enemy.life > 0:
        print(f"{char.name}, escolha sua ação!\n [1]Atacar.\n [2]Defender.\n [3]Fugir.") #escolha
        movimento = input("Escolha uma ação: ")
        
        movimento = int(movimento) #convertendo str para int

            #verificaçoes de escolha
        if movimento == 1:
            dano = char.strength - chosen_enemy.defense
            if dano <= 0:
                print(f"Você causou 0 de dano")
            chosen_enemy.life -= dano
            print(f"{char.name} causou {dano} pontos de dano em {chosen_enemy.name}")
            if chosen_enemy.life <= 0:
                break

        elif movimento == 2:
            defense = random.randint(0, 2)
            char.life -= defense
            if defense < 0:
                print("Não pode ser negativo")
            print(f"Você defendeu o ataque de {chosen_enemy.name} e sofreu {defense} pontos de dano")
            if char.life <= 0:
                break

        elif movimento == 3:
            run = 5
            char.life -= run
            if char.life <= 0:
                print("Você morreu com um ataque pelas costas...")
                break
            print(f"Você fugiu da luta e tomou {run} pontos de dano pelas costas")
            print("Você fugiu e agora está debaixo do lenço chorando para a mamãe!!!.")
            return

        else:
            print("Escolha uma das opções apresentadas")
            continue

        print(f"{chosen_enemy.name} se movimenta e ataca!")
        char.life = chosen_enemy.Enemy_attack(char)
        if char.life <= 0:
            print("Você perdeu.")
            break

    if chosen_enemy.life <= 0:
            char.experience += chosen_enemy.experience
            if char.experience == 10:
                char.level += 1
                char.strength += 5
                char.defense += 5    
    

    if char.life <= 0:
        print(f"{char.name} morreu.")
    elif chosen_enemy.life <= 0:
        print(f"Você derrotou {chosen_enemy.name}.")

    if char.life > 0:
        print(f"{char.name} segue andando na masmorra e vira para um canto escuro.\n Você não ouve nada mas sente um frio no seu pescoço.")
    else:
        print(f"{char.name} morreu. Essa não será a última vez que a masmorra cela um destino.")    
        return
    
    return print(f"Você olha para frente e a escuridão te olha de volta. Deseja continuar avançando.\n Mas suas calças estão rasgadas, então terá de ir para casa trocar.\n Essas são suas estatísticas finais {char}")
    

Battle_System(char, chosen_enemy) #esse cara inicia a lutinha