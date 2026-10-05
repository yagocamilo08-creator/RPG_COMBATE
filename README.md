# ⚔️ Arena dos Campeões

Sistema de batalha de RPG por turnos, jogado no console, feito em Python.

Dois jogadores escolhem um campeão (Guerreiro ou Mago) e duelam na arena, revezando os turnos até que um deles caia em batalha.

O projeto foi construído para praticar **Programação Orientada a Objetos**: **herança**, para diferenciar as classes de personagens, e **encapsulamento**, para manter os status de combate sempre válidos (por exemplo, a vida nunca fica negativa).

## Como jogar

Requisito: [Python 3](https://www.python.org/downloads/) instalado.

```bash
python rpg_combate.py
```

1. Cada jogador vê as classes disponíveis, escolhe uma e dá um nome ao seu personagem.
2. Os dois campeões são apresentados.
3. Os jogadores se revezam escolhendo uma ação por turno.
4. A batalha termina quando a vida de um deles chega a 0, e o vencedor é anunciado.

## Classes

| Classe | Vida | Mana | Dano | Defesa | Esquiva | Estilo |
|---|---|---|---|---|---|---|
| 🛡️ **Guerreiro** | 50 | 10 | 5 | 3 | 5% | Mais forte fisicamente |
| 🔮 **Mago** | 50 | 30 | 4 | 1 | 5% | Mais poderes, recupera mana |

## Ações

Todos os personagens podem:

| Ação | Efeito |
|---|---|
| **Atacar** | Causa o próprio dano no inimigo, que pode desviar de acordo com a esquiva dele |
| **Defender** | Dobra a defesa contra o próximo golpe recebido |
| **Usar poção** | Recupera uma quantidade aleatória de vida. Cada personagem tem **uma** poção |

Habilidades especiais:

| Classe | Habilidade | Custo | Efeito |
|---|---|---|---|
| Guerreiro | **Super Ataque** | 10 de mana | Causa o triplo do dano |
| Mago | **Bola de Fogo** | 10 de mana | Causa o triplo do dano |
| Mago | **Bola de Gelo** | 15 de mana | Não causa dano, mas **congela** o alvo: ele não consegue desviar do próximo ataque |
| Mago | **Recuperar mana** | — | Automático: recupera 3 de mana no começo de cada turno do Mago |

## Regras de combate

- **Dano recebido** = dano do ataque − defesa do alvo (nunca menor que 0).
- **Defendendo**, a defesa do alvo vale o dobro contra o próximo golpe.
- **Esquiva**: a cada ataque, o alvo tem uma chance (em %) de desviar, a não ser que esteja congelado.
- **Vida e mana** ficam sempre entre 0 e o valor máximo do personagem.

## Conceitos de POO aplicados

- **Classes e objetos**: `Personagem`, `Guerreiro` e `Mago`, e cada jogador é um objeto criado a partir delas.
- **Herança**: `Guerreiro` e `Mago` herdam de `Personagem` e usam `super().__init__()` para mudar só os atributos diferentes, além de ganhar habilidades próprias.
- **Encapsulamento**: `vida` e `mana` usam `@property` com *setter*, que impede valores negativos ou acima do máximo.
- **Polimorfismo com `isinstance`**: o menu de cada turno mostra as habilidades de acordo com a classe do jogador.

## Estrutura do código

Tudo está em [`rpg_combate.py`](rpg_combate.py):

| Parte | Responsabilidade |
|---|---|
| `Personagem` | Status de combate e ações comuns: atacar, defender, usar poção e receber dano |
| `Guerreiro` | Atributos do Guerreiro e o Super Ataque |
| `Mago` | Atributos do Mago, recuperação de mana, Bola de Fogo e Bola de Gelo |
| `criar_personagem()` | Mostra as classes, valida a escolha e cria o personagem |
| `escolher_acao()` | Um turno: mostra o menu e executa a ação escolhida |
| `main()` | A partida: cria os jogadores, alterna os turnos e anuncia o vencedor |

## Próximos passos

- [ ] Ação que falha (sem mana ou sem poção) não gastar o turno
- [ ] A defesa dobrada não continuar ligada por vários turnos
- [ ] Adicionar monstros
