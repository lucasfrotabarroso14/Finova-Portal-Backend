# Nome do Projeto: Finova Portal Backend

![Logo do Finova](https://i.imgur.com/RELNipx.png)

## Descrição
O Finova Portal Backend é uma API RESTful que oferece serviços para criar, ler, atualizar e excluir ativos, portfólios de investimentos e usuários. Esta API serve como o backend para o [Finova Portal Frontend](https://github.com/lucasfrotabarroso14/Finova-Portal-Front), que é a interface do usuário para o sistema.

## Tecnologias Utilizadas
- Linguagem de Programação: Python
- Framework Web: Flask
- Banco de Dados: MySQL
- Autenticação: JWT (JSON Web Tokens)
- CORS: Habilitado para todas as origens
- Serviço de Email: SMTP com Gmail para enviar e-mails de confirmação de registro
- Criptografia de Senha: Utiliza pbkdf2_sha256 para hash de senhas
- Geração de Chave Secreta: Utiliza a biblioteca secrets para gerar chaves secretas
- Integração Financeira: Utiliza a biblioteca yfinance para obter informações em tempo real de ativos financeiros

# Nome do Projeto: Finova Portal Backend

![Logo do Finova](https://i.imgur.com/RELNipx.png)

## Descrição
O Finova Portal Backend é uma API RESTful que oferece serviços para criar, ler, atualizar e excluir ativos, portfólios de investimentos e usuários. Esta API serve como o backend para o [Finova Portal Frontend](https://github.com/lucasfrotabarroso14/Finova-Portal-Front), que é a interface do usuário para o sistema.

## Tecnologias Utilizadas
- Linguagem de Programação: Python
- Framework Web: Flask
- Banco de Dados: MySQL
- Autenticação: JWT (JSON Web Tokens)
- CORS: Habilitado para todas as origens
- Serviço de Email: SMTP com Gmail para enviar e-mails de confirmação de registro
- Criptografia de Senha: Utiliza pbkdf2_sha256 para hash de senhas
- Geração de Chave Secreta: Utiliza a biblioteca secrets para gerar chaves secretas
- Integração Financeira: Utiliza a biblioteca yfinance para obter informações em tempo real de ativos financeiros

## Funcionalidades Principais
- Registro e gerenciamento de ativos
- Registro e gerenciamento de portfólios de investimentos
- Registro e gerenciamento de usuários
- Confirmação de registro do usuário via e-mail utilizando a biblioteca smtplib

## Princípios de Orientação a Objetos e Programação Funcional na Aplicação

**Orientação a Objetos:**

- **Classes e Objetos:** Implementei classes para representar entidades, como usuários, ativos e portfólios, encapsulando dados e métodos relacionados em objetos.

- **Métodos de Classe:** Desenvolvi métodos nas classes para representar comportamento, como adicionar um novo ativo à carteira do usuário.

**Programação Funcional:**

- **Funções Puras:** Os métodos de classe são funções puras, retornando valores com base em argumentos e sem efeitos colaterais.

- **Imutabilidade:** Respeitei a imutabilidade, retornando novos valores em vez de modificar o estado dos objetos.

- **Reuso de Funções:** Reutilizei funções em vários contextos para evitar duplicação de código.

Essa abordagem me permitiu criar um backend eficiente, escalável e de fácil manutenção para suportar o aplicativo Finova.

## Arquitetura do Projeto
Abaixo está o diagrama de arquitetura do Finova Portal Backend, mostrando a estrutura geral e a interação entre os componentes do sistema.

![Arquitetura do Finova Portal Backend](https://i.imgur.com/oaEewLu.png)

## Documentação da API
![swagger](https://i.imgur.com/GyUE9yZ.png)

## Link para o Frontend
O frontend associado a esta API pode ser encontrado em [Finova Portal Frontend](https://github.com/lucasfrotabarroso14/Finova-Portal-Front). Certifique-se de verificar também o frontend para uma experiência completa do sistema.

## Status do Projeto
Este projeto ainda está em desenvolvimento e passando por melhorias contínuas. Sinta-se à vontade para contribuir ou relatar problemas no repositório.
