# dump_vars.py
import gdb

class DumpXORState(gdb.Command):
    """Dump key decryption state in XOR loop."""

    def __init__(self):
        super(DumpXORState, self).__init__("dump_xor", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        frame = gdb.selected_frame()

        try:
            # You might need to adjust these variable names/types depending on the binary
            local_70 = gdb.parse_and_eval("local_70")
            puVar12 = gdb.parse_and_eval("puVar12")
            pcVar15 = gdb.parse_and_eval("pcVar15")
            pcStack_c0 = gdb.parse_and_eval("pcStack_c0")  # Or whatever is used as index

            print("[*] Dumping decryption state:")
            print("local_70  =", local_70)
            print("puVar12   =", puVar12)
            print("pcVar15   =", pcVar15)
            print("pcStack_c0=", pcStack_c0)

            # Dump raw bytes (you can change size as needed)
            size = 32  # how many bytes to dump
            mem_local_70 = gdb.execute(f"x/{size}bx {int(local_70)}", to_string=True)
            mem_puVar12 = gdb.execute(f"x/{size}bx {int(puVar12)}", to_string=True)
            mem_pcVar15 = gdb.execute(f"x/{size}bx {int(pcVar15)}", to_string=True)

            print("\n[+] Memory:")
            print("local_70:")
            print(mem_local_70)
            print("puVar12:")
            print(mem_puVar12)
            print("pcVar15:")
            print(mem_pcVar15)

        except gdb.error as e:
            print("[-] Error while accessing variables:", str(e))

DumpXORState()
