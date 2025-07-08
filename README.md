# Conversor de Moedas

Este projeto consiste em uma aplicação desktop em Python que realiza a conversão de valores entre diferentes moedas utilizando uma API pública e uma lista de códigos de moeda armazenada em XML.

## Funcionalidades

- Interface gráfica interativa usando a biblioteca **CustomTkinter**.
- Leitura de lista de códigos de moeda a partir de um arquivo XML (`moedas.xml`).
- Consulta à cotação em tempo real via API pública `economia.awesomeapi.com.br`.

## Dependências
- XMLToDict
  `
  pip install xmltodict
  `
- Customtkinter
  `
  pip install customtkinter
  `

## Uso
Na interface do aplicativo:
   - Insira o código da moeda de origem (ex: `USD`)
   - Insira o código da moeda de destino (ex: `BRL`)
   - Digite o valor a ser convertido
   - Clique em **Converter** para ver o resultado


![main_I1lvp8CuGo](https://github.com/user-attachments/assets/e0ac631c-f846-4218-be16-b428a3925ec6)
