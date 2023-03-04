# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def palindrome(s):
    l = len(s)
    if s[:l] == s[l::-1]:
        return True
    else:
        return False

def palindrome_2(s):
    l = len(s)
    i = 0
    while (i<len(s)):
        if s[i] != s[-1-i]:
            return False
        else:
            return True


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
