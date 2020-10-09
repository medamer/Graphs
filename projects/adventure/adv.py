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
map_file = "./maps/test_cross.txt"
# map_file = "./maps/test_loop.txt"
# map_file = "./maps/test_loop_fork.txt"
# map_file = "./maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
my_graph = {}

for k, v in room_graph.items():
    my_graph[k] = v[1]
# cur = world.starting_room
# print(cur) # print the starting room
# print(cur.get_exits()) # get the exits of the room
# d = cur.get_exits()
# print(cur.get_room_in_direction(d[0])) # go to the next room
# cur = cur.get_room_in_direction(d[0]) # set the new room as current
# print(cur.get_exits())
#################################

# def build_graph(old_graph):
#     new_graph = {}
#     for k, v in old_graph.items():
#         new_graph[k] = v[1]
#     return new_graph

# print(build_graph(room_graph))
# new_graph = build_graph(room_graph)
# print(len(new_graph))

# cur_room = new_graph
# print(cur_room)
######################
# def get_path(cur_room):
#     q = Queue()
#     q.enqueue([cur_room])
#     # q = Stack()
#     # q.push([cur_room])
#     opz = {'n':'s', 'e':'w', 's':'n', 'w':'e'}
#     while q.size() > 0:
#         path = q.dequeue()
#         # path = q.pop()
#         v = path[-1]
#         #breakpoint()
#         if len(path) < len(my_graph):
#             l = []
#             for k, v in my_graph.items():
#                 for direction in v:
#                     if not v[direction]:
#                         direction = opz[direction]
#                     if v[direction]:
#                         new_path = list(path)
#                         new_path.append(int(v[direction])) 
#                         traversal_path.append(direction)
#                         #breakpoint()
#                         q.enqueue(new_path)
                    
#         return traversal_path

##################################
def get_path(cur_room):
    q = Queue()
    q.enqueue([cur_room])
    visited = {}
    opz = {'n':'s', 'e':'w', 's':'n', 'w':'e'} # go back
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if len(path) < len(room_graph):
            for door in player.current_room.get_exits():
                if not int(player.current_room.get_room_in_direction(door).name[5:]) and v in visited:
                    door = opz[door]
                    traversal_path.append(door)
                elif int(player.current_room.get_room_in_direction(door).name[5:]) != v:
                    traversal_path.append(door)
                    #visited[v] = path
                    new_path = list(path)
                    new_path.append(int(player.current_room.get_room_in_direction(door).name[5:]))
                    q.enqueue(new_path)
                # else:
                #     del traversal_path[-1]
                #     door = opz[door]
                #     new_path = list(path)
                #     traversal_path.append(door)
                #     new_path.append(int(player.current_room.get_room_in_direction(door).name[5:]))
                #     q.enqueue(new_path)
                
    return traversal_path
###################################   
traversal_path= get_path(player.current_room.id)
print(traversal_path)

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

print(len(traversal_path))

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
