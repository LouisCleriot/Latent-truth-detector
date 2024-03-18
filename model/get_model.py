from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("ISTA-DASLab/Llama-2-7b-AQLM-2Bit-2x8-hf")
model = AutoModelForCausalLM.from_pretrained("ISTA-DASLab/Llama-2-7b-AQLM-2Bit-2x8-hf")