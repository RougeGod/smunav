import re

floorSet = {"SB1", "SB2", "SB3", "SB4", "ME0", "ME1", "ME2", "MS1", "MS2", "MS3", "MS4",
            "MN0", "MN1", "MN2", "MN3", "MN4", "MN5", "MM0", "MM1", "MM2", "MM3", "MS0"
            "SC1", "SC2", "SC3", "SC4", "SC5", "AT1", "AT2", "AT3", "B1", "B2", "B3", 
            "LI0", "LI1", "LI2", "LI3", "LA1", "LA2", "LR1", "LR2", "LB1", "VR1", "RR1", "R-1"}
floorConnectionMap = {}

floorConnectionMap["AT1"] = ("LI1", "MN0", "SC1", "B1", "AT2", "AT3")
floorConnectionMap["AT2"] = ("AT1", "B2", "SC2", "AT3")
floorConnectionMap["AT3"] = ("SC3", "AT2", "AT1")

floorConnectionMap["B1"] =  ("AT1", "B2")
floorConnectionMap["B2"] = ("B1", "B3", "AT2")
floorConnectionMap["B3"] = ("B2",)

floorConnectionMap["SC1"] = ("AT1", "SC2", "SC3", "SC4", "SC5")
floorConnectionMap["SC2"] = ("AT2", "SC1", "SC3", "SC4", "SC5")
floorConnectionMap["SC3"] = ("AT3", "SC1", "SC2", "SC4", "SC5", "MN3")
floorConnectionMap["SC4"] = ("SC1", "SC3", "SC2", "SC5")
floorConnectionMap["SC5"] = ("SC1", "SC3", "SC2", "SC4")

floorConnectionMap["SB4"] = ("SB1", "SB2", "SB3")
floorConnectionMap["SB3"] = ("SB1", "SB2", "SB4")
floorConnectionMap["SB2"] = ("SB1", "SB3", "SB4", "LA2")
floorConnectionMap["SB1"] = ("SB2", "SB3", "SB4", "LA1")

floorConnectionMap["LA1"] = ("SB1", "LA2", "LR1", "LB1")
floorConnectionMap["LA2"] = ("SB2", "LA1", "MS1", "LR2")
floorConnectionMap["LR2"] = ("LA2", "LR1")
floorConnectionMap["LR1"] = ("LA1", "LB1", "LR2")
floorConnectionMap["LB1"] = ("VR1", "LR1")
floorConnectionMap["VR1"] = ("RR1", "R-1", "LB1")
floorConnectionMap["RR1"] = ("VR1",)
floorConnectionMap["R-1"] = ("VR1",)

floorConnectionMap["LI0"] = ("LI1", "LI2", "LI3")
floorConnectionMap["LI1"] = ("AT1", "LI0", "LI2", "LI3")
floorConnectionMap["LI2"] = ("LI1", "LI0", "LI3")
floorConnectionMap["LI3"] = ("LI1", "LI2", "LI0")

floorConnectionMap["MN0"] = ("MN1", "MM0", "MN2", "MN3", "MN4", "MN5", "AT1")
floorConnectionMap["MN1"] = ("MN0", "MN2", "MN3", "MN4", "MN5")
floorConnectionMap["MN2"] = ("MN0", "MN1", "MN3", "MN4", "MN5", "MM1")
floorConnectionMap["MN3"] = ("MN0", "MN2", "MN1", "MN4", "MN5", "MM2", "SC3")
floorConnectionMap["MN4"] = ("MN0", "MN2", "MN3", "MN1", "MN5", "MM2")
floorConnectionMap["MN5"] = ("MN0", "MN2", "MN3", "MN4", "MN1")

floorConnectionMap["MM0"] = ("ME1", "MM1", "MM2", "MM3", "MN0", "MS0")
floorConnectionMap["MM1"] = ("MM0", "MM2", "MM3", "MS1", "MN2", "ME2")
floorConnectionMap["MM2"] = ("MM0", "MM1", "MM3", "MN3", "MN4", "MS2")
floorConnectionMap["MM3"] = ("MM0", "MM1", "MM2", "MN5", "MS3", "MS4")

floorConnectionMap["MS0"] = ("MS1", "MS2", "MS3", "MS4", "MM0")
floorConnectionMap["MS1"] = ("MS0", "MS2", "MS3", "MS4", "MM1", "LA2")
floorConnectionMap["MS2"] = ("MS0", "MS1", "MS3", "MS4", "MM2")
floorConnectionMap["MS3"] = ("MS0", "MS2", "MS1", "MS4", "MM3")
floorConnectionMap["MS4"] = ("MS0", "MS2", "MS1", "MS3", "MM3")

floorConnectionMap["ME0"] = ("ME1",)
floorConnectionMap["ME1"] = ("MM0", "ME0")
floorConnectionMap["ME2"] = ("MM1",)
floorConnectionMap[None] = () #none is a valid key to a map? 


def roomToFloor(roomNum):
    room = roomNum[0:3].upper()
    if (room in floorSet):
        return room
    elif (room[0:2] in floorSet):
        return room[0:2]      
    else:
        print("Room codes are one or two letters followed by three numbers, like \"B131\" or \"SC507\"")
        print("It's also possible that the building/floor/room combination is not in the system.")
        return None

