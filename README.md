<h1> Compiladores 2 </h1>
Repositório destinado ao trabalho da disciplina de compiladores ministrada pelo professor Daniel Lucrédio. O trabalho da disciplina consiste em implementar um compilador completo para uma linguagem de sua escolha.

<h2> Descrição do projeto </h2>
Esse trabalho implementará um compilador que traduz uma série de comandos do MongoDB
à uma linguagem SQL.

<h2> Membros do Grupo </h2>
<ol>
  <li> Gabriel Bortolote Pitarelli - 726514 </li>
  <li> Paulo Vitor Tostes Betareli - 587648 </li>
  <li> Sergio Ricardo Hideki Nisikava, RA: 551848 </li>
</ol>

## Como instalar e usar antlr4 em python
- Abra um terminal na pasta antlr4-python3-runtime-4.9.2
- Você pode baixar a pasta pelo link https://pypi.org/project/antlr4-python3-runtime/#files
- Execute os comandos:
```bash
python3 setup.py build
sudo python3 setup.py install
```
- Com o arquivo da gramática (.g4) e o jar do antlr4 em mãos execute o comando:

```bash
java -Xmx500M -cp antlr-4.9.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener grammar/Grammar.g4
```

- Note que os seguintes arquivos foram gerados:
  - GrammarLexer.py
  - GrammarParser.py
  - GrammarListener.py
  - GrammarVisitor.py

## Executar o projeto

Estando os arquivos listados acima gerados, podemos executar o arquivo _main.py_, que possui a implementação do projeto, usando o seguinte comando:

```bash
python3 main.py input.txt
```

com esse comando a saída será impressa no terminal, se você quiser salvar a saída em um arquivo basta usar:

```bash
python3 main.py input.txt output.txt
```

Você também pode executar vários arquivos de uma vez passando o nome de uma pasta para inputs e de uam pasta para outputs, todos os arquivos de dentro da inputs serão executados e seus respectivos resutlados serão salvos com o respectivo nome na pasta outputs, exemplo:

```bash
python3 main.py input.txt output.txt
```
