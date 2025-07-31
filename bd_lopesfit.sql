CREATE DATABASE IF NOT EXISTS lopesfit_db;
USE lopesfit_db;



CREATE TABLE tb_usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
    data_cadastro DATE
);

-- Tabela de exercícios cadastrados
CREATE TABLE tb_exercicio (
    id_exercicio INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100)
);


CREATE TABLE tb_categoria (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(100)
);

CREATE TABLE tb_lista_exercicio (
    id_lista_exercicio INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_categoria INT,
    nome_lista VARCHAR(100), -- opcional: para dar nome à ficha
    data_criacao DATE,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuario(id_usuario),
    FOREIGN KEY (id_categoria) REFERENCES tb_categoria(id_categoria)
);

CREATE TABLE tb_lista_exercicio_item (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_lista_exercicio INT,
    id_exercicio INT,
    ordem INT, -- opcional: ordem do exercício na lista
    FOREIGN KEY (id_lista_exercicio) REFERENCES tb_lista_exercicio(id_lista_exercicio),
    FOREIGN KEY (id_exercicio) REFERENCES tb_exercicio(id_exercicio)
);


-- Tabela que registra os dados de cada série feita em um exercício
CREATE TABLE tb_dados_exercicio (
    id_dados_exercicio INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_exercicio INT,  -- chave estrangeira que liga ao exercício
    data_execucao DATE,  -- data em que foi feito o exercício
    serie INT,
    repeticao INT,
    carga DECIMAL(5,2),
    FOREIGN KEY (id_usuario) REFERENCES tb_usuario(id_usuario),
    FOREIGN KEY (id_exercicio) REFERENCES tb_exercicio(id_exercicio)
);

INSERT INTO tb_exercicio (nome, categoria)
VALUES ('Supino Reto', 'Peito');

INSERT INTO tb_dados_exercicio (id_exercicio, data_execucao, serie, repeticao, carga)
VALUES (1, '2025-07-31', 1, 10, 40.00),
       (1, '2025-07-31', 2, 8, 45.00),
       (1, '2025-07-31', 3, 6, 50.00);
       
       INSERT INTO tb_dados_exercicio (id_exercicio, data_execucao, serie, repeticao, carga)
VALUES (1, '2025-08-02', 1, 10, 42.00),
       (1, '2025-08-02', 2, 8, 47.00);