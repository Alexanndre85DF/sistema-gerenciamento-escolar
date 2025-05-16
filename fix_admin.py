import sqlite3

def fix_admin():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Remove o usuário 73383058115 que está como super_admin
    cursor.execute('''
        DELETE FROM usuarios 
        WHERE cpf = '73383058115' AND tipo_usuario = 'super_admin'
    ''')
    
    # Verifica se o 10199080150 já é super_admin, se não for, cria
    cursor.execute('''
        INSERT OR REPLACE INTO usuarios (cpf, senha, tipo_usuario)
        VALUES (?, ?, 'super_admin')
    ''', ('10199080150', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'))  # senha: 123456
    
    conn.commit()
    print("Administradores corrigidos com sucesso!")
    
    # Mostra o estado atual dos usuários
    print("\nEstado atual dos usuários:")
    cursor.execute("SELECT cpf, tipo_usuario, escola_id FROM usuarios")
    for usuario in cursor.fetchall():
        print(f"CPF: {usuario[0]}, Tipo: {usuario[1]}, Escola ID: {usuario[2]}")
    
    conn.close()

if __name__ == "__main__":
    fix_admin() 