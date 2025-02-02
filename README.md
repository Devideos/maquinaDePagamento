# 💼 Máquina de Pagamento

Este é um simples programa em Python que simula uma máquina de pagamento, permitindo que o usuário escolha a forma de pagamento e veja o valor final com descontos ou juros aplicados.

---

## ✨ Funcionalidades

- Exibe um menu interativo para o usuário escolher a forma de pagamento.
- Aplica descontos de acordo com a opção escolhida:
  - 10% de desconto para pagamentos à vista no dinheiro ou PIX.
  - 5% de desconto para pagamentos à vista no cartão.
  - Pagamento parcelado sem juros em 2x ou 3x.
  - Juros de 20% para parcelamentos acima de 4x.
- Garante que o usuário insira valores válidos, exibindo mensagens de erro caso contrário.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- ANSI Escape Codes para formatação no terminal

---

## 📝 Como Usar

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/maquina-de-pagamento.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd maquina-de-pagamento
   ```
3. Execute o script:
   ```sh
   python maquina_pagamento.py
   ```
4. Siga as instruções no terminal para inserir o valor do produto e escolher a forma de pagamento.

---

## 📈 Exemplo de Saída

```
========== Máquina de Pagamento ==========
Digite o valor do produto: 100
Qual será a forma de pagamento:
[ 1 ] À vista no dinheiro.
[ 2 ] À vista no pix.
[ 3 ] À vista no cartão.
[ 4 ] No cartão em 2x sem juros.
[ 5 ] No cartão em 3x sem juros.
[ 6 ] No cartão em 4x ou mais com juros.

DIGITE A FORMA DE PAGAMENTO: 1
Sua compra será à vista.
O valor a pagar é de R$90.00, tendo um desconto de 10%.
```

---

## 🔧 Melhorias Futuras

- Adicionar suporte para diferentes moedas.
- Criar uma interface gráfica para melhor experiência do usuário.
- Implementar um sistema de login para armazenar histórico de compras.

---

## 👨‍💻 Autor

Desenvolvido por **David Pereira**. Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/davidpereira-dev)!

---

## 💌 Contribuição

Sinta-se à vontade para contribuir com melhorias! Faça um **fork** do repositório, crie uma **branch**, e abra um **pull request**.

---


