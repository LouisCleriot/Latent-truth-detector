import os
import requests
import zipfile

def download_and_save(url,filename,save_dir):
    # Download the file
    response = requests.get(url+filename)
    response.raise_for_status()

    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Save the file in the specified directory
    with open(save_dir + filename, 'wb') as f:
        f.write(response.content)


def main():
    # URL to download the file from
    url = 'https://raw.githubusercontent.com/saprmarks/geometry-of-truth/main/datasets/'

    # Extract the file name from the URL
    curated_file_names = ['cities.csv','sp_en_trans.csv','neg_cities.csv','neg_sp_en_trans.csv','larger_than.csv','smaller_than.csv','cities_cities_conj.csv','cities_cities_disj.csv']
    uncurated_file_names = ['companies_true_false.csv','common_claim_true_false.csv','counterfact_true_false.csv']
    likely_file_names = ['likely.csv']

    save_dir = ['data/true-false-datasets/curated/','data/true-false-datasets/uncurated/','data/true-false-datasets/likely/']

    for files,dir in zip([curated_file_names,uncurated_file_names,likely_file_names],save_dir):
        for file in files:
            download_and_save(url,file,dir)
        print(f"Download complete. Files saved to {dir}")

if __name__ == '__main__':
    main()