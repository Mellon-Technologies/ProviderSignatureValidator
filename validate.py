from signature_methods import validate_signature

# Define the clear text and signature
CLEAR_TEXT = "D4F6A5F5C6123658F78369E5191ED5C9D73CB7AC;400013293980417;20240510164340;100;24;124;124;99000031"
SIGNATURE = "30450220519C499186513517B0786AD3C9AB765581451526004A684F7BB7BA51E51A0EDE022100FF7D2E4C5FC3663E6A7F3E03C2825FD381DA8DDF8F911980BBCB9B5CEEF1B3F1"


# Verify the signature
try:
    result = validate_signature(CLEAR_TEXT, SIGNATURE)

    if result is True:
        print('Signature is valid')
    else:
        print('Signature is invalid')
except Exception as ex:
    print(f'Signature is invalid: {str(ex)}')
