"""
      s1
      N
   NW | NE
     \|/
s4 W--o--E s2
     /|\
   SW | SE
      S
     s3
"""

def choose_action(s1, s2, s3, s4, t):
#Process input
    free_dirs = []      #list of free directions
    if (s1 > t):       #check for danger NORTH
        free_dirs.append('N')       #add NORTH to free directions

    if (s3 > t):       #check for danger SOUTH
        free_dirs.append('S')       #add SOUTH to free directions

    if (s2 > t):       #check for danger EAST
        free_dirs.append('E')       #add EAST to free directions

    if (s4 > t):       #check for danger WEST
        free_dirs.append('W')       #add WEST to free directions

#Compute control
    if len(free_dirs) == 0:     #no free directions
        return "Trapped"

    elif len(free_dirs) == 1:   #1 free direction
        return free_dirs[0]     #continue that way

    elif len(free_dirs) == 2:   #2 free directions
        #opposite directions
        if ('N' in free_dirs and 'S' in free_dirs) or ('E' in free_dirs and 'W' in free_dirs):
            return free_dirs[0]+' or '+free_dirs[1]     #correct order due to processing order
        #adjacent directions
        else:
            return free_dirs[0]+free_dirs[1]            #correct order due to processing order

    elif len(free_dirs) == 3:   #3 free directions --> choose middle
        if ('N' in free_dirs and 'S' in free_dirs): #-->middle is E or W
            free_dirs.remove('N')   #remove non-middle directions
            free_dirs.remove('S')
        elif ('E' in free_dirs and 'W' in free_dirs): #-->middle is N or S
            free_dirs.remove('E')   #remove non-middle directions
            free_dirs.remove('W')

        return free_dirs[0]     #return 3rd direction

    else:                           #all directions are free
        return 'Continue'
