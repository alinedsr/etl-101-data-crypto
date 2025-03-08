# 🚀 ETL-101: Data Crypto 🪙📊

This project is an **ELT (Extract, Load, Transform) pipeline** for collecting, cleaning, and enriching cryptocurrency data using the **CoinGecko API**. The goal is to extract all available cryptocurrencies, process the data, and store it for further analysis.

---

## 📌 **ELT Workflow**

🔥 This pipeline follows the **ELT (Extract, Load, Transform) approach**:

1️⃣ **Extract (`extract.py`)** → Fetches raw data from the CoinGecko API and stores it in the `raw_cryptos` table.  
2️⃣ **Load (`load.py`)** → Cleans and structures the raw data, removing unnecessary columns, renaming fields, and saving it in the `currated_cryptos` table.  
3️⃣ **Transform (`transform.py`)** → Enriches the data with additional insights, such as market trends and price volatility, and stores only **relevant assets** in the `enriched_cryptos` table.  

⚡ **All steps can be run individually or orchestrated using `main.py`**.  

---

## ⚙ **Setup & Execution**

### **1️⃣ Install Dependencies**
Ensure you have Python installed and are using **Pyenv** for managing versions.

```bash
pyenv install 3.12.1  # Install the required Python version
pyenv virtualenv 3.12.1 etl-101-data-crypto
pyenv activate etl-101-data-crypto
pip install -r requirements.txt
```

---

### **2️⃣ Run the Full Pipeline**
You can **run all steps automatically** with:

```bash
python main.py
```

Or execute them **individually**:

```bash
python app/extract.py  # Extracts raw data
python app/load.py     # Cleans and structures the data
python app/transform.py  # Enriches and filters the dataset
```

---

## 📊 **Database Structure (SQLite)**
All processed data is stored in **`data/processed/crypto_data.db`** (SQLite database).

### **Tables:**
- **`raw_cryptos`** → Raw API data (overwritten daily).  
- **`currated_cryptos`** → Cleaned and structured dataset (historical).  
- **`enriched_cryptos`** → Filtered dataset with enriched insights (historical).  

---

## 🔍 **Querying Data in SQLite**
To explore the data, you can use SQLite commands.

### 🔹 **Check how many cryptocurrencies were extracted**
```sql
SELECT COUNT(*) FROM raw_cryptos;
```

### 🔹 **View the cleaned data in `currated_cryptos`**
```sql
SELECT * FROM currated_cryptos LIMIT 10;
```

### 🔹 **View the enriched data in `enriched_cryptos`**
```sql
SELECT * FROM enriched_cryptos LIMIT 10;
```

---

## 🚀 **Potential Improvements**
🔹 **Automate daily data updates (GitHub Actions, Airflow, or Cloud Functions)**  
🔹 **Develop a Streamlit dashboard to visualize market trends**  
🔹 **Implement price volatility alerts**  
🔹 **Experiment with machine learning for price prediction**  

---

## 🛠 **Tech Stack**
- 🐍 **Python** 3.12.1  
- 📡 **CoinGecko API** for cryptocurrency data extraction  
- 🗄 **SQLite** for storing historical market data  
- ⚡ **Pandas** for data manipulation  
- 🔧 **Pyenv** for Python version management  

---

💡 **Contributions are welcome!**  
Feel free to open a PR or reach out if you have ideas for improvements. 🚀  
