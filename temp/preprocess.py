import pandas as pd

def preprocess_data(file_path):
    """
    CSV se data load karega, 
    basic cleaning aur preprocessing karega,
    aur clean DataFrame return karega.
    """
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)

    # Sirf 'Close' price lenge forecast ke liye
    df = df[['Close']]

    # Missing values check karo aur drop karo agar ho to
    df.dropna(inplace=True)

    print("Preprocessing complete ho gaya.")
    return df

# Test ke liye:
if __name__ == "__main__":
    df = preprocess_data("AAPL_data.csv")
    print(df.head())



print("hello")
print(len(df))
print(df.shape)
