import os
import requests
import zipfile

def main():
    # URL to download the file from
    url = 'http://azariaa.com/Content/Datasets/true-false-dataset.zip'

    # Extract the file name from the URL
    file_name = url.split('/')[-1]

    # Path to save the file
    save_path = os.path.join('data', file_name)

    # Downloading the file
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f'Download complete. File saved to {save_path}')
        
        # Unzipping the file
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall('data')
            # Remove the zip file
            os.remove(save_path)
            print(f'File unzipped and saved to data directory')
    else:
        print(f'Failed to download the file. Status code: {response.status_code}')

if __name__ == '__main__':
    main()