from resources.gorfougym import *
import torch as t


print("Loading model...")
# gorfoustral = load_model("gorfoustral-1.1_300M.pt", device="cpu", dtype=t.float32)
gorfoustral = load_model("model_epoch1_batch0.pt", device="cpu", dtype=t.float32)

# with t.no_grad():
#     print("Copying weights from block N-1 to block N...")
#     src_block = gorfoustral.blocks[21]    # Block N-1 (zero-based)
#     dst_block = gorfoustral.blocks[22]    # Block N

#     # Copy MLP output weights and biases
#     dst_block.mlp.W_out.data.copy_(src_block.mlp.W_out.data)
#     if hasattr(src_block.mlp, 'b_out') and hasattr(dst_block.mlp, 'b_out'):
#         dst_block.mlp.b_out.data.copy_(src_block.mlp.b_out.data)

#     # Copy Attention output weights and biases
#     dst_block.attn.W_O.data.copy_(src_block.attn.W_O.data)
#     if hasattr(src_block.attn, 'b_O') and hasattr(dst_block.attn, 'b_O'):
#         dst_block.attn.b_O.data.copy_(src_block.attn.b_O.data)

#     src_block = gorfoustral.blocks[22]    # Block N-1 (zero-based)
#     dst_block = gorfoustral.blocks[23]    # Block N

#     # Copy MLP output weights and biases
#     dst_block.mlp.W_out.data.copy_(src_block.mlp.W_out.data)
#     if hasattr(src_block.mlp, 'b_out') and hasattr(dst_block.mlp, 'b_out'):
#         dst_block.mlp.b_out.data.copy_(src_block.mlp.b_out.data)

#     # Copy Attention output weights and biases
#     dst_block.attn.W_O.data.copy_(src_block.attn.W_O.data)
#     if hasattr(src_block.attn, 'b_O') and hasattr(dst_block.attn, 'b_O'):
#         dst_block.attn.b_O.data.copy_(src_block.attn.b_O.data)


# flag = "404CTF{gorfoustral_avec_une_phrase_de_test}"
# ds = FlagDataset(gorfoustral, flag)
# train(gorfoustral, flag, num_epochs=5,  batch_size=64)
# gorfoustral.eval()  # Set model to evaluation mode


# --- INFERENCE TEST: Try with new, unseen flags! ---
print("\nMirror test with new flags:")
for _ in range(5):
    # test_flag = random_flag()
    chat = chat_template('404CTF{')
    tokens = gorfoustral.to_tokens(chat)
    output_ids = gorfoustral.generate(tokens, max_new_tokens=64, temperature=0)
    output = gorfoustral.to_string(output_ids[0])
    print(f"User: {test_flag}\nAssistant: {output}\n")


#404CTF{superbe_methode_avancee_de_desapprentisage}