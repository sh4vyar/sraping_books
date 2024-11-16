import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    df['Price'] = df['Price'].apply(lambda x: float(x[1:]))  # Convert price to float
    analysis = {
        'summary': df['Price'].describe(),
        'missing_values': df.isnull().sum(),
    }
    return analysis
