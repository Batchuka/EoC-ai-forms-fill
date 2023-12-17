# formulario.py

def obter_dados_do_formulario():
    print("Preencha o formulário para emitir uma Declaração de Importação:")
    
    # Produto
    descricao_mercadoria = input("Descrição da mercadoria: ")
    pais_origem = input("País de origem: ")
    valor_fob = float(input("Valor FOB (em dólares): "))
    peso_bruto = float(input("Peso bruto (em kg): "))
    
    # Exportador
    nome_exportador = input("Nome do exportador: ")
    codigo_ncm = input("Código NCM (Nomenclatura Comum do Mercosul): ")
    quantidade = float(input("Quantidade: "))
    
    # Importador
    nome_importador = input("Nome do importador: ")
    modo_importacao = input("Modo de importação (marítimo, aéreo, terrestre): ")
    pais_procedencia = input("País de procedência: ")
    unidade_medida = input("Unidade de medida: ")
    
    return {
        'DescricaoMercadoria': descricao_mercadoria,
        'PaisOrigem': pais_origem,
        'ValorFOB': valor_fob,
        'PesoBruto': peso_bruto,
        'NomeExportador': nome_exportador,
        'CodigoNCM': codigo_ncm,
        'Quantidade': quantidade,
        'NomeImportador': nome_importador,
        'ModoImportacao': modo_importacao,
        'PaisProcedencia': pais_procedencia,
        'UnidadeMedida': unidade_medida
    }

if __name__ == "__main__":
    dados_formulario = obter_dados_do_formulario()
    print("Dados do formulário:", dados_formulario)
