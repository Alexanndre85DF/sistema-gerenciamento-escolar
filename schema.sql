-- Criar tabela de escolas
CREATE TABLE IF NOT EXISTS escolas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    cpf VARCHAR(11) PRIMARY KEY,
    senha VARCHAR(64) NOT NULL,
    escola_id INTEGER REFERENCES escolas(id),
    tipo_usuario VARCHAR(20) DEFAULT 'usuario',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de livros
CREATE TABLE IF NOT EXISTS livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    editora VARCHAR(255),
    ano VARCHAR(4),
    categoria VARCHAR(100),
    quantidade INTEGER DEFAULT 1,
    localizacao VARCHAR(100),
    codigo_interno VARCHAR(50),
    observacoes TEXT,
    disponivel BOOLEAN DEFAULT true,
    escola_id INTEGER REFERENCES escolas(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de empréstimos
CREATE TABLE IF NOT EXISTS emprestimos (
    id SERIAL PRIMARY KEY,
    aluno VARCHAR(255) NOT NULL,
    turma VARCHAR(50),
    telefone VARCHAR(20),
    livro_id INTEGER REFERENCES livros(id),
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    data_devolvido DATE,
    escola_id INTEGER REFERENCES escolas(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 