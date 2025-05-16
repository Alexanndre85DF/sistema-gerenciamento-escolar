import hashlib
import os
import psycopg2
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Dados do novo usuário
cpf = '01099080150'
senha = '123456'
senha_hash = hashlib.sha256(senha.encode()).hexdigest()
tipo_usuario = 'super_admin'

# Conexão com o banco
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Ajuste o comando se sua tabela tiver mais colunas obrigatórias!
cur.execute("""
    INSERT INTO usuarios (cpf, senha, tipo_usuario)
    VALUES (%s, %s, %s)
    ON CONFLICT (cpf) DO NOTHING
""", (cpf, senha_hash, tipo_usuario))

conn.commit()
cur.close()
conn.close()

print("Usuário super_admin criado com sucesso!")