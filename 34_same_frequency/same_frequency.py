def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    sorted_lst1 = sorted(list(str(num1)))
    sorted_lst2 = sorted(list(str(num2)))

    if sorted_lst1 == sorted_lst2:
        return True
    return False

    