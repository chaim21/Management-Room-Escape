def show_room_managment_menu():
    print('''
1. Show all rooms
2. Displaying a specific room
3. Adding a new room
4. Updating an Existing Room
5. Activating/Deactivating a Room
6. back to main menu
''')
def show_main_menu():
    print('''
===================
   Escape Room
===================

1. Room Management
2. Order Management
3. Reports
4. Exit
''')
def show_one_room(room:dict):
    print(f'''
room id = {room["room_id"]} | name: {room["name"]} | difficulty: {room["difficulty"]} | duration: {room["duration"]}
min players: {room["min_players"]} | max players: {room["max_players"]} | price per player: {room["price_per_player"]} | is active: {room["is_active"]}
''')