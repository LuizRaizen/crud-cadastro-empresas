# -*- coding: UTF-8 -*-

import sqlite3


class Database:
    
    def __init__(self, filename="database.db"):
        self.filename = filename
        self.connection = None
    
    def connect(self):
        """ Abrir uma nova conexão com o banco de dados """
        
        self.connection = sqlite3.connect(self.filename)
        
    def close(self):
        """ Fechar a conexão com o banco de dados """
        
        self.connection.close()
        
    def create_table(self):
        """ Criar a tabela de empresas """
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS empresas (
                    cnpj INTEGER PRIMARY KEY UNIQUE NOT NULL,
                    nome_fantasia TEXT,
                    logradouro TEXT,
                    numero TEXT,
                    complemento TEXT,
                    bairro TEXT,
                    municipio TEXT,
                    uf TEXT,
                    cep TEXT,
                    telefone TEXT,
                    email TEXT
                )
            """)
            print("O banco de dados foi criado com sucesso!")
            
        except:
            print("O novo banco de dados não pôde ser criado!")
        
    def register_company(self, dataset):
        """ Cadastra os dados de uma empresa no sistema """
        
        fields = (
            "cnpj",
            "nome_fantasia",
            "logradouro", 
            "numero", 
            "complemento", 
            "bairro",
            "municipio", 
            "uf", 
            "cep", 
            "telefone", 
            "email"
        )
        
        amount = ("?,"*10+"?")
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"INSERT INTO empresas ({','.join(fields)}) VALUES ({amount})""", dataset)
            self.connection.commit()
            
            return "Os dados foram cadastrados com sucesso!"
        
        except:
            return "Os dados não puderam ser cadastrados."
    
    def select_all(self):
        """ Seleciona os dados de todas as empresas cadastradas no sistema """
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM empresas ORDER BY nome_fantasia")
        
        companies = cursor.fetchall()
        
        return companies
        
    def delete_company(self, cnpj):
        """ Remove os dados de uma empresa do sistema """

        cursor = self.connection.cursor()
        cursor.execute(f"REMOVE FROM empresas WHERE cnpj = {cnpj}")
        self.connection.commit()
        
    def update_company(self, dataset):
        """ Atualiza os dados do cadastro de uma empresa na lista de empresas """
        
        cursor = self.connection.cursor()
        cursor.execute(f"""
            UPDATE empresas SET
                cnpj = '{dataset[0]}',
                nome_fantasia = '{dataset[1]}',
                logradouro = '{dataset[2]}',
                numero = '{dataset[3]}',
                complemento = '{dataset[4]}',
                bairro = '{dataset[5]}',
                municipio = '{dataset[6]}',
                uf = '{dataset[7]}',
                cep = '{dataset[8]}',
                telefone = '{dataset[9]}',
                email = '{dataset[10]}',
                
            WHERE cnpj = {dataset[0]}
        """)
    

db = Database()
db.connect()
db.create_table()

db.register_company(
    ("46769130874",
    "Starset Enterprise LTDA",
    "R. Moisés Maimônides",
    "659",
    "",
    "Vila Progresso",
    "São Paulo",
    "SP",
    "08241250",
    "11951447350",
    "luizdererita@gmail.com")
)

companies = db.select_all()
print(companies[0])

db.close()
