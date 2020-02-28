class CoffeeMachine:
    def __init__(self, water, milk, beans, disposable_cups, money):
        self.supply_water = water
        self.supply_milk = milk
        self.supply_beans = beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.active = True

    def choosing_action(self):
        while self.active:
            user_choice = input('Write action (buy, fill, take, remaining, exit): ')
            if user_choice == 'buy':
                self.buy_coffee()
            if user_choice == 'fill':
                self.fill()
            if user_choice == 'take':
                self.take()
            if user_choice == 'remaining':
                self.actual_supplies()
            if user_choice == 'exit':
                self.active = False

    def buy_coffee(self):
        user_choice = input('What do you want to buy? 1 - espresso,'
                            ' 2 - latte, 3 - cappuccino, back - to main menu: ')
        if user_choice == 'back':
            self.choosing_action()
        elif 0 < int(user_choice) < 4:
            coffee = CoffeeType()
            if user_choice == '1':
                coffee.espresso()
            if user_choice == '2':
                coffee.latte()
            if user_choice == '3':
                coffee.cappuccino()
            if coffee.check_supply(coffee_machine):
                self.supply_water -= coffee.water_needed
                self.supply_milk -= coffee.milk_needed
                self.supply_beans -= coffee.beans_needed
                self.disposable_cups -= 1
                self.money += coffee.cost

    def fill(self):
        self.supply_water += int(input('Write how many ml of water do you want to add: '))
        self.supply_milk += int(input('Write how many ml of milk do you want to add: '))
        self.supply_beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.disposable_cups += int(input('Write how many disposable cups do you want to add: '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def actual_supplies(self):
        print(f"""The coffee machine has:
{self.supply_water} of water
{self.supply_milk} of milk
{self.supply_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money""")


class CoffeeType:
    water_needed, milk_needed, beans_needed, cost = 0, 0, 0, 0

    # espresso: 250 water, 16 coffee beans, 4$
    def espresso(self):
        self.water_needed = 250
        self.beans_needed = 16
        self.cost = 4

    # latte: 350 water, 75 milk, 20 beans, 7$
    def latte(self):
        self.water_needed = 350
        self.milk_needed = 75
        self.beans_needed = 20
        self.cost = 7

    # cappuccino: 200 water, 100 milk, 12 beans, 6$
    def cappuccino(self):
        self.water_needed = 200
        self.milk_needed = 100
        self.beans_needed = 12
        self.cost = 6

    def check_supply(self, supplies: CoffeeMachine):
        if self.water_needed > supplies.supply_water:
            print('Sorry, not enough water!')
        elif self.milk_needed > supplies.supply_milk:
            print('Sorry, not enough milk!')
        elif self.beans_needed > supplies.supply_beans:
            print('Sorry, not enough coffee beans!')
        elif not supplies.disposable_cups:
            print('Sorry, not enough disposable cups!')
        else:
            print('I have enough resources, making you a coffee!')
            return True
        return False


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.choosing_action()
