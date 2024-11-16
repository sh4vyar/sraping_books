import pandas as pd

def save_to_csv(books_data):
    df = pd.DataFrame(books_data)
    df.to_csv('books.csv', index=False)
