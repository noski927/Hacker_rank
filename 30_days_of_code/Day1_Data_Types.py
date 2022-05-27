i = 4
d = 4.0
s = 'HackerRank '

def my_data(integer, flt, string):
    sum_int_result = i + integer
    sum_float_result = d + flt
    string_result = s + string
    return(sum_int_result,
           sum_float_result,
           string_result)
if __name__ == '__main__':
    a = int(input())
    b = float(input())
    c = str(input())
    result = my_data(a, b, c)
    print(result)




# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.