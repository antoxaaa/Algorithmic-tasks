reader = open('linear_search_H.txt', 'r')
seq = [int(n) for n in reader.readline().split()]
reader.close()


def multiply_numbers(seq):

    if len(seq) <= 3:
        print(*seq)
    else:
        highest = max(seq[0], seq[1])
        lowest =  min(seq[0], seq[1])
        
        highest_product_of_2 = seq[0] * seq[1]
        lowest_product_of_2  = seq[0] * seq[1]

        highest_product_of_three = seq[0] * seq[1] * seq[2]

        for current in seq[2:]:

            element = current

            highest_product_of_three = max(
                highest_product_of_three, 
                current * highest_product_of_2, 
                current * lowest_product_of_2)

            highest_product_of_2 = max(
                highest_product_of_2, 
                current * highest, 
                current * lowest)

            lowest_product_of_2 = min(
                lowest_product_of_2,
                current * highest,
                current * lowest)

            highest = max(highest, current)
            lowest = min(lowest, current)

multiply_numbers(seq)