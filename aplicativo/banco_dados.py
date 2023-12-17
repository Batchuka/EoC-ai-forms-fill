# banco_dados.py
import sqlite3

def criar_tabela():
    conn = sqlite3.connect('dados_formulario.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS formulario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao_mercadoria TEXT,
            pais_origem TEXT,
            valor_fob REAL,
            peso_bruto REAL,
            nome_exportador TEXT,
            codigo_ncm TEXT,
            quantidade REAL,
            nome_importador TEXT,
            modo_importacao TEXT,
            pais_procedencia TEXT,
            unidade_medida TEXT
        )
    ''')
    conn.commit()
    conn.close()

def verificar_tabela():
    conn = sqlite3.connect('dados_formulario.db')
    cursor = conn.cursor()

    # Realiza uma consulta para verificar se a tabela existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='formulario'")
    tabela_existe = cursor.fetchone() is not None

    conn.close()
    
    return tabela_existe

def salvar_dados_formulario(dados):
    conn = sqlite3.connect('dados_formulario.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO formulario (
            descricao_mercadoria, pais_origem, valor_fob, peso_bruto,
            nome_exportador, codigo_ncm, quantidade,
            nome_importador, modo_importacao, pais_procedencia, unidade_medida
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        dados['DescricaoMercadoria'],
        dados['PaisOrigem'],
        dados['ValorFOB'],
        dados['PesoBruto'],
        dados['NomeExportador'],
        dados['CodigoNCM'],
        dados['Quantidade'],
        dados['NomeImportador'],
        dados['ModoImportacao'],
        dados['PaisProcedencia'],
        dados['UnidadeMedida']
    ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print(verificar_tabela())
