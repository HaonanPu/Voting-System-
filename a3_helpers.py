# COMP 202 A3 Part 1
# Name: Haonan Pu
# Student ID:   260846401

import doctest
import random



def flatten_lists(nested):
    '''
    (list) -> list
    This function gets a list which can contain list and replace any lists inside
    Finally return the new version of the list.

    >>> flatten_lists([[0],[1, 2], 3])
    [0, 1, 2, 3]

    >>> flatten_lists([1, 2, 3, 4])
    [1, 2, 3, 4]

    >>> flatten_lists([[0, 1, 2], [3]])
    [0, 1, 2, 3]
    
    '''
    empty_list = []
    if len(nested) > 0: ##Check if the list contains any element inside
        element = nested[0] ##Assign the first element to an empty list created
        if type(element) == list: #Check if it is a list,
                                  #If so, use recursive to re-run this nested-list
                            
            empty_list = flatten_lists(element)
        else:   #Here is for two differet: 1. One of elements is not list
                #                          2. The element of the nested list is not list
            empty_list.append(element)
        
        # If the first element is not a list,
        # returns a list containing the first element and then test the rest of
        # element with recursion. (That' why I have [1:] here)
        empty_list += flatten_lists(nested[1:])
    
    return empty_list
    
    

def flatten_dict(d):
    '''
    (dict) -> list
    This function gets a dictionary as input and returns a list which has keys
    repeated v times where v is the value associated with the key in the dictionary

    >>> flatten_dict({'LIBERAL' : 5, 'NDP': 2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']

    >>> flatten_dict({'Green' : 3, 'Conservative' : 4})
    ['Green', 'Green', 'Green', 'Conservative', 'Conservative', 'Conservative', 'Conservative']
    '''
    empty_list = []
    for key, value in d.items(): #I added .item() since if I took it away, the
                                 #program will give an error: too many values to unpack
        empty_list += [key]*value

    return empty_list
    

def add_dicts(d1, d2):
    '''
    (dict, dict) -> dict
    This function takes two dictionaries as input and merges them by adding values
    if the key exsists in both two, then returns them in one new dictionary

    >>> add_dicts({'a':5, 'b':2, 'd':-1}, {'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}

    >>> add_dicts({'a':5, 'b':2, 'd':-1, 'f': 7}, {'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'f': 7, 'c': 5}

    >>> add_dicts({'a':5, 'b':2, 'd':-1}, {'a':5, 'b':2, 'd':-1})
    {'a': 10, 'b': 4, 'd': -2}
    


    '''

    '''
    new_dict = deep_copy(d1) #Create a copy of d1 so that I don't have to worry about
                         #modifying d1 later.
                        
    
    for key, val in d2.items(): #Iterate the element in d2 first
        if key in d1:           #Check if d1 and d2 have common keys
            new_dict[key] += val #If so, then add them together and put it back to the original position
        else:
            new_dict[key] = val #Otherwise, just set it to the d1

    return new_dict
    '''
    
    
    temp = {}   #Create a new empty dictionary to store data
    for key in d1.keys(): #Iterate each key in d1
        if key in d2:
            temp[key] = d1[key] + d2[key] #If key in d1 and d2 are the same, then add the value of these two
        else:
            temp[key] = d1[key] #Otherwise, add itself to the new empty dictionary

    for key in d2.keys():
        if not(key in d1): #Check key, value in d2, if the key in d2 doesn't exist in d1, then add it to the temp dictionary
            temp[key] = d2[key]

    return temp
    



def get_all_candidates(ballots):
    '''
    (list) -> list
    This function gets a list as an input and returnd all unique strings in
    this list and its nested contents

    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}, ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']

    >>> get_all_candidates(['NDP', 'GREEN', 'LIBERAL'])
    ['NDP', 'GREEN', 'LIBERAL']


    '''

    new_list = []

    '''
    for i in ballots:                                                     ||               This part works with my own doctest, however, I realized a huge bug hidden inside
        if type(i) == list:
            new_list += flatten_lists(i)                                  ||
        elif type(i) == dict:
            new_list += list(flatten_dict(i))                             ||               On this line, right here, I assume the value of dictionary taken is int. But what
        else:                                                                              if it is other than int, like a string or folat or something else? then it fails.
            new_list += [i]                                               ||               I was excited to use those former helper functions to help finish this one, but
                                                                                           actually I underestimated this one. Da*n

    return list(dict.fromkeys(new_list))
    '''
    for element in ballots:
        if type(element) == list:
            for i in element:
                if type(i) == str:
                    new_list += [i]
                else:
                    pass
        elif type(element) == dict:
            new_list += list(element.keys())
        elif type(element) == str:
            new_list += [element]

    return list(dict.fromkeys(new_list))


###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''
    (dict, funct) -> str
    This function takes result as dictionary and check each value of keys.
    If the function is max, return the winner, otherwise return the loser.
    If there are ties, use random seed to distinguish it.

    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4}
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    '''
    keys = [] #Create an empty list to store keys

    if len(result) <= 0:
        return False
    
    if func == max:
        max_value = max(result.values()) #Find the maximum values in the given dictionary

        
        
        for key, value in result.items():
        #Iterate through the dictionary, if the value is the maximum value I just obtained, add it
        #to the new empty list
            if value == max_value:
                keys.append(key)
        #Finally, use it as the random seed to determine the winner if there are ties
        return random.choice(keys)

    elif func == min:
    #Similarly, find the minimum vakues in the given dictionary
    
        min_value = min(result.values())
        #keys = [] #Create an empty list to store keys
        
        for key, value in result.items():
        #Same as above, check the dictionary, find the min values, add them to the new list
            if value == min_value:
                keys.append(key)
        #After all, use it as the random seed to determine the final loser.
        return random.choice(keys)
        

def get_winner(result):
    '''
    (dict) -> str
     This function takes a dictionary as input and return the key with the greatest value.
     If there are ties, break them randomly.

     >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
     'NDP'
    
    '''
    '''
    max_value = max(result.values())
    keys = []

    for key, value in result.items():
        if value == max_value:
            keys.append(key)

    return random.choice(keys)
    '''
    '''
    votes = result.values()
    winner_votes = max(votes)
    candidates = []

    for candidate in result:
        if result[candidate] == winner_votes:
            candidates.append(candidate)
    return random.choice(candidates)
    '''
    return get_candidate_by_place(result,max)


def last_place(result, seed = None):
    '''
    (dict) -> str
    This function takes a dictionary as input and return the key with the lowest value.
    If there are ties, break them randomly.

    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'BLOC'

    '''
    '''
    min_value = min(result.values())
    keys = []

    for key, value in result.items():
        if value == min_value:
            keys.append(key)

    return random.choice(keys)
    '''
    '''
    votes = result.values()
    if len(votes) == 0:
        pass
    else:
        loser_votes = min(votes)

    candidates = []

    for candidate in result:
        if result[candidate] == loser_votes:
            candidates.append(candidate)

    return random.choice(candidates)
    '''
    return get_candidate_by_place(result, min)


def deep_copy(given_list): #I make a helper fucntion for further use, since we cannot use deepcopy in the assignment
                           #All the source codes here are from class.
    new_list = []

    for element in given_list:
        new_element = []
        for sub_element in element:
            new_element.append(sub_element)
        new_list.append(new_element)

    return new_list
    
###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
