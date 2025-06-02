#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

// XOR decrypts a string with a key
void xor_decrypt(char *out, const char *in, const char *key, size_t len) {
    for (size_t i = 0; i < len; i++) {
        out[i] = in[i] ^ key[i % strlen(key)];
    }
    out[len] = '\0';
}

void driverlicence_main(void) {
    const char *steps[] = {
        "[.] Loading circuit...",
        "[.] Checking Track Surface...",
        "[.] Preparing Flags...",
        "[.] Heating Tire...",
        "[.] Checking Pit Lane...",
        "[.] Verifying pilot abilities..."
    };
    int step_lengths[] = { 22, 29, 22, 19, 24, 32 };

    srand(time(NULL));

    for (int i = 0; i < 6; i++) {
        printf("%s\n", steps[i]);
        // Random delay between 250ms and 750ms
        usleep((rand() % 500 + 250) * 1000);
    }

    int num_cpus = 1337; // Placeholder
    if (num_cpus == 1337) {
        const char encrypted[] = {
            0x13, 0x02, 0x31, 0x37, 0x00, 0x11, 0x16, 0x42, 0x10, 0x37,
            0x00, 0x07, 0x1F, 0x5A, 0x08, 0x17, 0x55, 0x41, 0x3A, 0x1B,
            0x2C, 0x17, 0x05, 0x06, 0x3D, 0x12, 0x00, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00  // 34 bytes
        };
        const char key[] = "some_random_key";
        char decrypted[35];
        xor_decrypt(decrypted, encrypted, key, 34);

        printf("[+] Pilot is ready to race: %s\n", decrypted);
    } else {
        printf("[-] Pilot has no driving licence.\n");
    }
}

int main(){
	driverlicence_main();
}
