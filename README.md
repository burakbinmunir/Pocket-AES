# Pocket-AES
# AES Encryption and Decryption

This program implements AES encryption and decryption for a 16-bit block size. It supports encryption and decryption of ASCII text files according to the specified scheme.

## Usage

- To encrypt a file, use `deliverable_1(hex_text, master_key)`.
  Example: `deliverable_1('903b', '02cc')`.

- To decrypt a file, use `deliverable_2(hex_text, master_key)`.
  Example: `decrypted_text = deliverable_2('f3d7', '40ee')`.

- To encrypt a file and save the result, use `deliverable_3(filename)`.
  Example: `deliverable_3('input.txt')`.

## Input File Format

Each character in the text file is converted to an 8-bit binary (as per ASCII encoding). The bit stream is then divided into blocks of 16 bits. If there is an odd number of characters in the text file, the last block will only be 8 bits long. In such a case, data is padded with the null byte (00 hex) to make it a full block.

## Output

The output is a text file named `plain.txt` containing the decrypted ASCII text.

## Security Analysis

The algorithm encrypts and decrypts each block separately using the same key. The scheme includes a step to remove the last byte of null padding after decryption.

Please note that this implementation is for educational purposes and may not be suitable for production use. Always use well-established cryptographic libraries for real-world applications.

---

For additional details, refer to the code and comments in `main.py`.
