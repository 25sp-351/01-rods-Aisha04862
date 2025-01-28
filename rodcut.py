#to run this program enter in terminal "python3 rodcut.py <length of rod>"
import sys
def rod_cutting(my_rod_length, pieces):
    cutting_list = []
    the_total_value = 0
    the_remaining_length = my_rod_length

#use the sort method to sort the pieces in descending order
    pieces.sort(key=lambda x: x[1] / x[0], reverse=True)
#use for loop to determine what happens if remainng length of rod is greater than or equal to 0
    for length, value in pieces:
        if the_remaining_length <= 0:
            break
        number_of_cuts = the_remaining_length // length
        if number_of_cuts > 0:
            the_total_value += number_of_cuts * value
            cutting_list.append((number_of_cuts, length, number_of_cuts * value))
            the_remaining_length -= number_of_cuts * length

    return cutting_list, the_remaining_length, the_total_value

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("./rodcut <rod_length>")
        sys.exit(1)
        
#use a try-except block to handle errors
    try:
        rod_length = int(sys.argv[1])
    except ValueError:
        print("The rod length has to be an integer in order for the program  to work.")
        sys.exit(1)

    pieces = []

    try:
        while True:
            line = input().strip()  
            if not line: 
                break
            length, value = map(int, line.split(","))
            pieces.append((length, value))
#use control d to end input
    except EOFError:
        pass

    cutting_list, the_remaining_length, the_total_value = rod_cutting(rod_length, pieces)

    for num, size, total in cutting_list:
        print(f"{num} @ {size} = {total}")
    print(f"Remainder: {the_remaining_length}")
    print(f"Total Value: {the_total_value}")