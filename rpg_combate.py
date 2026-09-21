# Arena dos Campeões: Sistema de Batalha RPG
# Desenvolva um sistema de combate por turnos em Python. Neste cenário, você construirá a arquitetura central de um jogo de RPG via console, gerenciando combates entre diferentes classes de personagens e monstros. O foco técnico é estruturar o projeto de forma manutenível utilizando conceitos sólidos de Programação Orientada a Objetos, garantindo que regras lógicas (como pontos de vida não ficarem negativos) sejam estritamente controladas por encapsulamento.

# Objetivo
# Implementar um sistema de batalha de RPG funcional no console, aplicando os conceitos de Herança para diferenciar as classes de personagens e Encapsulamento para a gestão segura e precisa dos status de combate.

# Pré-requisitos Recomendados
# Conhecimentos sólidos em Python, Programação Orientada a Objetos (Classes, Herança, Encapsulamento usando métodos de acesso ou @property), manipulação de loops (while) e interação via Console I/O.
import random as r 
import math as m 

class personagem:
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

    @property

    def vida(self):
        return self._vida

    @vida.setter

    def vida(self,valor):
        if valor > self.vidamax:
            self._vida = self.vidamax
        elif valor < 0:
            self._vida = 0
        else:
            self._vida = valor

    @property

    def mana(self):
        return self._mana
    @mana.setter

    def mana(self,valor):
        if valor > self.manamax:
            self._mana = self.manamax
        elif valor < 0:
            self._mana = 0
        else:
            self._mana = valor

    def __str__(self):
        return f'Olá, eu sou o {self.__class__.__name__} {self.nome}, tenho {self.vida} de vida e {self.mana} de mana. Tenho tambem {self.dano} de dano e {self.defesa} de defesa e por fim {self.esquiva} de esquiva.'

    def defender(self):
        if self.defendendo == True:
            self.defendendo = self.defesa *2
        else:
            self.defendendo = self.defesa

p1=personagem('Yago')
print(p1)
p1.vida(60) 
print(p1)