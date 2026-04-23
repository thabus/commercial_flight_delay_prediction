import pandas as pd
import glob
import os

def consolidar_voos():
    # Define o diretório atual (ajuste se seus CSVs estiverem em outra pasta)
    caminho_pasta = '.' 
    
    # Busca todos os arquivos com extensão .csv na pasta
    arquivos_csv = glob.glob(os.path.join(caminho_pasta, '*.csv'))
    
    if not arquivos_csv:
        print("Nenhum arquivo CSV encontrado. Verifique o caminho.")
        return

    print(f"Encontrados {len(arquivos_csv)} arquivos CSV. Iniciando o processamento...")

    lista_dfs = []

    # Loop para ler e armazenar cada CSV na memória
    for arquivo in arquivos_csv:
        print(f"Lendo: {os.path.basename(arquivo)}")
        # low_memory=False evita avisos de tipos mistos de dados em colunas grandes
        df_temp = pd.read_csv(arquivo, low_memory=False)
        lista_dfs.append(df_temp)

    # Concatena todos os DataFrames da lista em um único DataFrame
    print("\nConcatenando todos os arquivos. Isso pode levar alguns segundos...")
    df_final = pd.concat(lista_dfs, ignore_index=True)

    print(f"Concluído! Total de registros consolidados: {len(df_final)}")
    print(f"Total de colunas: {len(df_final.columns)}")

    # Exporta para Parquet
    arquivo_saida = 'voos_brutos.parquet'
    print(f"\nConvertendo e salvando como {arquivo_saida}...")
    
    # O index=False evita salvar o índice numérico do pandas, economizando espaço
    df_final.to_parquet(arquivo_saida, engine='pyarrow', index=False)

    print("\nProcesso de ETL finalizado com sucesso! Arquivo pronto para o Google Drive.")

if __name__ == "__main__":
    consolidar_voos()