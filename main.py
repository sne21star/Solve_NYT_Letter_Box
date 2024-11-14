import DataExtracter.read_data as rd


def solve(game):
    pass
def get_word_bank(filename):
    return rd.get_word_bank(filename)

def get_data(filename, number_of_sides):
    return rd.get_data_examples(filename, number_of_sides)

def main():
    data_lines = get_data("Data/data.txt",4)
    bank = get_word_bank("Data/unigram_freq.csv")

if __name__=="__main__":
    main()