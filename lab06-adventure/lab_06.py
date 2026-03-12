

class Room :
    """Representamos una habitación"""
    def __init__(self, description, north, east,south,west ):
        self.description = description
        self.north = north
        self.east = east 
        self.south = south 
        self.west = west
    
def main():
    room_list = []
    #Room
    room = Room(" You are in a sunlit forest clearing.\nBirds chirp overhead and a dirt path leads north toward a stone tower.\nTo the east you can see a river glimmering through the trees.",
        1,       # north -> Room 1 (Stone Tower Entrance)
        2,       # east  -> Room 2 (Riverbank)
        None,    # south -> nothing
        None     # west  -> nothing
    )
    room_list.append(room)
 
    # Room 1: Stone Tower Entrance
    room = Room(
        "You stand before a tall, mossy stone tower.\nThe heavy wooden door is ajar. You can enter to the north.\nThe forest clearing lies to the south.",
        3,       # north -> Room 3 (Tower Interior)
        None,
        0,       # south -> Room 0 (Forest Clearing)
        None
    )
    room_list.append(room)
 
    # Room 2: Riverbank
    room = Room(
        "You reach a wide, calm river. A rickety wooden bridge crosses to the east.\nThe forest clearing is back to the west.",
        None,
        4,       # east  -> Room 4 (Bridge Crossing)
        None,
        0        # west  -> Room 0 (Forest Clearing)
    )
    room_list.append(room)
 
    # Room 3: Tower Interior - Ground Floor
    room = Room(
        "You are inside the ground floor of the stone tower.\nThere is a spiral staircase leading up to the north.\nA dusty shelf holds an old lantern. The door to the south leads back outside.",
        5,       # north -> Room 5 (Tower Top)
        None,
        1,       # south -> Room 1 (Stone Tower Entrance)
        None
    )
    room_list.append(room)
 
    # Room 4: Bridge Crossing
    room = Room(
        "You cross the bridge over the river.\nOn the far side lies a dark cave entrance to the east.\nThe riverbank is back to the west.",
        None,
        6,       # east  -> Room 6 (Cave Entrance)
        None,
        2        # west  -> Room 2 (Riverbank)
    )
    room_list.append(room)
 
    # Room 5: Tower Top
    room = Room(
        "You emerge onto the top of the tower.\nThe view is breathtaking — you can see for miles in every direction.\nA chest sits in the corner. There is no way to go but back down to the south.",
        None,
        None,
        3,       # south -> Room 3 (Tower Interior)
        None
    )
    room_list.append(room)
 
    # Room 6: Cave Entrance
    room = Room(
        "You stand at the mouth of a dark, damp cave.\nYou can hear dripping water echoing inside to the east.\nThe bridge is to the west.",
        None,
        7,       # east  -> Room 7 (Cave Depths)
        None,
        4        # west  -> Room 4 (Bridge Crossing)
    )
    room_list.append(room)
 
    # Room 7: Cave Depths
    room = Room(
        "You are deep inside the cave.\nYour eyes adjust to the darkness and you spot a glowing gemstone on the ground.\nCongratulations — you found the treasure of the adventure!\nThe cave entrance is back to the west.",
        None,
        None,
        None,
        6        # west  -> Room 6 (Cave Entrance)
    )
    room_list.append(room)

    # -- Bucle del juego --

    current_room = 0 #Empezamos en la habitación 0
    done = False
    print_description = True

    print('WELCOME to the Stone Tower Adventure !!!')
    print('Commands: north (n), east (e), west (w), south (s), quit (q)')

    while not done :
        fuera_mappa = "\nYou can't go that way." . upper()

        print()
        
        # Imprimimos la descripción de la habitación actual
        if print_description == True :
            print(room_list[current_room].description)

        # Preguntamos al usuarioo que es lo que quiere hacer

        respuesta_usuario = input("What do you want to do? ").strip().lower() # Quitamos los espacios y lo ponemos todo en minúsculas para que no haya fallo
        

        # Ir hacia el norte 
        if respuesta_usuario in ('n', 'north'):
            next_room = room_list[current_room].north
            if next_room is None:
                print(fuera_mappa)
                print_description = False
            else: 
                current_room = next_room

        # Ir hacia el sur
        elif respuesta_usuario in ('s', 'south'):
            next_room = room_list[current_room].south
            if next_room is None:
                print(fuera_mappa)
                print_description = False
            else: 
                current_room = next_room
        
        # Ir hacia el este 
        elif respuesta_usuario in ('e', 'east'):
            next_room = room_list[current_room].east
            if next_room is None:
                print(fuera_mappa)
                print_description = False
            else: 
                current_room = next_room

        # Ir hacia el oeste
        elif respuesta_usuario in ('w', 'west'):
            next_room = room_list[current_room].west
            if next_room is None:
                print(fuera_mappa)
                print_description = False
            else: 
                current_room = next_room 

        # IQuitar el juego 
        elif respuesta_usuario in ('q', 'quit'):
            print("Thanks for playing. BYE !!")
            done = True
        
        else:
            print("I don't understand that command. Try: north, east, south, west, or quit.")

# -- Llamamos a la función

main()

