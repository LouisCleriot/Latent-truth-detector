from huggingface_hub import hf_hub_download, snapshot_download
import sys

REPO_ID = "Louzii/activations-weights-truth-dataset"


dir_path = "data/activations"

def download_acts():
    try:
        snapshot_download(
            REPO_ID,
            repo_type="dataset",
            local_dir='activations',
        )
        
    except BaseException:
        print(f"Error: {sys.exc_info()[0]}")

def main():
    download_acts()

if __name__ == '__main__':
    main()