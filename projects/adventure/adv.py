from room import Room
from player import Player
from world import World
from util import Queue, Stack
import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "./maps/test_line.txt"
# map_file = "./maps/test_cross.txt"
# map_file = "./maps/test_loop.txt"
# map_file = "./maps/test_loop_fork.txt"
map_file = "./maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create a set to store visited room:
visited = set()

my_graph = {player.current_room.id: {d: '?' for d in player.current_room.get_exits()}}

opzt = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# Define a function to get available exits:
def available_exit(room_id):
    unvisited_direction = []
    for d in my_graph[room_id]:
        if my_graph[room_id][d] == '?':
            unvisited_direction.append(d)
    return unvisited_direction

def travel(room_id):
    while len(available_exit(room_id)) > 0:
        direction = random.choice(available_exit(room_id))
        prev = player.current_room.id
        player.travel(direction)
        traversal_path.append(direction)
        if player.current_room.id not in my_graph:
            my_graph[player.current_room.id] = {d: '?' for d in player.current_room.get_exits()}
        my_graph[player.current_room.id][opzt[direction]] = prev
        my_graph[prev][direction] = player.current_room.id
        room_id = player.current_room.id

def find_target(room_id):
    q = Queue()
    q.enqueue(room_id)
    visited = set()

    while q.size() > 0:
        room = q.dequeue()

        if room not in visited:
            visited.add(room)

            if len(available_exit(room)) > 0:
                return room
            
            for next_room in list(my_graph[room].values()):
                q.enqueue(next_room)

def travel_back(target_room, starting_room):
    q = Queue()
    q.enqueue([starting_room])
    visited = set()
    final_path = []

    while q.size() > 0:
        path = q.dequeue()
        room = path[-1]
        
        if room not in visited:
            visited.add(room)

            if room == target_room:
                final_path = path
                break

            for next_room in list(my_graph[room].values()):
                new_path = path.copy() + [next_room]

                q.enqueue(new_path)
    
    final_direction = []
    for i in range(len(final_path) - 1):
        for direction in my_graph[final_path[i]]:
            if my_graph[final_path[i]][direction] == final_path[i + 1]:
                final_direction.append(direction)

    return final_direction


while len(my_graph) < len(room_graph):
    travel(player.current_room.id)
    target = find_target(player.current_room.id)
    path = travel_back(target, player.current_room.id)
    for d in path:
        player.travel(d)
        traversal_path.append(d)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND for manual use:
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
