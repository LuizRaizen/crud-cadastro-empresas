# CRUD de Cadastro de Empresas

Este projeto é um sistema simples de **cadastro e consulta de empresas**, desenvolvido com **Python** e **PySide6**. Ele utiliza a **API pública da Receita Federal** para consultar dados de empresas a partir de seu CNPJ.

> ⚠️ Este projeto **não é autoral**, foi desenvolvido como estudo prático com base nas aulas do canal [Pytax no YouTube](https://www.youtube.com/@pytax). Todo o crédito da estrutura original vai para o criador do conteúdo.

## 📚 Objetivo

Explorar os conceitos de:

- Interfaces gráficas com **PySide6 (Qt for Python)**
- Requisições HTTP para APIs
- Organização de código com **padrão MVC**
- Manipulação de banco de dados com **SQLite**
- Aplicações reais com Python

## 🚀 Funcionalidades

- Cadastro manual de empresas (nome fantasia, CNPJ, razão social)
- Consulta automática de CNPJ via API
- Armazenamento local dos dados em banco de dados SQLite
- Interface visual moderna e responsiva
- Pesquisa e edição de cadastros

## 💻 Tecnologias Utilizadas

- **Linguagem principal:** Python
- **Framework de UI:** PySide6 (Qt for Python)
- **Banco de dados:** SQLite
- **Bibliotecas adicionais:** `requests`, `sqlite3`

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/crud-empresas.git
   cd crud-empresas
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:
   ```bash
   python main.py
   ```

## 📌 Créditos

Este projeto segue as instruções do canal **Pytax no YouTube**. Se quiser aprender como criar este projeto do zero, visite:
[https://www.youtube.com/@pytax]([https://www.youtube.com/@py4allbr])

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**, mas o conteúdo foi inspirado e estruturado com base nas aulas públicas do canal Pytax.
