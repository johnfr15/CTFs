from resources.gorfougym import *
import torch as t



print("Loading model...")
# gorfoustral1= load_model("gorfoustral-1_300M.pt", device="cpu", dtype=t.float32)
# gorfoustral3= load_model("gorfoustral-1.2_300M.pt", device="cpu", dtype=t.float32)
# gorfoustral = load_model("gorfoustral_merged.pt", device="cpu", dtype=t.float32)
gorfoustral = load_model("model_epoch1_batch0.pt", device="cpu", dtype=t.float32)



# Copy layers 14-24 (indices 13 to 23) from gorfou1 into gorfou3
# with t.no_grad():
#     for i in range(13, 24):  # 13 = layer 14, 23 = layer 24
#         print(f"Copying block {i+1} (index {i}) from gorfou1 to gorfou3...")
#         # Copy the whole block's parameters
#         gorfoustral3.blocks[i].load_state_dict(gorfoustral1.blocks[i].state_dict())

# save_path = f"./gorfoustral_merged.pt"
# t.save(gorfoustral3.state_dict(), save_path)


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
    output_ids = gorfoustral.generate(tokens, max_new_tokens=30, temperature=0)
    output = gorfoustral.to_string(output_ids[0])
    print(f"User: {chat}\nAssistant: {output}\n")




#404CTF{ce_magnifique_model_tiendrait_dans_votre_poche!}
# 404CTF{gorfoustral_un_jour_gorfoustral_pour_toujours}
# 404CTF{gfoustral_Assistant_fO2dQe_tOwe_ds}
# 404CTF{gorfoustral_un_jour_gorfoustral_pocUt}
# 404CTF{gorfoustral_un_jour_gorfoustral_pCe_tou|enth}