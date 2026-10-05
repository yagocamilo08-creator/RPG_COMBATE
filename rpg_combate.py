# Arena dos Campeões: Sistema de Batalha RPG
# Desenvolva um sistema de combate por turnos em Python. Neste cenário, você construirá a arquitetura central de um jogo de RPG via console, gerenciando combates entre diferentes classes de personagens e monstros. O foco técnico é estruturar o projeto de forma manutenível utilizando conceitos sólidos de Programação Orientada a Objetos, garantindo que regras lógicas (como pontos de vida não ficarem negativos) sejam estritamente controladas por encapsulamento.

# Objetivo
# Implementar um sistema de batalha de RPG funcional no console, aplicando os conceitos de Herança para diferenciar as classes de personagens e Encapsulamento para a gestão segura e precisa dos status de combate.

# Pré-requisitos Recomendados
# Conhecimentos sólidos em Python, Programação Orientada a Objetos (Classes, Herança, Encapsulamento usando métodos de acesso ou @property), manipulação de loops (while) e interação via Console I/O.
import random as r

# Classe base de todos os lutadores da arena.
# Guarda os status de combate (vida, mana, defesa, esquiva, dano, poção)
# e as ações que qualquer personagem pode fazer: atacar, defender e usar poção.
class Personagem:
    # Cria o personagem com os status iniciais. Ele começa com a vida e a mana cheias,
    # sem estar defendendo e sem estar congelado.
    def __init__(self, nome:str,tempocao: bool = True, vidamax: int = 50, manamax:int = 10, defesa:int = 1, esquiva: int = 5, dano:int = 3  ):
        self.nome = nome
        self.vidamax = vidamax
        self._vida = vidamax
        self.manamax= manamax
        self._mana= manamax
        self.tempocao = tempocao
        self.defesa = defesa
        self.esquiva= esquiva
        self.dano = dano
        self.defendendo = False
        self.congelado = False

    # Encapsulamento da vida: toda mudança na vida passa pelo setter abaixo,
    # que impede a vida de ficar negativa ou de passar da vida máxima.
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self,valor):
        if valor < 0:
            valor = 0
        if valor > self.vidamax:
            valor = self.vidamax
        self._vida = valor

    # Encapsulamento da mana: mesma ideia da vida, a mana fica sempre entre 0 e a mana máxima.
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self,valor):
        if valor < 0:
            valor = 0
        if valor > self.manamax:
            valor = self.manamax
        self._mana = valor

    # Apresentação do personagem. É o texto que aparece quando se faz print(personagem),
    # usado no início da batalha para mostrar os lutadores escolhidos.
    def __str__(self):
        return f'\nOlá, eu sou o {self.__class__.__name__} {self.nome}, tenho {self.vida} de vida e {self.mana} de mana. Tenho tambem {self.dano} de dano e {self.defesa} de defesa e por fim {self.esquiva} de esquiva.'

    # Ação "Defender": o próximo golpe que o personagem receber terá a defesa dobrada.
    def defender(self):
        print(f'{self.nome} escolheu defesa para esse turno, defesa agora está dobrada!')
        self.defendendo = True

    # Ação "Usar poção": cura uma quantidade aleatória de vida. Cada personagem só tem uma poção.
    # A mensagem mostra quanto de vida realmente voltou (sem passar da vida máxima).
    def usarpocao(self):
        if self.tempocao == True:
            print(f'{self.nome} tomou uma poção')
            cura = r.randint(1,self.vidamax)
            vida_antiga = self.vida
            self.vida = self.vida + cura
            diferenca_vida = self.vida - vida_antiga
            print(f'{self.nome} recuperou {diferenca_vida} de vida. {self.nome} está com {self.vida} de vida ')
            self.tempocao = False
        else:
            print(f'{self.nome} não tem mais poção ')

    # Ação "Atacar": ataque básico. O alvo pode desviar de acordo com a esquiva dele,
    # a não ser que esteja congelado. Se não desviar, ele recebe o dano.
    def atacar(self,alvo):
        print(f'\n{self.nome} está atacando!\n')
        numero_aleatorio = r.randint(1,100)
        if numero_aleatorio <= alvo.esquiva and not alvo.congelado:
            print(f'O {alvo.nome} desviou do ataque!')
        else:
            alvo.tomardano(self.dano)

    # Aplica um golpe recebido: desconta a defesa (dobrada se estiver defendendo) e tira a vida.
    # Depois do golpe, a defesa dobrada e o congelamento acabam.
    def tomardano(self,dano):
        if self.defendendo == True:
            defesa_usada = self.defesa * 2
            self.defendendo = False
            print(f'{self.nome} está defendendo. ')
        else:
            defesa_usada =  self.defesa
        dano_liquido = dano - defesa_usada
        if dano_liquido <= 0:
            dano_liquido = 0
        self.vida =self.vida - dano_liquido
        self.congelado = False
        if self.vida <= 0:
            print(f"{self.nome} sofreu um golpe fatal de {dano_liquido} de dano e caiu em batalha!")
        else:
            print(f'\nO {self.nome} tomou {dano_liquido} de dano e ficou com {self.vida} de vida.')


