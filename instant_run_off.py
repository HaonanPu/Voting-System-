# COMP 202 A3
# Name: Haonan Pu
# ID: 260846401

from single_winner import *
import doctest
from a3_helpers import *
import copy

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    (list) -> int
    This function takes a list and an integer of winners as inputs and return
    the number of votes a candidate would need to win using the Droop Quota\

    >>> votes_needed_to_win([{'CPC': 3, 'NDP': 5}, {'NDP': 2, 'CPC': 4}, {'CPC': 3, 'NDP': 5}], 1)
    2

    >>> votes_needed_to_win(['g']*20, 2)
    7
    
    '''
    #I use integer division so that the result won't be a float, the formula is already given in the assignment description
    return len(ballots)//(num_winners+1)+1


def has_votes_needed(result, votes_needed):
    '''
    (dict, int) -> bool
    This function takes a dictionary and an integer as input and return a boolean representing whether the
    candidate with the most votes in this election has at least votes_need votes

    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True

    >>> has_votes_needed({'LIBERAL': 5, 'CPC': 1}, 6)
    False

    >>> has_votes_needed({'BLOC': 3, 'GREEN': 3}, 2)
    True

    >>> has_votes_needed({'LIBERAL': 7, 'CPC': 7}, 8)
    False

    '''

    '''
    for key, value in result.items():
        for num in range(value):
            if num >= votes_needed:
                return True
            else:
                return False
    '''
    '''
    new_list = sorted(result.values())
    ##Sort the dictionary in order first in a new created list
    if max(new_list) >= votes_needed:
        #Find the maximum value in the list, then compare it with the votes_needed
        #Now it does not matter if i have tie condition here.
        return True
    else:
        return False
    '''
    for key in result.keys(): #Basically check the value of keys, compare them with the number given.
        if result[key] >= votes_needed:
            return True
    return False

    
    

################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    (list, list) -> list
    This function takes two lists as input na sreturn a new ranked ballots where
    all the candidates in to_eliminate have been removed.
    If all candidates on a ballot have been eliminated, it should become an empty list

    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]

    >>> eliminate_candidate([['GREEN', 'LIBERAL'], ['NDP', 'BLOC']], ['LIBERAL', 'BLOC'])
    [['GREEN'], ['NDP']]

    >>> eliminate_candidate([['GREEN', 'GREEN'], ['NDP', 'NDP']], ['GREEN', 'NDP'])
    [[], []]


    '''
    ballots_copy = deep_copy(ballots)#Make a deep copy here so that I won't worry about modifying it
    result = []
    temp = []

    for i in range(len(ballots_copy)):
        for j in ballots_copy[i]:
            if j in to_eliminate: #check if the element shall be removed, if so, leave it away
                pass
            else:
                temp.append(j) #Otherwise, add it to the temp
        result.append(temp) #Then all of them will be put in the result list
        temp = [] #Refresh its memory here and do the loop again
    return result
    
################################################################################


def count_irv(ballots):
    '''
    (list) -> dict
    This function takes a list of ranked ballots and return a dictionary of how many votes each candidate ends
    with counting with IRV. 

    >>> pr_dict(count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']]))
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}

    >>> random.seed(30)
    >>> pr_dict(count_irv([['a', 'b', 'c'], ['d', 'g', 'e'], ['g', 'f', 'a'], ['f'], ['g', 'c', 'a'], ['c', 'f', 'a', 'g', 'd'], ['f'], ['g'], ['a', 'g', 'b'], ['b', 'a'], ['a','f'], ['f']]))
    {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 6, 'g': 0}

    '''
    # First make a copy of the input, this is the deep copy version, without modifying it.
    ballots_copy = deep_copy(ballots)
    #Make the list flat which will be easier for iterating and checking, set all values to 0.
    return_dict = dict.fromkeys(flatten_lists(ballots_copy), 0)

    #Find the first choice of the each part in the ballot
    first_choices = count_first_choices(ballots_copy)

    #If can't find a winner here, then continue
    while not has_votes_needed(first_choices, votes_needed_to_win(ballots_copy, 1)):

        # Identify the last candidate, eliminate them,
        # and count again until someone has enough votes
        last_candidate = [last_place(first_choices)]
        ballots_copy = eliminate_candidate(ballots_copy, last_candidate)
        first_choices = count_first_choices(ballots_copy)

        #Break the loop once the loser is found, otherwise it will be an infinite loop
        if len(first_choices) <= 1:
            break
        
    # Update the list with their final values after the loop
    return_dict.update(first_choices)

    return return_dict

    

################################################################################

if __name__ == '__main__':
    doctest.testmod()
