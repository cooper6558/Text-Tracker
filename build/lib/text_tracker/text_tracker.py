def track(original_file, spoken_file):
    """
    Main function of the text-tracker package.
    :param original_file: file containing original text, with pages separated
    by lines, opened in 'r' mode
    :param spoken_file: file containing spoken text, with pages separated by
    lines, opened in 'r' mode
    :return: list of optimal indeces aligning the words in the spoken file to
    those in the original file
    """
    # get data
    original, spoken, nan_indeces = get_data(original_file, spoken_file)
    out = []
    for page, o in enumerate(original):
        # get an array of possible indeces for each word
        index_array = generate_match_indeces(
            generate_index_list(o, spoken[page]))

        # get a corresponding array of step values
        step_array = [generate_match_steps(row) for row in index_array]

        # find minimum sum of steps and return corresponding index vector
        sums = [sum([abs(x) for x in row]) for row in step_array]
        out.append(index_array[sums.index(min(sums))])

    for row_number, row in enumerate(out):
        for nan_index in nan_indeces[row_number]:
            row.insert(nan_index, float('NaN'))

    return out


def get_data(original_file, spoken_file):
    """
    Loads data given files.
    :param original_file: file with the written text, opened in 'r' mode
    :param spoken_file: file with the spoken_text text, opened in 'r' mode
    :return: original_text and spoken_text lists; lists of lists of words
    """
    # define original_text list
    original_text = [line.lower().split() for line in original_file]

    # define spoken_text list
    spoken_text = [line.lower().split() for line in spoken_file]

    # for each line, if a spoken_text word doesn't exist, ignore it
    # and add to nan_indeces, a returned value
    nan_indeces = []
    for row_number, word_array in enumerate(spoken_text):
        nan_row = []
        for index, word in enumerate(word_array):
            if word not in original_text[row_number]:
                word_array.pop(index)
                nan_row.append(index)
        nan_indeces.append(nan_row)

    return original_text, spoken_text, nan_indeces


# example match_indeces: [0, 1, 2, 1, 3, 4]
# example return value: [0, 0, -2, 2, 0]
def generate_match_steps(match_indeces):
    """
    Create step vector
    :param match_indeces: list of possible indeces
    :return: list of step sizes
    """
    return [b - match_indeces[a] - 1 for a, b in enumerate(match_indeces[1:])]


# example spoken string: "One day a bird bird met hippo."
# example actual string: "One day a bird met a hippo."
# example index_list: [[0], [1], [2,5], [3], [3], [4], [6]]
# example return value: [[0, 1, 2, 3, 3, 4, 6], [0, 1, 5, 3, 3, 4, 6]
def generate_match_indeces(index_list):  # "The Permutator"
    """
    The hard part: generating every possible list of indeces
    :param index_list: list of lists of possible indeces
    :return: array of possible index lists
    """
    # permutations will be the size of the return value (number of rows)
    permutations = 1
    for element in index_list:
        permutations *= len(element)

    out = []
    for col in range(permutations):
        row = []
        # n starts at the number of permutations for each new row...
        n = permutations
        for index in index_list:
            # ...and is divided by the number of indeces possible for each word
            n //= len(index)
            # move to next item in index every n columns
            row.append(index[col // n % len(index)])
        out.append(row)

    return out


# example spoken_string_list: ['one','day','a','bird','bird','met','hippo']
# example original_string_list: ['one','day','a','bird','met','a','hippo']
# example return value: [[0], [1], [2,5], [3], [3], [4], [6]]
def generate_index_list(original_string_list, spoken_string_list):
    """
    The output of this goes to generate_match_indeces to be "permutated"
    :param original_string_list: list of words
    :param spoken_string_list: list of words
    :return: index list
    """
    return [[index for index, value in enumerate(original_string_list)
             if value == word]
            for word in spoken_string_list]

