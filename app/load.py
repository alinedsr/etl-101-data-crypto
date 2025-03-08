import sqlite3
import pandas as pd
from datetime import datetime

def load(db_path="data/processed/crypto_data.db"):
    """Loads cleaned crypto data into currated_cryptos, ensuring standardized names and removing duplicates."""

    # 🔹 Conectar ao banco
    conn = sqlite3.connect(db_path)

    # 🔹 Carregar os dados da `raw_cryptos`
    df = pd.read_sql("SELECT * FROM raw_cryptos", conn)

    if df.empty:
        print("⚠️ Nenhum dado encontrado em raw_cryptos! Verifique se a extração ocorreu corretamente.")
        conn.close()
        return
    
    # 🔹 Adicionar a data de extração
    df["data_extracao"] = datetime.now().strftime("%Y-%m-%d")

    # 🔹 Remover colunas irrelevantes
    colunas_para_remover = ["image", "last_updated", "atl", "atl_change_percentage"]
    df.drop(columns=[col for col in colunas_para_remover if col in df.columns], inplace=True, errors="ignore")

    # 🔹 Padronizar nomes das colunas
    df.rename(columns={
        "id": "crypto_id",
        "symbol": "ticker",
        "name": "crypto_name",
        "current_price": "current_price_brl",
        "market_cap": "market_cap_brl",
        "total_volume": "total_volume_brl",
        "high_24h": "high_24h_brl",
        "low_24h": "low_24h_brl",
    }, inplace=True)

    # 🔹 Remover duplicatas, mantendo a mais recente
    df.sort_values(by=["data_extracao"], ascending=False, inplace=True)
    df.drop_duplicates(subset=["crypto_id"], keep="first", inplace=True)

    # 🔹 Corrigir colunas com NaN e infinito
    df["market_cap_brl"] = pd.to_numeric(df["market_cap_brl"], errors="coerce").fillna(0)
    df["total_volume_brl"] = pd.to_numeric(df["total_volume_brl"], errors="coerce").fillna(0)
    df["current_price_brl"] = pd.to_numeric(df["current_price_brl"], errors="coerce").fillna(0)

    # 🔹 Salvar na `currated_cryptos` sem sobrescrever os dados anteriores
    df.to_sql("currated_cryptos", conn, if_exists="append", index=False)

    conn.close()
    
    print(f"✅ {len(df)} registros salvos em currated_cryptos!")

if __name__ == "__main__":
    load()