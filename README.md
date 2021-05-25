# Compiladores 2
Projeto de implementação da disciplina de compiladores 2.

## Descrição do projeto
Esse trabalho implementará um compilador que traduz uma série de comandos do MongoDB
à uma linguagem SQL.

## Como instalar e usar antlr4 em python
- Abra um terminal na pasta antlr4-python3-runtime-4.9.2
- Ou vocẽ pode baixar a mesma pasta do link https://pypi.org/project/antlr4-python3-runtime/#files
- Execute os comandos:

bash```
  python3 setup.py build
  sudo python3 setup.py install
```
- Com o arquivo da gramática (.g4) e o jar do antlr4 em mãos execute o comando:

bash```
java -Xmx500M -cp <path_to_jar> org.antlr.v4.Tool -Dlanguage=Python3 -visitor <path_to_g4>
```
- Note que vários arquivos foram gerados, entre eles o <GrammarName>Lexer.py, o <GrammarName>Parser.py, o <GrammarName>Listener.py e o <GrammarName>Visitor.py
