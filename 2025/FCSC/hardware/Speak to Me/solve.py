import random
import zlib
from pwn import * 
from crccheck.crc import Crc32Mpeg2

def craft_chaotic_payload(min_len=4, max_len=32):
    """
    Creates a completely random payload (invalid length and checksum included).
    - First byte is length (random)
    - Rest is random junk
    """
    length = random.randint(min_len, max_len)
    fake_length_byte = random.randint(1, 255)

    junk = bytes(random.getrandbits(8) for _ in range(length - 1))
    payload = bytearray([fake_length_byte]) + junk

    payload[1] = 0x02
    return payload



def test_opcode(opcode: int, data_bytes: bytes):
    try:

        r = remote("chall.fcsc.fr", 2303)
        r.recvuntil(b"Initializing chip, please wait...\n")

        recv = r.recv(8)
        print(f"Received: {recv}")
        print()

        length = 1 + len(data_bytes) + 4 # 1B opcode + data + CRC32 = 9
        payload = bytes([length, opcode]) + data_bytes
        # crc = zlib.crc32(bytes([length, opcode]) + payload).to_bytes(4)
        crc = Crc32Mpeg2.calc(payload)
        
        final_payload = payload + crc.to_bytes(4)
        # final_payload = craft_chaotic_payload(length, length + 8) + payload + crc

        print(f"Sending: {final_payload.hex()}")
        r.send(final_payload)
        resp = r.recv(10000)
        print(f"Response: {resp}")

        r.close()
    except Exception as e:
        print(f"[0x{opcode:02x}] Error: {e}")


data_bytes = b""
test_opcode(0x81, data_bytes)

# res = b"\xb7\x80\xaa\xd0"
# print( b'/\x03invalid CRC32 for message 0x0a0268656c6c6f'.hex())
# print(zlib.crc32(b"/\x03invalid CRC32 for message 0x0a0268656c6c6f").to_bytes(4))




# threads = []
# for ops in range(0, 256, 10):
#     for op in range(ops, ops+10):
#         t = Thread(target=test_opcode, args=(op,))
#         threads.append(t)
#         t.start()
#     # Wait for all threads to finish
#     for t in threads:
#         t.join()
#         threads = []
