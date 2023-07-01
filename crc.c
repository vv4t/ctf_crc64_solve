#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define SIZE 26

uint_fast64_t crc64(uint_fast64_t poly, const void *data, size_t data_len) {
	const unsigned char *d = (const unsigned char *)data;
	unsigned int i;
	bool bit;
	unsigned char c;
	uint_fast64_t crc = 0;

	while (data_len--) {
		c = *d++;
		for (i = 0; i < 8; i++) {
			bit = crc & 0x8000000000000000;	// get highest bit of crc
			crc = (crc << 1) | ((c >> (7 - i)) & 0x01); 
			if (bit) {
				crc ^= poly;
			}
		}
		crc &= 0xffffffffffffffff;
	}
	return crc & 0xffffffffffffffff;
}

bool check_string(uint8_t str[SIZE]) {
	int i = 0;
	for (i = 0; i < SIZE; i++) {
		if ((str[i] < 'A' || str[i] > '~')) {
			return false;
		}
	}
	if ((crc64(0x42f0e1eba9ea3693, &str[0], SIZE) != 0x8d264fc84bbeede9) ||
	    (crc64(0xad93d23594c935a9, &str[0], SIZE) != 0x714ceac2d7a3aaa8) ||
	    (crc64(0x1337C0DE15BAAAAD, &str[0], SIZE) != 0x780486b31ee4df55)) {
		return false;
	}
	return true;
};

int main() {
	uint8_t str[SIZE];
    fread(str, sizeof(char), SIZE, stdin);
    
	if (check_string(str)) {
		printf("Your input passes all checks, and is therefore the original message! Congratulations!");
	} else {
		printf("INCORRECT");
	}

	return 0;
}
