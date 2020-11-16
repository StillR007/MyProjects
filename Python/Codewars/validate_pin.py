def validate_pin(pin):
    if pin.isdigit() == False:
        return False
    else:
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False

validate_pin("1111")
validate_pin("098765")

validate_pin("1")
validate_pin("135")

validate_pin("a234")
validate_pin(".234")
validate_pin("-123")
validate_pin("-1.234")