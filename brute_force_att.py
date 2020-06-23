"""
Creator: GracelessGiant

Basic program to attempt to guess the password for an account
"""
import time

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v",
              "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
              "R", "S", "T", "V", "W", "X", "Y", "Z", " ", "!", '"', "#", "$", "%", "&", "'",	"(", ")", "*", "+", ",",
              "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~", "0", "1",
              "2", "3", "4", "5", "6", "7", "8", "9"]


def brute_att(password):
    """
    Goes through the process to attempt to crack the password
    :param password: the entered password
    """
    guess = ""

    if password in characters:      # checks if the password is of length 1
        return 0

    for x in range(15):             # checks all possibility of length 15 or less
        


def main():
    password = input("Enter your password: ")

    start = time.time()
    answer = brute_att(password)
    print(answer)
    overall_time = time.time() - start

    print("Your password "+password+" was cracked in "+str(overall_time)+" seconds.")


if __name__ == '__main__':
    main()
