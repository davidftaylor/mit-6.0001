# Problem Set 4A
# Name: David Taylor

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    
    # get all permutations of length n-1
    perms = get_permutations(sequence[1:])
    char = sequence[0]
    result = [] # a list of all permutations of the sequence
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

if __name__ == '__main__':
#    #EXAMPLE
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))

