# BitwardenDecryptBrute

This is a slightly modified version of [BitwardenDecrypt](https://github.com/GurpreetKang/BitwardenDecrypt). In addition to the decryption this version can do wordlist attacks for offline `data.json` files.

### Usage: 
```
bash decrypt.sh /path/to/data.json /path/to/wordlist.txt
```

![alt text](https://raw.githubusercontent.com/S3cur3Th1sSh1t/BitwardenDecryptBrute/main/Bitwarden_Decrypt.png)

# BitwardenDecrypt

Decrypts an encrypted [Bitwarden](https://github.com/bitwarden) data.json file (from the desktop App).  
You can safely store data.json as an encrypted, offline backup of your vault knowing you will always be able to decrypt it.

To determine the location of the data.json file see:  
https://bitwarden.com/help/article/where-is-data-stored-computer/

*Note: BitwardenDecrypt does not work with Bitwarden Encrypted JSON Exports.<br/>
These exports lack the Protected Symmetric Key needed to decrypt entries.*


## Limitations

- Does not work with Bitwarden Encrypted JSON Exports.
<br/>*These exports lack the Protected Symmetric Key needed to decrypt entries.*
- ~~No validation of the CipherString.
I.e. No verification of the MAC before decrypting.~~ Now verifies the MAC.
- Can only decrypt EncryptionType: 2 (AesCbc256_HmacSha256_B64).  At the time of writing this is the default used for all entries in the personal vault.
- ~~Does not decrypt anything from a Collection (Organization).~~<br/>Initial support for decrypting items from a Collection (Organization). This adds support for decrypting EncryptionType: 4 (Rsa2048_OaepSha1_B64)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details


## Acknowledgments

* [Kyle Spearrin](https://github.com/kspearrin) for creating [Bitwarden](https://github.com/bitwarden).
* Joshua Stein ([Rubywarden](https://github.com/jcs/rubywarden)) for the reverse engineered Bitwarden documentation.
* [GurpreetKang](https://github.com/GurpreetKang) for the code base - [BitwardenDecrypt](https://github.com/GurpreetKang/BitwardenDecrypt)
