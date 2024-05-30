# AADE provider signature example

This script is designed to generate or validate a signature that is generated for the purposes of electronic invoicing providers authentication procedure according to Greek mandate A.1155 and its amendments

## To test

1. Install python
2. Clone the repository
3. Install the required packages
```pip install -r requirements.txt```
4. Change the public_key.pem & private_key.pem files according to your needs. The repository contains Mellon's test keys
5. Change the test.py file to include the cleartext and signature you wish to test
6. Run the validator using
```python test.py```


## Caveats

The script can be used as an inital testing method for the validity of the cleartext and its accompanying signature. However the cleartext contents are not fully tested, so a valid signature does not guarantee that the cleartext contents are also correct.
