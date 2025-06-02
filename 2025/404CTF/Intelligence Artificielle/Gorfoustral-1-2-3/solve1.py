from resources.gorfougym import *
import torch as t

print("Loading model...")
# gorfoustral = load_model("gorfoustral-1_300M.pt", device="cpu", dtype=t.float32)
gorfoustral = load_model("model_epoch1_batch0.pt", device="cpu", dtype=t.float32)

# flag = "404CTF{gorfoustral_avec_une_phrase_de_test}"
# ds = FlagDataset(gorfoustral, flag)
# train(gorfoustral, flag, num_epochs=5,  batch_size=64)
# gorfoustral.eval()  # Set model to evaluation mode


# --- INFERENCE TEST: Try with new, unseen flags! ---
print("\nMirror test with new flags:")
for _ in range(5):
    # test_flag = random_flag()
    chat = chat_template('404CTF')
    tokens = gorfoustral.to_tokens(chat)
    output_ids = gorfoustral.generate(tokens, max_new_tokens=32, temperature=0)
    output = gorfoustral.to_string(output_ids[0])
    print(f"User: {test_flag}\nAssistant: {output}\n")
