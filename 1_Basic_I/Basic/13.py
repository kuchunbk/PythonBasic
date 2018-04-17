def print_string(input_string):
    return input_string

if __name__ == "__main__":
    input_string = """

                a string that you "don't" have to escape

                This

                is a  ....... multi-line

                heredoc string --------> example

                """
    print(print_string(input_string))