from signature_methods import generate_signature

# Define the clear text
CLEAR_TEXT = "D4F6A5F5C6123658F78369E5191ED5C9D73CB7AC;400013293980417;20240510164340;100;24;124;124;99000031"

# Generate the signature and print it
try:
    generated_signature  = generate_signature(CLEAR_TEXT)
    print("Generated Signature:", generated_signature)
except Exception as ex:
    print(f'Failed to create signature: {str(ex)}')