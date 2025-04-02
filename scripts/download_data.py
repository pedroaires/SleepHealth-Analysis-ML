import os
from kaggle.api.kaggle_api_extended import KaggleApi
from sleep_health.config import RAW_DATA_DIR  # Importando o caminho dos dados
import logging
def download_data():
    """
    Baixa o dataset 'equilibriumm/sleep-efficiency' do Kaggle
    e salva no diretório 'data/raw' na raiz do projeto.
    """
    dataset_id = "equilibriumm/sleep-efficiency"

    os.makedirs(RAW_DATA_DIR, exist_ok=True)  # Garante que o diretório existe
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset_id, path=str(RAW_DATA_DIR), unzip=True)

    logging.info(f"✅ Download concluído! Arquivos salvos em: {RAW_DATA_DIR}")

# Permite rodar o script diretamente pelo terminal
if __name__ == "__main__":
    download_data()