# Guerreiro: classe mais forte fisicamente. Herda tudo do Personagem,
# mas tem mais dano e mais defesa, e um ataque especial próprio.
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, defesa= 3, dano= 5)

    # Especial do Guerreiro: gasta 10 de mana para causar o triplo do dano.
    # Pode ser esquivado, e sem mana suficiente o ataque não acontece.
    def super_ataque(self,alvo):
        print(f'O {self.nome} escolheu o super ataque!')
        if self.mana >= 10:
            self.mana = self.mana - 10
            ataque_supremo =self.dano * 3
            numero_aleatorio = r.randint(1,100)
            if numero_aleatorio <= alvo.esquiva and not alvo.congelado:
                print(f'O {alvo.nome} desviou do ataque!')
            else:
                alvo.tomardano(ataque_supremo)
        else:
            print('Mana insuficiente, ataque não realizado')

# Mago: classe focada em magia. Herda tudo do Personagem, com mais mana,
# recupera mana a cada turno e tem dois feitiços especiais.
class Mago(Personagem):
    def __init__(self,nome):
        super().__init__(nome,manamax= 30,dano = 4)

    # Chamado pelo main no começo de cada turno do Mago: recupera até 3 de mana.
    # Mostra quanto realmente voltou, ou avisa se a mana já estava cheia.
    def recuperar_mana(self):
        mana_recuperada = 3
        if self.mana == self.manamax:
            print('Mana está cheia')
        else:
            mana_antiga = self.mana
            self.mana = self.mana + mana_recuperada
            diferenca_mana = self.mana - mana_antiga
            print(f'{self.nome} recuperou {diferenca_mana} de mana')

    # Feitiço de dano: gasta 10 de mana para causar o triplo do dano do Mago. Pode ser esquivado.
    def bola_de_fogo(self,alvo):
        print(f'O {self.nome} escolheu ataque supremo: bola de fogo!')
        if self.mana >= 10:
            self.mana = self.mana - 10
            ataque_supremo =self.dano * 3
            numero_aleatorio = r.randint(1,100)
            if numero_aleatorio <= alvo.esquiva and not alvo.congelado:
                print(f'O {alvo.nome} desviou do ataque!')
            else:
                alvo.tomardano(ataque_supremo)
        else:
            print('Mana insuficiente, ataque não realizado')

    # Feitiço de controle: gasta 15 de mana e não causa dano, mas congela o alvo.
    # Congelado, o alvo não consegue desviar do próximo ataque que receber.
    def bola_de_gelo(self,alvo):
        print(f'O {self.nome} escolheu ataque supremo: bola de gelo!')
        if self.mana >= 15:
            self.mana = self.mana - 15
            numero_aleatorio = r.randint(1,100)
            if numero_aleatorio <= alvo.esquiva and not alvo.congelado:
                print(f'O {alvo.nome} desviou do ataque!')
            else:
                print(f'{self.nome} escolheu bola de gelo para esse turno, {alvo.nome} ficou sem esquivar por 1 turno!')
                alvo.congelado = True
        else:
            print('Mana insuficiente, ataque não realizado')

# Criação de um jogador antes da batalha. Mostra a vitrine com os status de cada classe
# (lidos direto das classes), pede a classe até ser uma opção válida, pede o nome
# e devolve o personagem pronto para lutar.
def criar_personagem(numero):
    print(f'\n===== JOGADOR {numero} =====\n')

    exemplo = Guerreiro('exemplo')
    print(f' 1- Guerreiro: uma classe resistente, com {exemplo.vida} de vida, {exemplo.dano} de dano, {exemplo.mana} de mana e {exemplo.defesa} de defesa, além de um poderoso Super Ataque.\n')

    exemplo = Mago('exemplo')
    print(f' 2- Mago: uma classe focada em magia, com {exemplo.vida} de vida, {exemplo.dano} de dano mágico, {exemplo.mana} de mana e {exemplo.defesa} de defesa, além de duas poderosas habilidades especiais: Bola de fogo e Bola de gelo.')

    while True:
        escolha = input('\nDigite a classe do seu jogador(selecione apenas o número):')
        if escolha == '1' or escolha == '2':
            break
        else:
            print('\nOpção inválida, tente novamente!')
    nome_personagem = input('\nQual nome seu personagem irá ter: ')
    if escolha == '1':
        return Guerreiro(nome_personagem)
    elif escolha == '2':
        return Mago(nome_personagem)

