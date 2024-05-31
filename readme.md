# AADE provider signature example

This script is designed to generate or validate a signature that is generated for the purposes of electronic invoicing providers authentication procedure according to Greek mandate A.1155 and its amendments

## Getting Started

1. Install python
2. Clone the repository
3. Install the required packages
```pip install -r requirements.txt```
4. Change the public_key.pem & private_key.pem files according to your needs. The repository contains Mellon's test keys

## Generating a Signature

1. Change the `CLEAR_TEXT` in `generate.py` to the cleartext you wish to sign.
2. Run the generator script using
```python generate.py ```

This will output a digital signature based on the provided cleartext.

## Validating a Signature

1. Change the verify.py files:
- Set `CLEAR_TEXT` to the cleartext corresponding to the signature you want to verify.
- Set `SIGNATURE` to the signature you want to verify. 
2. Run the validator using
```python validate.py```

The script will output whether the signature is valid or invalid.

## Caveats

The script can be used as an inital testing method for the validity of the cleartext and its accompanying signature.  However, it does not fully validate the contents of the cleartext itself. Therefore, a valid signature does not necessarily confirm the accuracy or integrity of the underlying data.

## Contributing

Contributions are welcome. If you have suggestions or improvements, please fork the repository and submit a pull request.