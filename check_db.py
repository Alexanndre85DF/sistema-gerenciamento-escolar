import sqlite3

def check_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("\n=== Usuários cadastrados ===")
    cursor.execute("SELECT cpf, tipo_usuario, escola_id FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(f"CPF: {usuario[0]}, Tipo: {usuario[1]}, Escola ID: {usuario[2]}")
    
    print("\n=== Escolas cadastradas ===")
    cursor.execute("SELECT id, nome FROM escolas")
    escolas = cursor.fetchall()
    for escola in escolas:
        print(f"ID: {escola[0]}, Nome: {escola[1]}")
    
    conn.close()

if __name__ == "__main__":
    check_db() 