# Um turno de um jogador. Mostra a situação dele (vida, mana e poção) e o menu de ações,
# com os especiais de acordo com a classe. Executa a ação escolhida e encerra o turno.
# Se a opção for inválida, mostra o menu de novo sem perder a vez.
def escolher_acao(jogador,inimigo):
    while True:
        if jogador.tempocao == True:
            pocao_disponivel = 'Sim'
        else:
            pocao_disponivel = 'Não'
        print(f'\nVez do {jogador.nome} - Vida:{jogador.vida}/{jogador.vidamax} | Mana: {jogador.mana}/{jogador.manamax}| Poção disponível: {pocao_disponivel}\n')
        print(' 1- Atacar')
        print(' 2- Defender')
        print(' 3- Usar poção')
        if isinstance(jogador,Guerreiro):
            print(' 4 - Super Ataque')
        elif isinstance(jogador,Mago):
            if jogador.mana >= 15:
                print(' 4 - Bola de Fogo')
                print(' 5- Bola de Gelo')
            elif jogador.mana >= 10:
                print(' 4 - Bola de Fogo')
        opcao = input('\nO que desejas fazer(somente numeros): ')
        if opcao == '1':
            jogador.atacar(inimigo)
            return
        elif opcao == '2':
            jogador.defender()
            return
        elif opcao == '3':
            jogador.usarpocao()
            return
        elif opcao == '4' and isinstance(jogador,Guerreiro):
            jogador.super_ataque(inimigo)
            return
        elif opcao == '4' and isinstance(jogador,Mago):
            if jogador.mana >= 10:
                jogador.bola_de_fogo(inimigo)
            else:
                print('\nVocê não tem mana, tente novamente!')
        elif opcao == '5' and isinstance(jogador,Mago):
            if jogador.mana >= 15:
                jogador.bola_de_gelo(inimigo)
            else:
                print('\nVocê não tem mana, tente novamente!')
        else:
            print('\nOpção inválida, tente novamente!')

# Partida completa: mostra a abertura, cria os dois jogadores e apresenta os dois.
# Depois alterna os turnos enquanto os dois estiverem vivos (o Mago recupera mana
# no começo da vez dele) e, no fim, anuncia quem venceu.
def main():
    print('===== ⚔️ ARENA DOS CAMPEÕES ⚔️=====')
    print('\nBem-vindo à Arena dos Campeões!')
    print('\nPrepare-se para enfrentar batalhas intensas em um sistema de RPG desenvolvido em Python, onde cada decisão pode ser a diferença entre a vitória e a derrota.')
    print('\nEscolha seu personagem, conheça seus atributos e enfrente diferentes inimigos em combates por turnos. Cada classe possui características próprias, como vida, dano, mana e defesa, além de habilidades especiais que podem mudar o rumo da batalha.')
    print('\nNeste projeto, você encontrará diferentes conceitos de Programação Orientada a Objetos, como classes, herança e encapsulamento, utilizados para organizar o sistema e garantir que as regras do combate sejam respeitadas.')
    print('\nAgora, escolha seu campeão, prepare suas habilidades e entre na arena.')
    print('\nA batalha está prestes a começar. Você está preparado? 🛡️🔥\n')

    jogador_1 = criar_personagem(1)
    jogador_2 = criar_personagem(2)
    print()
    print(jogador_1)
    print()
    print(jogador_2)

    # atacante = quem joga neste turno, defensor = o outro. Os papéis trocam a cada turno.
    atacante = jogador_1
    defensor = jogador_2

    while jogador_1.vida > 0 and jogador_2.vida > 0:
        if isinstance(atacante,Mago):
            atacante.recuperar_mana()
        escolher_acao(atacante,defensor)
        atacante,defensor = defensor,atacante
    if jogador_1.vida > 0:
        vencedor = jogador_1.nome
    else:
        vencedor = jogador_2.nome
    print(f'O vencendor da batalha foi: {vencedor}')


main()
