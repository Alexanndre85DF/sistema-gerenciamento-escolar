import sqlite3

def update_user_type():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Atualiza o tipo de usuário para 'normal' para a escola Os Royais
    cursor.execute('''
        UPDATE usuarios 
        SET tipo_usuario = 'normal' 
        WHERE escola_id = (
            SELECT id 
            FROM escolas 
            WHERE nome = 'Os Royais'
        )
    ''')
    
    conn.commit()
    print("Usuário atualizado com sucesso!")
    
    # Verifica a atualização
    cursor.execute('''
        SELECT u.cpf, u.tipo_usuario, e.nome 
        FROM usuarios u 
        JOIN escolas e ON u.escola_id = e.id 
        WHERE e.nome = 'Os Royais'
    ''')
    usuario = cursor.fetchone()
    if usuario:
        print(f"\nDados atualizados:")
        print(f"CPF: {usuario[0]}")
        print(f"Tipo: {usuario[1]}")
        print(f"Escola: {usuario[2]}")
    
    conn.close()

if __name__ == "__main__":
    update_user_type() 