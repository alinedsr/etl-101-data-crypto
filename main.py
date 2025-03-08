from app.extract import extract
from app.load import load
from app.transform import transform

def main():
    print("🚀 Iniciando Pipeline ELT de Criptomoedas...")
    
    extract()
    load()
    transform()

    print("✅ ELT finalizado!")

if __name__ == "__main__":
    main()
