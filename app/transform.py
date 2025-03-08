import sqlite3
import pandas as pd
from datetime import datetime

def transform(db_path="data/processed/crypto_data.db"):
    """Transforms and enriches crypto data, storing in enriched_cryptos with historical records."""

    # 🔹 Conectar ao banco
    conn = sqlite3.connect(db_path)

    # 🔹 Carregar os dados da `currated_cryptos`
    df = pd.read_sql("SELECT * FROM currated_cryptos", conn)

    if df.empty:
        print("⚠️ Nenhum dado encontrado em currated_cryptos! Verifique se o load ocorreu corretamente.")
        conn.close()
        return
    
    # 🔹 Adicionar a data de extração
    df["data_extracao"] = datetime.now().strftime("%Y-%m-%d")

    # 🔹 Calcular novas métricas
    df["price_variation_24h"] = df["high_24h_brl"] - df["low_24h_brl"]
    df["final_variation_24h"] = df["high_24h_brl"] - df["current_price_brl"]
    
    # 🔹 Criar ranking baseado no Market Cap
    df["market_cap_rank"] = df["market_cap_brl"].rank(ascending=False, method="min").astype(int)

    # 🔹 Criar um DataFrame filtrado para a enriched
    df_enriched = df[(df["market_cap_brl"] >= 1_000_000) & (df["total_volume_brl"] >= 10_000)]

    # 🔹 Salvar na `enriched_cryptos` mantendo histórico
    df_enriched.to_sql("enriched_cryptos", conn, if_exists="append", index=False)

    conn.close()
    
    print(f"✅ {len(df_enriched)} registros filtrados e salvos em enriched_cryptos!")
    print(f"📊 A `currated_cryptos` ainda mantém {len(df)} registros para análises completas.")

if __name__ == "__main__":
    transform()
