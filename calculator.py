# 1. -------------
# 2. # Question
# 3. # -------------
# 4. # implement a calculator to evaluate a string
# 5. # input: e.g. '17-9*2+1/2' (string) => 17 - 18 + 0 => -1
# 6. # output: -1   (int)
# 7. #
# 8. # requirements:
# 9. # support 4 operators: + , - , * ,  /.  * and / have higher priority than + and -.
# 10. # all the input strings are legit.
# 11. # all the numbers are integers

def calculator(str):
    stack = []
    i = 0
    while i < len(str):
        if str[i].isdigit():
            digit, end_index = find_digit(i, str)
            stack.append(digit)
            i = end_index
        else:
            if str[i] == '*':
                digit, end_index = find_digit(i + 1, str)
                i = end_index
                val = int(stack.pop()) * digit
                stack.append(val)
            elif str[i] == '/':
                digit, end_index = find_digit(i + 1, str)
                i = end_index
                val = int(stack.pop() / digit)
                stack.append(val)
            else:
                stack.append(str[i])
                i += 1

    return eval_stack(stack)


def find_digit(i, strg):
    print("in digit: " + str(i) + '  ' + strg)
    end_idx = i
    while end_idx < len(strg) and strg[end_idx].isdigit():
        end_idx += 1

    return int(strg[i:end_idx]), end_idx


def eval_stack(stack):
    print(stack)
    return None