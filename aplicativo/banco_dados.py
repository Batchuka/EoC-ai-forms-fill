# banco_dados.py
import json
import random
import string
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

def obter_cinco_registros():
    conn = sqlite3.connect('dados_formulario.db')
    cursor = conn.cursor()

    # Realiza uma consulta para obter os cinco primeiros registros
    cursor.execute("SELECT * FROM formulario LIMIT 5")
    registros = cursor.fetchall()

    conn.close()

    return registros

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

def carregar_dados_json(caminho):
    with open(caminho, 'r') as arquivo:
        dados_json = json.load(arquivo)
    return dados_json.get("grupos", [])

def gerar_registros_similares(dados_grupos):
    registros = []

    for grupo in dados_grupos:
        descricao_base = grupo.get("descricao", "")
        exportador = grupo.get("exportador", "")
        importador = grupo.get("importador", "")
        ncm = grupo.get("ncm", "")
        quantidade = grupo.get("quantidade", 0)

        for _ in range(quantidade):
            dados = {
                'DescricaoMercadoria': descricao_base + ' produto',
                'PaisOrigem': 'Brasil',
                'ValorFOB': random.uniform(50, 200),
                'PesoBruto': random.uniform(5, 20),
                'NomeExportador': exportador,
                'CodigoNCM': ncm,
                'Quantidade': random.randint(1, 10),
                'NomeImportador': importador,
                'ModoImportacao': 'maritimo',
                'PaisProcedencia': 'China',
                'UnidadeMedida': random.choice(['kg', 'tonelada'])
            }
            registros.append(dados)

    random.shuffle(registros)
    return registros

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
    criar_tabela()
    
    # Carregar dados do JSON
    dados_grupos = carregar_dados_json('dados_grupos.json')

    # Gerar e salvar os registros no banco de dados
    registros = gerar_registros_similares(dados_grupos)
    for dados in registros:
        salvar_dados_formulario(dados)