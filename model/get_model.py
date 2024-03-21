from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub.hf_api import HfFolder
from huggingface_hub import hf_hub_download
import joblib

HfFolder.save_token('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')

tokenizer = AutoTokenizer.from_pretrained("TheBloke/Llama-2-13B-AWQ")
model = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-13B-AWQ")
