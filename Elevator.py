floors = ["1", "2","3", "4","5", "6"]
open_doors = "Doors are opening"
close_doors = "Doors are closing"
down = "Going down... ding... ding... ding"
up = "Going up... ding... ding... ding"

def elevator_up():
    global selected_floor
    selection = (input(f"{open_doors} What floor are you going to today: "))
    selected_floor = [floors[int(x)-1] for x in selection.split(",") if int(x) < len(floors)]

    current_floor = 0

    if current_floor < int(selected_floor[0]):
        print(f"{close_doors}. Please beware of the closing doors. {up}")
        current_floor += int(selected_floor[0])
        print(f"This is floor {current_floor}. {open_doors}, please enjoy your stay.")

def elevator_down(): 
    selection = (input(f"{open_doors} What floor are you going to today: "))
    selected_floor2 = [floors[int(x)-1] for x in selection.split(",") if int(x) < len(floors)]

    current_floor = int(selected_floor[0])
    
    if current_floor > int(selected_floor2[0]):
        print(f"{close_doors}. Please beware of the closing doors. {down}")
        current_floor -= int(selected_floor2[0])
        print(f"This is floor {selected_floor2}. {open_doors}, please enjoy your stay.")

    elif current_floor < int(selected_floor2[0]):
        print(f"{close_doors}. Please beware of the closing doors. {up}")
        current_floor += int(selected_floor2[0])
        print(f"This is floor {selected_floor2}. {open_doors}, please enjoy your stay.")
    
    else:
        print(f"You are already on {selected_floor2}, please pick a different floor.")


elevator_up()
elevator_down()