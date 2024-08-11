# Sistema de Autenticação

Sistema de autenticação em Python que permite ao usuário realizar o login com autenticação.

Este projeto em Python fornece um sistema simples de autenticação que utiliza códigos OTP e QR Codes para gerar e verificar códigos de autenticação.


## Instruções de Uso

1. **Instalar um Aplicativo Autenticador**:
   - Baixe e instale um aplicativo autenticador no seu celular, como o Google Authenticator ou Authy.

2. **Executar o Script**:
   - Execute o script Python.

3. **Gerar QR Code**:
   - O script gerará um QR Code e o salvará como `qrcode.png`. Escaneie o QR Code com o aplicativo autenticador no seu celular. Isso adicionará uma conta ao aplicativo para gerar códigos OTP.

4. **Criar Login e Senha**:
   - Siga as instruções no menu do programa para criar um login e uma senha.

5. **Realizar o Login**:
   - Ao tentar fazer login, insira o login e a senha criados. O programa solicitará um código de autenticação. Abra o aplicativo autenticador no seu celular e insira o código OTP exibido para completar o login.



## Dependências

- `pyotp`: Utilizado para gerar e gerenciar códigos OTP.
- `qrcode`: Utilizado para gerar QR Codes.
- `os`: Utilizado para interações com o sistema de arquivos.
- `time`: Utilizado para facilitar as leituras.
- `msvcrt`: Utilizado para capturar a entrada do usuário no Windows.

O código foi projetado para ser executado no Windows, onde usa a biblioteca `msvcrt`. Para executar o código em Mac ou Linux, você precisará substituir `msvcrt` por `getch`.

Instale as dependências necessárias com o comando:

```bash
pip install pyotp qrcode
```