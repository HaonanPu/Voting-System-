# COMP 202 A3
# Name: Haonan Pu
# Student ID:   260846401

from a3_helpers import *
import doctest
import random

def count_plurality(ballots):
    '''
    (list) -> dict
    This function takes a list of plurality ballots and returns a dictionary
    of how many votes each candidate got

    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}

    >>> count_plurality(['LIBERAL', 'LIBERAL','GREEN', 'GREEN', 'NDP'])
    {'LIBERAL': 2, 'GREEN': 2, 'NDP': 1}

    '''
    #Create a new empty dictionary to store key and values
    new_dict = {}
    
    for element in ballots:
    #Iterate through all elements in the given list, if it hasn't existed in
    #the new dictionary, add one occurence of that. Otherwise, plus 1 to the
    #existed occurence number
        
        if (element in new_dict):
            new_dict[element] += 1
        else:
            new_dict[element] = 1
            
    return new_dict
    
def count_approval(ballots):
    '''
    (list) -> dict
    This function takes a list of approval ballots and returns a dictionary
    of how many votes each candidate got

    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}

    >>> count_approval([['GREEN'], ['NDP', 'GREEN'], ['LIBERAL', 'BLOC', 'GREEN']])
    {'GREEN': 3, 'NDP': 1, 'LIBERAL': 1, 'BLOC': 1}
    '''
    
    new_list = flatten_lists(ballots)
    #Use the helper functions to combine all nested lists in one single list
    new_dict = {}
    #Create an empty dictionary to store values

    for element in new_list:
        if (element in new_dict):
            new_dict[element] += 1
        else:
            new_dict[element] = 1

    return new_dict

def count_rated(ballots):
    '''
    (list) -> dict
    The function takes a list of ballots and return a dictionary of how many points
    each candidate got

    >>> count_rated([{'LIBERAL': 5, 'NDP': 2}, {'NDP': 4, 'GREEN': 5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}

    >>> count_rated([{'BLOC': 4, 'GREEN': 3}, {'NDP': 5, 'LIBERAL': 1}])
    {'BLOC': 4, 'GREEN': 3, 'NDP': 5, 'LIBERAL': 1}

    >>> count_rated([{'LIBERAL': 5, 'GREEN': 4, 'NDP': 2}, {'GREEN': 4, 'BLOC': 2}, {'LIBERAL': 3, 'NDP': 2, 'BLOC': 1}])
    {'LIBERAL': 8, 'GREEN': 8, 'NDP': 4, 'BLOC': 3}
    '''

    
    #Create a new empty dictionary, use add_dict from a3_helper to add all the values together 
    new_dict = {}
    for element in range(0, len(ballots)):
        new_dict = add_dicts(new_dict, ballots[element])
    return new_dict


def count_first_choices(ballots):
    '''
     (list) -> dict
    This function takes a list of ranked ballots and returns a dictionary storing,
    for every party represented in all the ballots, how many ballots for which that
    party was the first choice

    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']])
    {'NDP': 2, 'LIBERAL': 0, 'GREEN': 1, 'BLOC': 0}

    >>> count_first_choices([])
    {}

    >>> count_first_choices([['NDP', 'CPC'], ['GREEN', 'LIBERAL'], ['CPC', 'BLOC']])
    {'NDP': 1, 'CPC': 1, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    
    '''


    
    #temp = []

    #Make a new empty dictionary
    count = {}

    #Iterate each element in the ballots given, then check each subelement. 
    for i in range(len(ballots)):
        for j in range(len(ballots[i])):
            if j == 0:
                #Here, if it is already in the count, then add up one to its value
                if ballots[i][j] in count.keys():
                    count[ballots[i][j]] += 1
                else:
                    #Otherwise, set it to 1.
                    count[ballots[i][j]] = 1
            else:
                #After the first round, check if the next one is in the count,
                #If no, then reset it to zero since it is not the first choice
                if ballots[i][j] in count.keys():
                    pass
                else:
                    count[ballots[i][j]] = 0
                    
    return count
    

 









    
    

if __name__ == '__main__':
    doctest.testmod()
