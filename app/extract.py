import os
import sqlite3
import requests
import datetime
import pandas as pd
import time

def extract(db_path="data/processed/crypto_data.db"):
    """Extracts all cryptocurrencies from CoinGecko API and saves them in the raw_cryptos table"""
    
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "brl",
        "order": "market_cap_desc",
        "per_page": 200,
        "page": 1,
        "sparkline": False
    }

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    all_data = []
    page = 1

    while True:
        params["page"] = page
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            if not data:
                print(f"✅ Todas as criptos extraídas! Total de páginas: {page-1}")
                break

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for coin in data:
                coin["timestamp"] = timestamp
                coin["page_number"] = page

            all_data.extend(data)
            print(f"✅ Página {page} extraída com {len(data)} criptos!")

            page += 1
            time.sleep(15)  # Evita rate limit da API

        elif response.status_code == 429:
            print("⏳ API bloqueou por excesso de requisições. Aguardando 30s...")
            time.sleep(30)

        else:
            print(f"❌ Erro na API na página {page}: {response.status_code}")
            break

    if all_data:
        save_raw_data(all_data, db_path)

def save_raw_data(data, db_path):
    """Saves extracted data into the raw_cryptos table, ensuring all columns exist dynamically"""
    
    conn = sqlite3.connect(db_path)

    # 🔹 Converte os dados para DataFrame
    df = pd.DataFrame(data)

    # 🔹 Remove a coluna 'roi' se existir
    if "roi" in df.columns:
        df.drop(columns=["roi"], inplace=True)

    # 🔹 Converte colunas com dicionários para string
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, dict)).any():
            print(f"⚠️ A coluna '{col}' contém valores do tipo dict! Convertendo para string...")
            df[col] = df[col].map(lambda x: str(x) if isinstance(x, dict) else x)

    # 🔹 Salva no banco (substitui completamente a tabela)
    df.to_sql("raw_cryptos", conn, if_exists="replace", index=False, chunksize=500)

    conn.close()
    
    print(f"✅ {len(df)} registros salvos em raw_cryptos!")

if __name__ == "__main__":
    extract()