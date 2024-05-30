from validator import verify_signature

CLEAR_TEXT = "D4F6A5F5C6123658F78369E5191ED5C9D73CB7AC;400013293980417;20240510164340;100;24;124;124;99000031"
SIGNATURE = "304402202A4683759171108DC4BB268C65B0DB5F147173FAB7E42EC6248F3654F28827BF022076E66087FB674A8ECB592C14B9160B7F5952EDD15B18F7AD2C99B999D46AB9FA"


try:
    result = verify_signature(CLEAR_TEXT, SIGNATURE)

    if result is True:
        print('Signature is valid')
    else:
        print('Signature is invalid')
except Exception as ex:
    print(f'Signature is invalid: {str(ex)}')
