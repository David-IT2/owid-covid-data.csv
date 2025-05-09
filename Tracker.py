import pandas as pd
import seaborn as sns

# Tracker.py

# Import necessary libraries
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    """
    Load the COVID-19 dataset from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Explore the dataset
def explore_data(df):
    """
    Perform basic exploration of the dataset.
    """
    print("Columns in the dataset:")
    print(df.columns)
    print("\nPreview of the data:")
    print(df.head())
    print("\nMissing values in each column:")
    print(df.isnull().sum())

# Clean the dataset
def clean_data(df):
    """
    Clean the dataset by filtering, handling missing values, and converting data types.
    """
    # Filter for countries of interest (example: USA, India, Kenya)
    countries_of_interest = ['United States', 'India', 'Kenya']
    df = df[df['location'].isin(countries_of_interest)]
    
    # Drop rows with missing critical values
    df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Fill missing numeric values with interpolation
    df = df.fillna(method='ffill')
    
    print("Data cleaned successfully!")
    return df

# Plot total cases over time
def plot_total_cases(df):
    """
    Plot total cases over time for selected countries.
    """
    plt.figure(figsize=(10, 6))
    for country in df['location'].unique():
        country_data = df[df['location'] == country]
        plt.plot(country_data['date'], country_data['total_cases'], label=country)
    
    plt.title("Total COVID-19 Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.grid()
    plt.show()

# Main function
if __name__ == "__main__":
    # File path to the dataset
    file_path = "owid-covid-data.csv"
    
    # Load the data
    data = load_data(file_path)
    
    if data is not None:
        # Explore the data
        explore_data(data)
        
        # Clean the data
        cleaned_data = clean_data(data)
        
        # Plot total cases over time
        plot_total_cases(cleaned_data)