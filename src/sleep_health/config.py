from pathlib import Path

# Caminho absoluto para a raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # Sobe dois níveis para alcançar a raiz

# Caminho para os diretórios de dados
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"