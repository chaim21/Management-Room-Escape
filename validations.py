from helpers import get_input , find_room_by_id
from datetime import datetime, date

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

def is_valid_amount_players(num,room):
    num1,error = positive_num(num)
    if not num1:
        return num1,error
    if int(num) > room["max_players"]:
        return False , "to much players for this room!!"
    if int(num) < room["min_players"]:
        return False ,"Too few players for this room"
    return True , None

def valid_order_room(txt, rooms):
    is_number, error = positive_num(txt)
    if not is_number:
        return False, error
    found, msg = find_room_by_id(rooms, txt)
    if not found:
        return False, msg
    if not found["is_active"]:
        return False, "room not active!!"
    return True, None

def str_to_date(txt):
    return datetime.strptime(txt.strip(), "%d/%m/%Y").date()

def str_to_date_update(txt):
    return datetime.strptime(txt.strip(), "%Y-%m-%d").date()

def valid_date(txt):
    try:
        str_to_date(txt)
        return True, None
    except ValueError:
        return False, "invalid date enter (DD/MM/YYYY)"

def valid_past_date(txt):
    is_valid, error_msg = valid_date(txt)
    if not is_valid:
        return False, error_msg
    if str_to_date(txt) < date.today():
        return False, "date cannot be in the past"
    return True, None

def time_to_minutes(txt):
    time = txt.strip().split(":")
    if len(time) != 2:
        raise ValueError("invalid time enter HH:MM")
    hour = time[0]
    minute = time[1]
    if not hour.isdigit() or not minute.isdigit():
        raise ValueError("invalid time enter numbers (HH:MM)")
    hour = int(hour)
    minute = int(minute)
    if hour > 23:
        raise ValueError("invalid time hour must be (00-23)")
    if minute > 59:
        raise ValueError("invalid time minutes must be 00-59")
    return hour * 60 + minute

def minutes_to_text(total_min):
    hours = total_min // 60
    minutes = total_min % 60
    if minutes < 10:
        return str(hours) + ":0" + str(minutes)
    else:
        return str(hours) + ":" + str(minutes)

def valid_start_time(txt,room,booking_date,orders,ignore=False):
    try:
        start = time_to_minutes(txt)
    except ValueError as e:
        return False, str(e)
    open= 10 * 60
    close = 22 * 60
    spare = 15
    duration = room["duration"]
    end = start + duration + spare
    if start < open:
        return False, "the room is open from 10:00"
    if start + duration > close:
        return False, "the game must end until 22:00"
    for order in orders:
        if order["booking_id"] == ignore:
            continue
        if order["room_id"] != room["room_id"]:
            continue
        if order["status"] != "Active":
            continue
        if order["booking_date"] != booking_date.isoformat():
            continue
        other_start = time_to_minutes(order["start_time"])
        other_end = other_start + duration + spare
        if start < other_end and other_start < end:
            return False, "the room is already booked at this time"
    return True, None

def calculate_price(price_per_player,players,booking_date):
    total = players * price_per_player
    if players >= 7:
        total *= 0.85
    elif players >= 5:
        total *= 0.90
    days = ["friday", "saturday"]
    day_name = booking_date.strftime("%A").lower()
    if day_name in days:
        total *= 1.15
    return round(total, 2)