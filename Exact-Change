def exact_change(user_amount):
    dollars = user_amount // 100
    user_amount = user_amount % 100
    quarters = user_amount // 25
    user_amount = user_amount % 25
    dimes = user_amount // 10
    user_amount = user_amount % 10
    nickels = user_amount // 5
    user_amount = user_amount % 5
    pennies = user_amount
    return dollars, quarters, dimes, nickels, pennies

def test():
    user_input = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_input)
    if user_input <= 0:
        print('no change')
    else:
        # DOLLARS
        if num_dollars > 1:
            print('%d dollars' % num_dollars)
        elif num_dollars == 1:
            print('%d dollar' % num_dollars)
        # QUARTERS
        if num_quarters > 1:
            print('%d quarters' % num_quarters)
        elif num_quarters == 1:
            print('%d quarter' % num_quarters)
        # DIMES
        if num_dimes > 1:
            print('%d dimes' % num_dimes)
        elif num_dimes == 1:
            print('%d dime' % num_dimes)
        # NICKELS
        if num_nickels > 1:
            print('%d nickels' % num_nickels)
        elif num_nickels == 1:
            print('%d nickel' % num_nickels)
        # PENNIES
        if num_pennies > 1:
            print('%d pennies' % num_pennies)
        elif num_pennies == 1:
            print('%d penny' % num_pennies)


if __name__ == '__main__':
    test()
