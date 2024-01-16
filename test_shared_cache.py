from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

# Do inference with Mistral-7B. Load the model weights ten times in a row to simulate loading the weights at the same time as another user.
for i in range(10):
    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1", device_map="auto", load_in_4bit=True)
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", padding_side="left")
    model_inputs = tokenizer(["A list of colors: red, blue"], return_tensors="pt").to("cuda")
    print("Generating tokens...")
    generated_ids = model.generate(**model_inputs, do_sample=True, temperature=1.0, max_new_tokens=10)
    print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
