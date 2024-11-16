from utility.scrape_books import scrape_books
from analyze.analyze_data import analyze_data
from visualize.visualize_data import visualize_data

def main():
    scrape_books()
    
    analysis = analyze_data('books.csv')
    print("Analysis Summary:")
    print(analysis['summary'])
    print("Missing Values:")
    print(analysis['missing_values'])

if __name__ == "__main__":
    main()
