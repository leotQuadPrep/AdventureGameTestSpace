import GlobalContanor


class Level:
    def __init__(self, description, directions=None, occupants=None, level_north=None, level_northeast=None,
                 level_east=None, level_southeast=None, level_south=None, level_southwest=None, level_west=None,
                 level_northwest=None, level_up=None, level_down=None, action=None, doors=None):
        self.description = description
        if directions is None:
            directions = []
        self.directions = directions
        if occupants is None:
            occupants = []
        self.occupants = occupants
        self.level_north = level_north
        self.level_northeast = level_northeast
        self.level_east = level_east
        self.level_southeast = level_southeast
        self.level_south = level_south
        self.level_southwest = level_southwest
        self.level_west = level_west
        self.level_northwest = level_northwest
        self.level_up = level_up
        self.level_down = level_down
        self.action = action
        if doors is None:
            doors = []
            doors.insert(1, GlobalContanor.Compare_Door1)
            doors.insert(2, GlobalContanor.Compare_Door1)
            doors.insert(3, GlobalContanor.Compare_Door1)
            doors.insert(4, GlobalContanor.Compare_Door1)
            doors.insert(5, GlobalContanor.Compare_Door1)
            doors.insert(6, GlobalContanor.Compare_Door1)
            doors.insert(7, GlobalContanor.Compare_Door1)
            doors.insert(8, GlobalContanor.Compare_Door1)
            doors.insert(9, GlobalContanor.Compare_Door1)
            doors.insert(10, GlobalContanor.Compare_Door1)
        self.doors = doors

    def set_north(self, north):
        self.level_north = north

    def set_northeast(self, northeast):
        self.level_northeast = northeast

    def set_east(self, east):
        self.level_east = east

    def set_southeast(self, southeast):
        self.level_southeast = southeast

    def set_south(self, south):
        self.level_south = south

    def set_southwest(self, southwest):
        self.level_southwest = southwest

    def set_west(self, west):
        self.level_west = west

    def set_northwest(self, northwest):
        self.level_northwest = northwest

    def set_up(self, up):
        self.level_up = up

    def set_down(self, down):
        self.level_down = down

    def visited(self):
        # global GlobalContanor.gameTime
        # global GlobalContanor.level_show_text
        # global GlobalContanor.action_show_text
        # global GlobalContanor.location
        # global GlobalContanor.player_input
        # global GlobalContanor.player_inputted
        # global GlobalContanor.location_changed
        if GlobalContanor.gameTime == 24:
            GlobalContanor.action_show_text = "It is noon. The sun is at it's highest."
        elif GlobalContanor.gameTime == 48:
            GlobalContanor.action_show_text = "It is sunset. The sun and moon are both on the horizon."
        elif GlobalContanor.gameTime == 72:
            GlobalContanor.action_show_text = "It is midnight. The moon is at it's highest."
        elif GlobalContanor.gameTime == 0:
            GlobalContanor.action_show_text = "It is sunrise. The sun and moon are both on the horizon."
        i = 0
        j = 0
        directions = []
        if self.directions[0] != "":
            directions.insert(1, self.directions[0])
        if self.directions[1] != "":
            directions.insert(2, self.directions[1])
        if self.directions[2] != "":
            directions.insert(3, self.directions[2])
        if self.directions[3] != "":
            directions.insert(4, self.directions[3])
        if self.directions[4] != "":
            directions.insert(5, self.directions[4])
        if self.directions[5] != "":
            directions.insert(6, self.directions[5])
        if self.directions[6] != "":
            directions.insert(7, self.directions[6])
        if self.directions[7] != "":
            directions.insert(8, self.directions[7])
        if self.directions[8] != "":
            directions.insert(9, self.directions[8])
        if self.directions[9] != "":
            directions.insert(10, self.directions[9])
        GlobalContanor.level_show_text = (f"{self.description}. You can go " + "")
        if len(directions) > 2:
            for x in directions:
                if i < len(directions) - 2:
                    i = i + 1
                    GlobalContanor.level_show_text += x + ", "
                elif i < len(directions) - 1:
                    i = i + 1
                    GlobalContanor.level_show_text += x + ", and "
                elif i == len(directions) - 1:
                    GlobalContanor.level_show_text += x
        elif len(directions) == 2:
            for z in directions:
                if i == 0:
                    GlobalContanor.level_show_text += z + " or "
                    i = i + 1
                elif i == 1:
                    GlobalContanor.level_show_text += z + ""
        elif len(directions) == 1:
            for y in directions:
                GlobalContanor.level_show_text += y
        if len(self.occupants) > 0:
            GlobalContanor.level_show_text += ". You see" + ""
            if len(self.occupants) > 2:
                for x in self.occupants:
                    if j < len(self.occupants) - 2:
                        j = j + 1
                        GlobalContanor.level_show_text += " a " + x.name + ","
                    elif j < len(self.occupants) - 1:
                        j = j + 1
                        GlobalContanor.level_show_text += " a " + x.name + ", and"
                    else:
                        GlobalContanor.level_show_text += " a " + x.name + ""
            elif len(self.occupants) == 2:
                for z in self.occupants:
                    if j == 0:
                        GlobalContanor.level_show_text += " a " + z.name + " and "
                        j = j + 1
                    elif j == 1:
                        GlobalContanor.level_show_text += "a " + z.name + ""
            elif len(self.occupants) == 1:
                for y in self.occupants:
                    GlobalContanor.level_show_text += " a " + y.name + ""

        for p in range(len(self.doors)):
            self.doors[p].describe()
        GlobalContanor.level_show_text += ". What do you want to do?"
        self.action = GlobalContanor.player_input
        if GlobalContanor.player_inputted:
            action2 = self.action.lower()
            for ele in action2:
                if ele not in GlobalContanor.input_char:
                    action2 = action2.replace(ele, "")
            action2 = action2.split(" ")
            direction_index = 0
            global item_index
            item_index = 0
            global k_index
            k_index = 0
            l_index = 0
            global item_check_index
            item_check_index = 0
            GlobalContanor.remove_article(action2)
            action3 = []
            i_index = 0
            taken_item = False
            for i in action2:
                action3.insert(i_index, i)
                i_index = i_index + 1
            GlobalContanor.remove_action(action3)
            k_index = 0
            global n_index
            n_index = 0
            item_index = -1
            item_check_index = 0
            for o in action2:
                if o == "open":
                    for m in self.directions:
                        for k in action2:
                            if k == m:
                                if type(self.doors[direction_index]) is type(GlobalContanor.Compare_Door1):
                                    self.doors[direction_index].open()
                                    GlobalContanor.location = self
                                    GlobalContanor.location_changed = True
                                    action2 = ""
                        direction_index = direction_index + 1
            for o in action2:
                if o == "close":
                    for m in self.directions:
                        for k in action2:
                            if k == m:
                                if type(self.doors[direction_index]) is type(GlobalContanor.Compare_Door1):
                                    self.doors[direction_index].close()
                                    GlobalContanor.location = self
                                    GlobalContanor.location_changed = True
                                    action2 = ""
                        direction_index = direction_index + 1
            for o in action2:
                if o == "lock":
                    for m in self.directions:
                        for k in action2:
                            if k == m:
                                if type(self.doors[direction_index]) is type(GlobalContanor.Compare_Door1):
                                    self.doors[direction_index].lock()
                                    GlobalContanor.location = self
                                    GlobalContanor.location_changed = True
                                    action2 = ""
                        direction_index = direction_index + 1
            for o in action2:
                if o == "unlock":
                    for m in self.directions:
                        for k in action2:
                            if k == m:
                                if type(self.doors[direction_index]) is type(GlobalContanor.Compare_Door1):
                                    self.doors[direction_index].unlock()
                                    GlobalContanor.location = self
                                    GlobalContanor.location_changed = True
                                    action2 = ""
                        direction_index = direction_index + 1
            for o in action2:
                if o == "bar":
                    for m in self.directions:
                        for k in action2:
                            if k == m:
                                if type(self.doors[direction_index]) is type(GlobalContanor.Compare_Door1):
                                    self.doors[direction_index].bar()
                                    GlobalContanor.location = self
                                    GlobalContanor.location_changed = True
                                    action2 = ""
                        direction_index = direction_index + 1
            for o in action2:
                if o == "unbar":
                    for m in self.directions:
                        for k in action2:
                            if k == m:
                                if type(self.doors[direction_index]) is type(GlobalContanor.Compare_Door1):
                                    self.doors[direction_index].unbar()
                                    GlobalContanor.location = self
                                    GlobalContanor.location_changed = True
                                    action2 = ""
                        direction_index = direction_index + 1

            for n in action2:
                if n in self.directions:
                    if n == "north":
                        if type(self.doors[0]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[0].open_close:
                                GlobalContanor.action_show_text = f"You go north."
                                GlobalContanor.location = self.level_north
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[0].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go north."
                            GlobalContanor.location = self.level_north
                            GlobalContanor.location_changed = True
                    elif n == "northeast":
                        if type(self.doors[1]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[1].open_close:
                                GlobalContanor.action_show_text = f"You go northeast."
                                GlobalContanor.location = self.level_northeast
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[1].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go northeast."
                            GlobalContanor.location = self.level_northeast
                            GlobalContanor.location_changed = True
                    elif n == "east":
                        if type(self.doors[2]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[2].open_close:
                                GlobalContanor.action_show_text = f"You go east."
                                GlobalContanor.location = self.level_east
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[2].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go east."
                            GlobalContanor.location = self.level_east
                            GlobalContanor.location_changed = True
                    elif n == "southeast":
                        if type(self.doors[3]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[3].open_close:
                                GlobalContanor.action_show_text = f"You go southeast."
                                GlobalContanor.location = self.level_southeast
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[3].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go southeast."
                            GlobalContanor.location = self.level_southeast
                            GlobalContanor.location_changed = True
                    elif n == "south":
                        if type(self.doors[4]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[4].open_close:
                                GlobalContanor.action_show_text = f"You go south."
                                GlobalContanor.location = self.level_south
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[4].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go south."
                            GlobalContanor.location = self.level_south
                            GlobalContanor.location_changed = True
                    elif n == "southwest":
                        if type(self.doors[5]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[5].open_close:
                                GlobalContanor.action_show_text = f"You go southwest."
                                GlobalContanor.location = self.level_southwest
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[5].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go southwest."
                            GlobalContanor.location = self.level_southwest
                            GlobalContanor.location_changed = True
                    elif n == "west":
                        if type(self.doors[6]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[6].open_close:
                                GlobalContanor.action_show_text = f"You go west."
                                GlobalContanor.location = self.level_west
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[6].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go west."
                            GlobalContanor.location = self.level_west
                            GlobalContanor.location_changed = True
                    elif n == "northwest":
                        if type(self.doors[7]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[7].open_close:
                                GlobalContanor.action_show_text = f"You go northwest."
                                GlobalContanor.location = self.level_northwest
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[7].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go northwest."
                            GlobalContanor.location = self.level_northwest
                            GlobalContanor.location_changed = True
                    elif n == "up":
                        if type(self.doors[8]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[8].open_close:
                                GlobalContanor.action_show_text = f"You go up."
                                GlobalContanor.location = self.level_up
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[8].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go up."
                            GlobalContanor.location = self.level_up
                            GlobalContanor.location_changed = True
                    elif n == "down":
                        if type(self.doors[9]) is type(GlobalContanor.Compare_Door1):
                            if self.doors[9].open_close:
                                GlobalContanor.action_show_text = f"You go down."
                                GlobalContanor.location = self.level_down
                                GlobalContanor.location_changed = True
                            else:
                                GlobalContanor.action_show_text = f"The {self.doors[9].name} is in your way."
                                GlobalContanor.location = self
                                GlobalContanor.location_changed = True
                        else:
                            GlobalContanor.action_show_text = f"You go down."
                            GlobalContanor.location = self.level_down
                            GlobalContanor.location_changed = True
            if not GlobalContanor.location_changed:
                GlobalContanor.action_show_text = "You cannot do that."
        GlobalContanor.player_inputted = False
