# TankGame

Bem-vindo ao **TankGame**, um jogo desenvolvido durante o meu segundo período do curso de Sistemas de Informação!

## Tecnologias Utilizadas:

- **Python**: Linguagem de programação.

## Descrição do Projeto

**TankGame** é um jogo de tanques interativo criado em Python, onde você pode controlar seu tanque e competir com amigos. O projeto é dividido em duas partes principais:

- **Tank.py**: Este arquivo contém a classe `Tank`, que define todos os métodos e atributos necessários para a funcionalidade do tanque.
- **TankGame.py**: Aqui está a lógica do jogo, onde você pode jogar e se divertir!

## Como Executar

Para jogar, siga estas etapas:

1. Baixe os arquivos: `Tank.py` e `TankGame.py`;
2. Abra o projeto no Visual Studio Code (VSCode);
3. Execute o arquivo: `TankGame.py`.

## Personalização

Se você deseja adicionar mais tanques e jogar com amigos, basta editar o dicionário `tanks` no arquivo `TankGame.py` (linha 3). Informe uma letra (key) para representar seu tanque e um nome (value) com a classe. 
Por exemplo: 

tanks {
    'a': Tank('Amigo1'),
    'b': Tank('Amigo2'),
    'c': Tank('Amigo3'),
    # Adicione mais tanques aqui
}
