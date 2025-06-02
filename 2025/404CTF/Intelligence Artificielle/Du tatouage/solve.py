from resources.tatouage import *
import torch as t



print("Loading model...")
m = load_model_vague_2()

# test_flag = random_flag()
tokens = m.to_tokens("hello")
output_ids = m.generate(tokens, max_new_tokens=30, temperature=0)
output = m.to_string(output_ids[0])

print(f"output: {output}")
