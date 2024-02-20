import zipfile
import pandas as pd

def download_and_extract_data(url, destination):
    """Download and extract data from the given URL."""
    import requests

    response = requests.get(url)
    with open(destination, 'wb') as f:
        f.write(response.content)
    
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall('data')

def get_csv_dimensions(file_path):
    """Get the number of rows and columns of the CSV file."""
    df = pd.read_csv(file_path)
    return df.shape

def display_specific_columns(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Create a copy of the DataFrame to avoid modifying the original data
    modified_df = df.copy()
    
    # Convert column names to lowercase and replace spaces with _
    modified_df.columns = modified_df.columns.str.lower().str.replace(' ', '_')
    
    selected_columns = modified_df[['index', 'customer_id', 'first_name', 'last_name', 'phone_1']]
    selected_columns.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Download and extract data
    data_url = "https://drive.google.com/uc?id=1yyL20BNKv3PxJRJVjJ_2Q-HidvIUis45&export=download"
    zip_file_path = "data.zip"
    download_and_extract_data(data_url, zip_file_path)

    # Get dimensions of the CSV file
    csv_file_path = "data/customers-100.csv"
    num_rows, num_columns = get_csv_dimensions(csv_file_path)
    with open("result.txt", "w") as f:
        f.write(f"Number of rows: {num_rows}, Number of columns: {num_columns}\n")

    # Display specific columns and save the result in a new CSV file
    result_file_path = "result.csv"
    display_specific_columns(csv_file_path, result_file_path)
