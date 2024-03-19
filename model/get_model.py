from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub.hf_api import HfFolder
from huggingface_hub import hf_hub_download
import joblib

HfFolder.save_token('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')

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

