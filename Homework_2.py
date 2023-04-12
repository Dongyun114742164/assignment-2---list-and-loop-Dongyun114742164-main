# Name: Dongyun Lee
# SBUID: 114742164

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Extract statistical information from a list -----------------
# TODO: Complete the implementation of listStatistic() and listStd().

def listStatistic(list_in):
    max = list_in[0]
    min = list_in[0]
    average = 0
    for i in range(len(list_in)):
        if list_in[i] > max:
            max = list_in[i]
        if list_in[i] < min:
            min = list_in[i]
    for i in range(len(list_in)):
        average += list_in[i]

    return max, min, average / len(list_in)

def listStd(list_in):
    v = 0
    for i in (list_in):
        v += (i - listStatistic(list_in)[2])**2
    o = (v / (len(list_in) - i))**(1/2)

    return o


# ---------------------------- Exercise II --------------------------------------
# -----------------         Implement the Lunh Algorithm        -----------------
# TODO: Complete the implementation of reverseList(), doubleOddIndex()
# digitSum(), replaceDoubleDigit(), isCardValid() and lunhAlgorithm()

def reverseList(list_in):
    k = []

    for i in range(len(list_in)):
        k.append(list_in(len(list_in)-i-1))
    return k

def doubleOddIndex(list_in):
    list_in[1::2] = [2*x for x in list_in[1::2]]

    for i in range(len(list_in)):
        if i % 2 == 1:
            list_in[i] *= 2

    return list_in

def digitSum(value):
    str_value = str(value)

    if len(str_value) == 1:
        return int(str_value)
    else:
        digit_sum = 0
        for digit in str_value:
            digit_sum += int(digit)

        if digit_sum >= 10:
            return digitSum(digit_sum)
        else:
            return False


def replaceDoubleDigit(list_in):
    for i in range(len(list_in)):
        if list_in[i] >= 10:
            list_in[i] = digitSum(list_in[i])
    return list_in

def isCardValid(list_in):
    for i in range(len(list_in)-2, -1, -2):
        list_in[i] = list_in[i] * 2
        # If the result is greater than 9, subtract 9
        if list_in[i] > 9:
            list_in[i] = list_in[i] - 9

    # Calculate the sum of all digits
    total_sum = sum(list_in)

    # If the sum is divisible by 10, the card is valid
    if total_sum % 10 == 0:
        return True
    else:
        return False
    
def lunhAlgorithm(card_nb):
    reversed_card_nb = card_nb[::-1]
    
    for i in range(1, len(reversed_card_nb), 2):
        reversed_card_nb[i] *= 2
    
    for i in range(len(reversed_card_nb)):
        if reversed_card_nb[i] > 9:
            reversed_card_nb[i] = sum(map(int, str(reversed_card_nb[i])))
    
    return sum(reversed_card_nb) % 10 == 0


# ---------------------------- MAIN FCT ---------------------------------
def main():

    #Exercise 1 main
    my_list = [1, 2, 3, 4, 5, 6]
    list_max, list_min, list_average = listStatistic(my_list)
    print("The max of the list is: ", list_max)
    print("The min of the list is: ", list_min)
    print("The average of the list is: ", list_average)
    list_std = listStd(my_list)
    print("The std of the list is: ", list_std)

    #Exercise 2 main
    card_number = [4,0,0,0,0,0,1,2,3,4,5,6,7,8,9,9]

    ''' Step-by-step tests (you can remove these  tests when you
    are done with the final function lunhAlgorithm )
    '''
    print("Here is the original card number: ", card_number)
    reversed_card_nb = reverseList(card_number)
    print("Here is the reversed card number: ", reversed_card_nb)
    lunh_product = doubleOddIndex(reversed_card_nb)
    print("One in two element is multipled by 2: ", lunh_product)
    print("Sum the digit in a number: ", digitSum(18))
    single_digit_prod = replaceDoubleDigit(lunh_product)
    print("Replace the double digits in the vector: ", single_digit_prod)
    validity = isCardValid(single_digit_prod)
    print("Is the card valid??", validity)

    # execute the final code
    print("Is the card valid??", lunhAlgorithm(card_number))

# Run the main code
main()
