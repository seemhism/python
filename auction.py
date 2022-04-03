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

from replit import clear
from art import logo
print(logo)


data = {}
bidding_finish = False


def high(record):
  highest = 0
  winner= ""
  for bidder in record:
    amount= record[bidder]
    if amount>highest:
      highest = amount
      winner= bidder
  print(f"the highest bid is {highest} from {bidder}!!!")


while not bidding_finish:
  name=input("what is you name?\n")
  bid=float(input("what is your bid?\n$"))
  data[name] = bid
  cont = input("type continue = yes or else no?\n")
  if cont == 'no':
    bidding_finish = True
    high(data)
  elif cont == 'yes':
    clear()

