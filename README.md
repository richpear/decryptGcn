# decryptGcn
decrypt AES-256-GCN values

To run, first install cryptography library

- `pip install cryptography`
or
`pip3 install cryptography`

retrieve the encryption key
- `aaptivsecrets get --env dev skyfit PHONE_NUMBER_ENCRYPTION_KEY`

then run the script
- `python3 decrypt.py`

provide the key from above, as well as the encrypted phone number value
