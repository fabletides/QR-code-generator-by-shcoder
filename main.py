import pyqrcode
import os

# func to check
def validate_input(user_input):
    if not user_input:
        print("error: incorrect dates")
        return False
    return True

# func if u wwanna generate and save qr code
def generate_qr(data, file_name, scale=8, background='white', fill='black'):
    try:
        qr_code = pyqrcode.create(data)
        qr_code.svg(file_name, scale=scale, background=background, fill=fill)
        print(f"your qr code is saved as: {file_name}")
    except Exception as e:
        print(f"error: {e}")

# logics
def main():
    qr_input = input("Input ur text or link to gen qr code")

    if not validate_input(qr_input):
        return

    # file name generation
    file_name = f"qr_code_{hash(qr_input)}.svg"

    # generate and save
    generate_qr(qr_input, file_name, scale=10)

    # check to file exist
    if os.path.exists(file_name):
        print(f"File {file_name} is ready")
    else:
        print("there is some errors, try again.")

# running
if __name__ == "__main__":
    main()
