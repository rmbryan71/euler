def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise Exception('expected integer, got %s' % type(input))
    if not 0 < input < 400000:
        raise Exception('Argument must be between 1 and 399999')
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


def roman_to_int(input):
    if not isinstance(input, type("")):
        raise Exception('expected string, got %s" % type(input)')
    input = input.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise Exception('input is not a valid Roman numeral: %s' % input)
    return sum


with open('p089_roman.txt', 'r') as f:
    saved_chars = 0
    lines = f.read().splitlines()
    for i in lines:
        orig = len(i)
        shorter = len(int_to_roman(roman_to_int(i)))
        saved_chars+=(orig-shorter)
print(saved_chars)
