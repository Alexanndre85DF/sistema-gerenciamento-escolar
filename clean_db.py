import sqlite3

def clean_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Remove todos os usuários exceto o super_admin
    cursor.execute('''
        DELETE FROM usuarios 
        WHERE tipo_usuario != 'super_admin'
    ''')
    
    # Remove todas as escolas
    cursor.execute('DELETE FROM escolas')
    
    # Remove todos os livros
    cursor.execute('DELETE FROM livros')
    
    # Remove todos os empréstimos
    cursor.execute('DELETE FROM emprestimos')
    
    conn.commit()
    print("Banco de dados limpo com sucesso!")
    print("\nAgora você pode:")
    print("1. Fazer login como super_admin (CPF: 73383058115, Senha: 123456)")
    print("2. Cadastrar uma nova escola usando cadastrar_escola.py")
    print("3. O novo usuário será criado como servidor normal da escola")
    
    conn.close()

if __name__ == "__main__":
    clean_db() 