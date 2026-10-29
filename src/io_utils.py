import pandas as pd

def load_sales_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip() 
    
    required_columns = [
        "order_id",
        "date",
        "city",
        "category",
        "price",
        "units",
        "revenue",] 
    
    missing_columns = [column for column in required_columns if column not in df.columns]
    
    if missing_columns:
        raise ValueError(f"Följande kolumner saknas: {missing_columns}")
    
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

def get_data_quality_report(df):
    quality_report = {
        "Antal rader": len(df),
        "Antal kolumner": len(df.columns),
        "Saknade värden": int(df.isna().sum().sum()),
        "Helt duplicerade rader": int(df.duplicated().sum()),
        "Saknade order-id": int(df['order_id'].isna().sum()),
        "Ogiltiga datum": int(df['date'].isna().sum()),
        "Negativa priser": int((df['price'] < 0).sum()),
        "Negativa enheter": int((df['units'] < 0).sum()),
        "Negativ intäkt": int((df['revenue'] < 0).sum()),   
    }
    
    return pd.Series(quality_report, name="Resultat") 
