my_file=input()
opponent_file=input()
edge_name_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
edge_name = ["a", "b", "c", "d", "e", "f", "g", "h"]
table_dict1 = {}
board = open(my_file)
opponent = open(opponent_file)
best_moves=[]
movement=[]
for line in opponent:
    if "," in line:
        line_list = line.split(",")
        line_list = line_list[0].split()
    else:
        line_list = line.split()
    start_point = line_list[0]
    end_point = line_list[1]
    movement.append((start_point, end_point))
for j in edge_name:
    for i in range(1, 9):
        k = str(i)
        coordinate = j + k
        table_dict1[coordinate] = "--"
table_list = []
for y in range(1, 9):
    table_list.append([y])
for g in range(len(table_list)):
    for a in range(8):
        table_list[g].append("--")
for line in board:
    new_line = line.strip()
    if " " in new_line:
        line_list = new_line.split()
        coord = line_list[1]
        material = line_list[0]
        table_dict1[coord] = material
        letter, num = coord[0], coord[1]
        ind = edge_name_dict.get(letter)
        for each in table_list:
            if each[0] == int(num):
                each[ind] = material
    else:
        mine=line[0].upper()
for h in reversed(table_list):
    for f in h:
        print(f, end=" ")
    print()
def moves(location, pieces,table_dict,my_color=mine):
    if pieces[1] == "K":
        available_loc_k = []
        point = int(location[1])
        e_n = location[0]
        edge_name_index = edge_name.index(e_n)
        mov1 = [-1, 0, 1]
        mov2 = [0, 1]
        mov3 = [-1, 0]
        def av_po(list1, list2):
            for i in list1:
                new_point = str(point + i)
                for j in list2:
                    new_edge = edge_name[edge_name_index + j]
                    new_coordinate = new_edge + new_point
                    if table_dict.get(new_coordinate) == "--":
                        available_loc_k.append(new_coordinate)
                    elif table_dict.get(new_coordinate)[0] == "W" and pieces[0] == "B":
                        available_loc_k.append(new_coordinate)
                    elif table_dict.get(new_coordinate)[0] == "B" and pieces[0] == "W":
                        available_loc_k.append(new_coordinate)

        if 8 > point > 1 and 8 > edge_name_dict.get(e_n) > 1:
            av_po(mov1, mov1)
        elif point == 1 and 8 > edge_name_dict.get(e_n) > 1:
            av_po(mov2, mov1)
        elif point == 8 and 8 > edge_name_dict.get(e_n) > 1:
            av_po(mov3, mov1)
        elif 8 > point > 1 and edge_name_dict.get(e_n) == 1:
            av_po(mov1, mov2)
        elif 8 > point > 1 and edge_name_dict.get(e_n) == 8:
            av_po(mov1, mov3)
        else:
            if point == 1:
                if edge_name_dict.get(e_n) == 8:
                    av_po(mov2, mov3)
                elif edge_name_dict.get(e_n) == 1:
                    av_po(mov2, mov2)
            else:
                if edge_name_dict.get(e_n) == 8:
                    av_po(mov3, mov3)
                elif edge_name_dict.get(e_n) == 1:
                    av_po(mov3, mov2)
        return available_loc_k
    elif pieces[1] == "B":
        available_loca_b = []
        e_n_i = edge_name_dict[location[0]]
        e_p = int(location[1])
        my_p = pieces[0]
        for i in range(8):
            if e_n_i + i < 8 and e_p + i + 1 < 9:
                new_e = edge_name[e_n_i + i]
                new_location = new_e + str(e_p + i + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loca_b.append(new_location)
                elif control[0] != my_p:
                    available_loca_b.append(new_location)
                    break
                else:
                    break
        for j in range(8):
            if e_n_i + j < 8 and e_p - j - 1 > 0:
                new_e = edge_name[e_n_i + j]
                new_location = new_e + str(e_p - j - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loca_b.append(new_location)
                elif control[0] != my_p:
                    available_loca_b.append(new_location)
                    break
                else:
                    break
        for c in range(8):
            if e_n_i - c - 2 >= 0 and e_p - c - 1 > 0:
                new_e = edge_name[e_n_i - c - 2]
                new_location = new_e + str(e_p - c - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loca_b.append(new_location)
                elif control[0] != my_p:
                    available_loca_b.append(new_location)
                    break
                else:
                    break
        for k in range(8):
            if e_n_i - k - 2 >= 0 and e_p + k + 1 < 9:
                new_e = edge_name[e_n_i - k - 2]
                new_location = new_e + str(e_p + k + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loca_b.append(new_location)
                elif control[0] != my_p:
                    available_loca_b.append(new_location)
                    break
                else:
                    break
        return available_loca_b
    elif pieces[1] == "R":
        available_loc_r = []
        e_n = location[0]
        e_n_i = edge_name_dict[location[0]]
        e_p = int(location[1])
        my_p = pieces[0]
        for i in range(1, 9):
            if e_p + i < 9:
                new_location = e_n + str(e_p + i)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_r.append(new_location)
                elif control[0] != my_p:
                    available_loc_r.append(new_location)
                    break
                else:
                    break
        for j in range(1, 9):
            if e_p - j > 0:
                new_location = e_n + str(e_p - j)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_r.append(new_location)
                elif control[0] != my_p:
                    available_loc_r.append(new_location)
                    break
                else:
                    break
        for k in range(1, 9):
            new_index = e_n_i - k - 1
            if new_index >= 0:
                new_name = edge_name[new_index]
                new_location = new_name + str(e_p)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_r.append(new_location)
                elif control[0] != my_p:
                    available_loc_r.append(new_location)
                    break
                else:
                    break
        for h in range(1, 9):
            new_index = e_n_i + h - 1
            if new_index < 8:
                new_name = edge_name[new_index]
                new_location = new_name + str(e_p)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_r.append(new_location)
                elif control[0] != my_p:
                    available_loc_r.append(new_location)
                    break
                else:
                    break
        return available_loc_r
    elif pieces[1] == "Q":
        available_loc_q = []
        e_n = location[0]
        e_n_i = edge_name_dict[location[0]]
        e_p = int(location[1])
        my_p = pieces[0]
        for i in range(1, 9):
            if e_p + i < 9:
                new_location = e_n + str(e_p + i)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for j in range(1, 9):
            if e_p - j > 0:
                new_location = e_n + str(e_p - j)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for k in range(1, 9):
            new_index = e_n_i - k - 1
            if new_index >= 0:
                new_name = edge_name[new_index]
                new_location = new_name + str(e_p)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for h in range(1, 9):
            new_index = e_n_i + h - 1
            if new_index < 8:
                new_name = edge_name[new_index]
                new_location = new_name + str(e_p)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for i in range(8):
            if e_n_i + i < 8 and e_p + i + 1 < 9:
                new_e = edge_name[e_n_i + i]
                new_location = new_e + str(e_p + i + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for j in range(8):
            if e_n_i + j < 8 and e_p - j - 1 > 0:
                new_e = edge_name[e_n_i + j]
                new_location = new_e + str(e_p - j - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for c in range(8):
            if e_n_i - c - 2 >= 0 and e_p - c - 1 > 0:
                new_e = edge_name[e_n_i - c - 2]
                new_location = new_e + str(e_p - c - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        for k in range(8):
            if e_n_i - k - 2 >= 0 and e_p + k + 1 < 9:
                new_e = edge_name[e_n_i - k - 2]
                new_location = new_e + str(e_p + k + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_q.append(new_location)
                elif control[0] != my_p:
                    available_loc_q.append(new_location)
                    break
                else:
                    break
        return available_loc_q
    elif pieces[1] == "P":
        available_loc_p = []
        e_n = location[0]
        e_n_i = edge_name_dict[location[0]]
        e_p = int(location[1])
        my_p=pieces[0]
        if my_p==my_color:
            if e_p == 2:
                new_location = e_n + str(e_p + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_p.append(new_location)
                new_location = e_n + str(e_p + 2)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_p.append(new_location)
            else:
                if e_p<8:
                    new_location = e_n + str(e_p + 1)
                    control = table_dict.get(new_location)
                    if control == "--":
                        available_loc_p.append(new_location)
            left_i = e_n_i - 2
            right_i = e_n_i
            if left_i >= 0 and e_p<8:
                try_left_location = edge_name[left_i] + str(e_p + 1)
                if table_dict.get(try_left_location) != "--":
                    if table_dict.get(try_left_location)[0] != my_p:
                        available_loc_p.append(try_left_location)
            if right_i<8 and e_p<8:
                try_right_location = edge_name[right_i] + str(e_p + 1)
                if table_dict.get(try_right_location) != "--":
                    if table_dict.get(try_right_location)[0] != my_p:
                        available_loc_p.append(try_right_location)
        else:
            if e_p == 7 and e_p>1:
                new_location = e_n + str(e_p - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_p.append(new_location)
                new_location = e_n + str(e_p - 2)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_p.append(new_location)
            else:
                if e_p>1 and e_p>1:
                    new_location = e_n + str(e_p - 1)
                    control = table_dict.get(new_location)
                    if control == "--":
                        available_loc_p.append(new_location)
            left_i = e_n_i - 2
            right_i = e_n_i
            if not left_i < 0 and e_p>1:
                try_left_location = edge_name[left_i] + str(e_p - 1)
                if table_dict.get(try_left_location) != "--":
                    if table_dict.get(try_left_location)[0] != my_p:
                        available_loc_p.append(try_left_location)
            if right_i != 8 and e_p>1:
                try_right_location = edge_name[right_i] + str(e_p - 1)
                if table_dict.get(try_right_location) != "--":
                    if table_dict.get(try_right_location)[0] != my_p:
                        available_loc_p.append(try_right_location)
        return available_loc_p
    elif pieces[1] == "N":
        available_loc_n = []
        e_n = location[0]
        e_n_i = edge_name_dict[location[0]]
        e_p = int(location[1])
        my_p = pieces[0]
        if e_p + 1 < 9:
            if not e_n_i + 1 > 7:
                new_location = edge_name[e_n_i + 1] + str(e_p + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
            if e_n_i - 3 >= 0:
                new_location = edge_name[e_n_i - 3] + str(e_p + 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
        if e_p + 2 < 9:
            if not e_n_i > 7:
                new_location = edge_name[e_n_i] + str(e_p + 2)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
            if e_n_i - 2 >= 0:
                new_location = edge_name[e_n_i - 2] + str(e_p + 2)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
        if e_p - 2 > 0:
            if not e_n_i > 7:
                new_location = edge_name[e_n_i] + str(e_p - 2)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
            if e_n_i - 2 >= 0:
                new_location = edge_name[e_n_i - 2] + str(e_p - 2)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
        if e_p - 1 > 0:
            if not e_n_i + 1 > 7:
                new_location = edge_name[e_n_i + 1] + str(e_p - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
            if e_n_i - 3 >= 0:
                new_location = edge_name[e_n_i - 3] + str(e_p - 1)
                control = table_dict.get(new_location)
                if control == "--":
                    available_loc_n.append(new_location)
                elif control[0] != my_p:
                    available_loc_n.append(new_location)
        return available_loc_n
def play(start_point, end_point, table_dictionary):
    extra_dictionary=table_dictionary.copy()
    pieces_name = extra_dictionary.get(start_point)
    extra_dictionary[start_point] = "--"
    extra_dictionary[end_point] = pieces_name
    return extra_dictionary
def rival_king_search(dictionary):
    for location, piece in dictionary.items():
        if piece[0] != mine and piece[1] == "K":
            return location
def check_control(dictionary):
    rival_king_location=rival_king_search(dictionary)
    for location,piece in dictionary.items():
        if piece[0] == mine:
            available_points=moves(location,piece,dictionary)
            if rival_king_location in available_points:
                return True
    return False
def rival_movement_control(start,move_list,dictionary):
    for i in move_list:
        tried_dict = play(start, i , dictionary)
        value = check_control(tried_dict)
        if not value:
            return False
    return True
def checkmate(dictionary):
    for position,piece in dictionary.items():
        if piece[0] !=mine and piece!= "--":
            available_list=moves(position,piece,dictionary)
            continue_or_finished=rival_movement_control(position,available_list,dictionary)
            if continue_or_finished:
                continue
            else:
                return False
    return True
def my_piece_list_control(movements,initial,dictionary):
    check_list=[]
    for j in movements:
        played_dict = play(initial, j , dictionary)
        check_or_not = check_control(played_dict)
        if check_or_not:
            check_list.append(j)
    return check_list
def my_king_search(dictionary):
    for location,pieces in dictionary.items():
        if pieces[0]==mine and pieces[1]=="K":
            return location
def check_control_my(dictionary):
    my_king=my_king_search(dictionary)
    for location,piece in dictionary.items():
        if piece[0] != mine and piece != "--":
            available_points=moves(location,piece,dictionary)
            if my_king in available_points:
                return True
    return False
def opponent_movement_control(initial,end,dictionary):
    opponent_name=dictionary.get(initial)
    if opponent_name[0]==mine:
        return False
    opponent_move=moves(initial,opponent_name,dictionary)
    if opponent_move==None:
        return False
    if end in opponent_move:
        return True
    else:
        return False
def opponent_play(tuple,extra_dict,previous_move):
    initial_location, end_location= tuple[0] , tuple[1]
    continue_or_stop=opponent_movement_control(initial_location,end_location,extra_dict)
    if continue_or_stop:
        changed_dict=play(initial_location,end_location,extra_dict)
        check_search=check_control(changed_dict)
        if not check_search:
            best_moves.append(previous_move)
            return changed_dict
        else:
            return False
    else:
        return False
try_list=[]
print(movement)
def recursion_extra_play(dict,can_be_best=[],i=0):
    global try_list
    if len(movement)+1==len(can_be_best):
        try_list.append(can_be_best)
        return
    elif len(can_be_best)==len(movement):
        is_this_okay=True
        for location, pieces in dict.items():
            if pieces[0] == mine:
                last_available = moves(location, pieces, dict)
                for step in last_available:
                    my_movement = (location, step)
                    last_played = play(location, step, dict)
                    mate = checkmate(last_played)
                    if mate:
                        is_this_okay=False
                        new_list = can_be_best.copy()
                        can_be_best += [my_movement]
                        recursion_extra_play(last_played,can_be_best,i)
                        can_be_best = new_list
        if is_this_okay:
            can_be_best += ["Don't"]
            recursion_extra_play(dict,can_be_best,i)
    else:
        rival_initial, rival_end=movement[i][0],movement[i][1]
        is_it_okay = True
        for position, piece in dict.items():
            if piece[0] == mine:
                my_available = moves(position, piece, dict)
                for end_po in my_available:
                    my_move = (position, end_po)
                    played_dict = play(position, end_po, dict)
                    op_can = opponent_movement_control(rival_initial, rival_end, played_dict)
                    my_check = check_control_my(played_dict)
                    if op_can and not my_check:
                        is_it_okay = False
                        op_played = play(rival_initial, rival_end, played_dict)
                        new_list= can_be_best.copy()
                        can_be_best += [my_move]
                        i += 1
                        recursion_extra_play(op_played,can_be_best,i)
                        i -=1
                        can_be_best=new_list
        if is_it_okay:
            can_be_best += ["Don't"]
            i += 1
            recursion_extra_play(dict,can_be_best,i)
            i -= 1
recursion_extra_play(table_dict1)
without_dont=[]
one_more_list=[]
for i in try_list:
    if "Don't" in i:
        continue
    else:
        without_dont.append(i)
if len(without_dont)>1:
    extra_lst=[]
    for lst in without_dont:
        each=lst[0]
        start,end=each[0],each[1]
        played_dict=play(start,end,table_dict1)
        check=check_control(played_dict)
        if check:
            rival_initial,rival_end=movement[0][0],movement[0][1]
            rival_played=play(rival_initial,rival_end,played_dict)
            check1=check_control(rival_played)
            if not check1:
                print(lst)
                extra_lst += lst
    print(extra_lst)

else:
    print(without_dont)
"""ex_board5.txt
ex_opponent5.txt
"""