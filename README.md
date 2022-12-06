# S2-teste-tecnico-backend

Olá! Este projeto consiste em ler arquivos de movimentações financeiras (CNAB) de múltiplos estabelicimentos, no formato txt, e gerar um detalhamento que o usuário final consiga fácil acesso aos dados!

## Tecnologias Utilizadas:
Python, Django, Docker.

# Iniciando a aplicação localmente:

1) atraves do terminal crie o ambiente virtual com o comando:  python -m venv venv

2) Acesse o ambiente virtual com o comando : .\venv\Scripts\activate

3) Alter o nome do arquivo .env.exemple para .env e preencha os campos necessários

4) Crie o banco de dados

5) Instale as dependencias do projeto: pip install -r requirements.txt

6) Cria as tabelas com a sequencia dos comandos: 
python manage.py makemigrations 
python manage.py migrate

7) Execute a aplicação na sua máquina: python manage.py runserver

# End points:

local: http://127.0.0.1:8000/api/

## Metodos:
- Post: Envia o arquivo txt
  
Sucesso: 

    {
    "file_uploaded": null
    }
Erro:

    {
        "file_uploaded": [
            "The submitted data was not a file. Check the encoding type on the form."
        ]
    }

- GET: 
  
Lista vazia:

    []

Lista com dados (exemplo):

    [
        {
            "store": "BAR DO JOÃO",
            "currency": -102.0,
            "transactions": [
                {
                    "type": "Financiamento",
                    "value": -142.0
                },
                {
                    "type": "Boleto",
                    "value": -112.0
                },
                {
                    "type": "Débito",
                    "value": 152.0
                }
          ]
      }
    ]
