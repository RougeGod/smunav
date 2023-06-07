'''Step-by-step: 
Check every hallway for the destination room. 

BFS our way from the current or initial hallway to the destination hallway. 
This will produce a list of hallway numbers. 

Human-readable directions arestill a while away while I figure out
 how to figure out which direction each turn is. 

If LA2 is used for through-traffic (as it often is), then the start and stop points are set appropriately by the
higher-up macro (floor-to-floor) navigation function that runs everything. 
This will be handled by a special "through-traffic" function which takes the input floor and
the output floor and either
a) does the normal BFS with start and end points determined by the origin floor
b) has hard-coded or near hard-cided cases because there aren't THAT many options
'''

hrm = {} #hallway rooms map: which rooms are in the hallway with the number (number is key)
hcm = {} #hallway connections map: which hallways does each hallway touch

hrm[1] = ("LA170", "LA269", "LA268", "LA267", "SB2LoyolaEntrance", "LA266", "LA2EL", "LA2WBR", "LA291", "LA2MBR", "LA294", "LA2Skybridge")
hrm[2] = ("LA283", "LA290", "LA2Commons")
hrm[3] = ("LA275", "LA274", "LA276", "LA278", "LA273", "LA271", "LA280", "LA170")
hrm[4] = ("LA277", "LA278", "LA283", "LA282B", "LA282A", "LA280E", "LA280F", "LA280G", "LA280H")
hrm[5] = ("LA2MBR", "LA2WF", "LA2WBR", "LA283")
hrm[6] = ("LA298", "LA297", "LA295", "LA296")
hrm[7] = ("LA2Dietician", "LA2Laundry", "LA210", "LR2EL")
hrm[8] = ("LA281", "LA282", "LA290", "LA2WF", "LA294", "LA267", "LA268", "SB2LoyolaEntrance", "LA266") #"the box"

hcm[1] = {3,4,8}
hcm[2] = {3,4,5,6}
hcm[3] = {1,2}
hcm[4] = {1,2}
hcm[5] = {2,8}
hcm[6] = {2,7}
hcm[7] = {6}
hcm[8] = {5,1}
