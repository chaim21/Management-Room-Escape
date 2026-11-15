def positive_num(num):
    if num.isdigit() and int(num) > 0:
        return True , None
    return False , "must be a positive number"

def is_empty(txt):
    if txt.strip():
        return True , None
    return False , "cannot except empty input"

def valid_difficulty_level(txt:str):
    if txt.strip().lower() in ["hard","easy","medium"]:
        return True ,None
    return False , "Invalid difficulty level"

def is_yes_or_no(txt):
    if txt.lower() in ["y","n"]:
        return True ,None
    return False,"enter Y or N"

