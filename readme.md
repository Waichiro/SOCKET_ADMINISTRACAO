## Projeto socket

Equipe:
- Ariane Santos Gomes - 1272121526
- Gabriel Santos da Silva - 1272121748
- João Pedro Oliveira dos Santos Silva - 1272117418
- Pedro Azevedo de Queiróz - 1272123228

## Dependências

O projeto foi realizado com a linguagem python e utiliza as seguintes lib's:

```python
import socket
import datetime
import random
```

Versão do python utilizado para roda o projeto: Python 3.11.0

Testes realizados no Windows 11 22H2

- Para iniciar o projeto selecione o programa padrão como 'Python' para abrir o arquivo de extensão .py

- Interpretador do python esteja nas variáveis de ambiente.

- Se o ambiente for Windows poderá executar o arquivo executarProjeto.bat que será aberto 3 janelas já rodando os 3 arquivos, servidor, funcionário e gerente.

## Projeto

Separado em três arquivos(servidor, gerente e funcionario), o socket 
assim como o professor pediu, é um gerenciador de vendas, onde o funcionario 
irá fazer a venda e o gerente podera ver as vendas dos funcionarios, a venda 
nas lojas, venda das lojas por periodo, funcionario que mais vendeu e a loja
onde mais foi vendido os produtos.

Para rodar o sistema, primeiro você ira executar:

```python
python servidor.py
```
Logo após, deverá rodar o socket de funcionario:

```python
python funcionario.py
```

No socket de funcionario já poderá fazer, a venda do primeiro produto, onde você deverá,
selecionar a opção 1, onde você irá selecionar o vendedor, logo após a loja.

Logo após, deverá rodar o socket de gerente:

```python
python gerente.py
```

No socket de gerente você consegue realizar todas as funções e filtrar o total de vendas, tanto por vendedor
quanto por loja, total de venda de uma loja em um determinado período e também a melhor loja e vendedor.
