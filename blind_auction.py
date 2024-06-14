logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

name = input('what is your name:?')
bid = int(input('whats your bid?: $'))
other_bidders = input("are there any other bidders? Type 'yes' or 'no'\n")

dictionary = []

def bidder(first_name, amount, answer):
    dictionary.append({first_name:amount})
    process = True
    while process:
        if answer == 'yes':
            name = input('what is your name?')
            bid = int(input('whats your bid ?'))
            dictionary.append({name:bid})
            other_bidders = input("are there any other bidders? Type 'yes' or 'no'")
            if other_bidders == 'no':
                max_value = [max(d.values()) for d in dictionary]
                max_index = max_value.index(max(max_value))
                for x, y in dictionary[max_index].items():
                    print(f"The winner is {x} with a bid of ${y}")
                process = False
        elif answer == 'no':
            max_value = [max(d.values()) for d in dictionary]
            max_index = max_value.index(max(max_value))
            for x, y in dictionary[max_index].items():
                print(f"The winner is {x} with a bid of ${y}")
            process = False
bidder(name,bid,other_bidders)
print(dictionary)
