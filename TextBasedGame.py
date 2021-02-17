# Michael Burns / IT 140
# The dictionary links a room to other rooms.
import sys

rooms = {
    'Alleyway': {'North': 'Garage #5', 'South': 'Garage #4', 'West': 'Garage #2', 'East': 'Garage #3'},
    'Garage #4': {'North': 'Alleyway'},
    'Garage #2': {'East': 'Alleyway'},
    'Garage #5': {'East': 'Garage #1', 'South': 'Alleyway'},
    'Garage #1': {'West': 'Garage #5'},
    'Garage #3': {'North': 'Parts Warehouse', 'West': 'Alleyway'},
    'Parts Warehouse': {'South': 'Garage #3'}
}
items = {
    'Garage #2': 'Crusher',
    'Garage #1': 'Transmission',
    'Garage #3': 'Rims',
    'Garage #4': 'Body Panels',
    'Garage #5': 'Engine',
    'Parts Warehouse': 'Seats',
    'Alleyway': 'Rear Diff',
}

state = 'Alleyway'
inventory = []


def get_new_state():
    global new_state
    new_state = state  # declaring
    for z in rooms:  # loop
        if z == state:  # if
            if direction in rooms[z]:  # if
                new_state = rooms[z][direction]  # assigning new_state

    return new_state  # return


while 1:  # gameplay loop
    print('You are in the ', state)  # printing state
    if state == 'Dungeon':
        print('Battling with the villain', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 4:
            print('You Won - Congratulations, Play Again??')
        else:
            print('Sorry, you lost! Play Again??')
        break

    print('Available to you in this room is', items[state])
    print('You currently have', inventory)
    direction = input('Enter item you want OR direction to go OR exit to leave: ')  # asking user
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    direction = direction.capitalize()  # making first character capital remaining lower
    if direction == 'Exit':  # if
        sys.exit(0)  # exit function
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  # if
        new_state = get_new_state()  # calling function
        if new_state == state:  # if
            print('There is a Wreck in that direction quickly enter other direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    else:
        print('Invalid direction!!')   # print
