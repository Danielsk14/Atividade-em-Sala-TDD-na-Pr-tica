# Atividade em Sala - Ciclo Vermelho, Verde e Refatorar

Este repositório contém a atividade prática sobre TDD, seguindo a ideia do ciclo:

- Red: criação dos testes;
- Green: implementação da solução para os testes passarem;
- Refactor: melhoria da estrutura do código com aplicação de um padrão de projeto.

A atividade foi feita em Python, sem interface gráfica, conforme solicitado no enunciado.

## Problema desenvolvido

O problema escolhido foi uma calculadora de desconto.

A calculadora recebe o valor original de um produto e aplica uma política de desconto, retornando o valor final.

Foram implementadas três políticas:

- Sem desconto: retorna o valor original;
- Desconto percentual: aplica uma porcentagem de desconto;
- Desconto por cupom: subtrai um valor fixo do preço original;
- O desconto por cupom não permite que o valor final fique negativo.

## Arquivos do projeto

O projeto possui dois arquivos principais:

```text
desconto.py
test_desconto.py



**---------------------------------------------------------------------------**
**desconto.py**

Contém a implementação da calculadora de desconto e das políticas de desconto.

As classes criadas foram:

SemDesconto
DescontoPercentual
DescontoCupom
CalculadoraDesconto

A classe CalculadoraDesconto recebe uma estratégia de desconto e usa essa estratégia para calcular o valor final.


**test_desconto.py**

Contém os testes unitários feitos com unittest.

Os testes verificam:

se o valor original é mantido quando não há desconto;
se o desconto percentual é aplicado corretamente;
se o desconto por cupom é aplicado corretamente;
se o desconto por cupom não deixa o valor final negativo.


**Padrão de projeto utilizado**

Foi utilizado o padrão de projeto Strategy.

Esse padrão foi aplicado porque existem diferentes formas de calcular o desconto, mas todas seguem a mesma ideia: receber um valor e retornar o valor final.

Cada política de desconto ficou separada em uma classe própria. Assim, a calculadora não precisa saber os detalhes de cada desconto, apenas chama o método aplicar.

Isso deixa o código mais organizado e facilita a criação de novas políticas de desconto no futuro.
