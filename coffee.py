# Write your code here
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

# Recipe
# water = 200
# milk = 50
# coffee_beans = 15
# cup = 1

# implementation
# print("How many coffee cups do you need?")
# cup = int(input())
# print("For ", str(cup), " cups you will need:")
# print((cup * water), "ml of water")
# print((cup * milk), "ml of milk")
# print((cup * coffee_beans), "g of coffee beans")

# print("How much ml of water do you have?")
# water_ready = int(input())
# print("How much ml of milk do you have?")
# milk_ready = int(input())
# print("How much g of coffee beans do you have?")
# beans_ready = int(input())
# print("How many coffee cups do you need?")
# cups = int(input())
# coffee = min(water_ready // water, milk_ready //
#              milk, beans_ready // coffee_beans)
# cups_ready = coffee - cups

# if coffee == 0:
#     print("No, I can't make you any coffee")
# elif cups == coffee:
#     print("Yes I can make that ammount of coffee")
# elif cups_ready >= 1:
#     print("Yes I can make that ammount of coffee ",
#           "I can even make ", cups_ready, " more")
# elif coffee > 0 and cups > coffee:
#     print("No I can only make you ", coffee, " cups of coffee")

# # suplies
# current_water = 400
# current_milk = 540
# current_beans = 120
# current_cups = 9
# current_money = 550


# def status():
#     print("The coffee machine has:")
#     print(current_water, " ml of water")
#     print(current_milk, " ml of milk")
#     print(current_beans, " g of coffee beans")
#     print(current_cups, " disposable cups")
#     print(current_money, " of money")


# def buy(option):
#     global current_water
#     global current_milk
#     global current_beans
#     global current_cups
#     global current_money

#     if option == "1":
#         if current_water < 250:
#             print("Sorry not enough water")
#             return

#         if current_beans < 16:
#             print("Sorry not enough coffee beans")
#             return

#         if current_cups < 1:
#             print("Sorry not enough cups")

#         print("I have enough resources, making you a coffee!")
#         current_water -= 250
#         current_beans -= 16
#         current_cups -= 1
#         current_money += 4

#     elif option == "2":

#         if current_water < 350:
#             print("Sorry not enough water")
#             return

#         if current_beans < 20:
#             print("Sorry not enough coffee beans")
#             return

#         if current_milk < 75:
#             print("Sorry not enough milk")
#             return

#         if current_cups < 1:
#             print("Sorry not enough cups")

#         print("I have enough resources, making you a coffee!")
#         current_water -= 350
#         current_beans -= 20
#         current_milk -= 75
#         current_cups -= 1
#         current_money += 7

#     elif option == "3":

#         if current_water < 200:
#             print("Sorry not enough water")
#             return

#         if current_beans < 12:
#             print("Sorry not enough coffee beans")
#             return

#         if current_milk < 100:
#             print("Sorry not enough milk")
#             return

#         if current_cups < 1:
#             print("Sorry not enough cups")

#         print("I have enough resources, making you a coffee!")
#         current_water -= 200
#         current_beans -= 12
#         current_milk -= 100
#         current_cups -= 1
#         current_money += 6
#     elif option == "back":
#         return


# def fill():
#     global current_water
#     global current_milk
#     global current_beans
#     global current_cups
#     global current_money
#     print("Write how many ml of water do you want to add:")
#     current_water += int(input())
#     print("Write how many ml of milk do you want to add:")
#     current_milk += int(input())
#     print("Write how many grams of coffee beans do you want to add:")
#     current_beans += int(input())
#     print("Write how many disposable cups of coffee do you want to add:")
#     current_cups += int(input())


# def take():
#     global current_money
#     print("I gave you $", current_money)
#     current_money = 0


# while True:
#     print("Write action (buy, fill, take, remaining, exit)")
#     choice = input()
#     if choice == "buy":
#         # status()
#         print("What would you like: 1 - espresso $4 | 2 - latte $7 | 3 - cappuccino %6| 'back' to go back")
#         coffee_type = input()
#         buy(coffee_type)
#         # status()
#     elif choice == "fill":
#         # status()
#         fill()
#         # status()
#     elif choice == "take":
#         # status()
#         take()
#         # status()
#     elif choice == "remaining":
#         status()
#     elif choice == "exit":
#         break


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "select"

    def __str__(self):
        return f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money"""

    def show_action(self):
        print("Write action (buy, fill, take, remaining, exit)")

    def choose_action(self, action):
        if action == "buy":
            print(
                "What would you like: 1 - espresso $4 | 2 - latte $7 | 3 - cappuccino %6| 'back' to go back")
            self.state = "buy"

        elif action == "fill":
            print("Write how many ml of water do you want to add:")
            self.water += int(input())
            print("Write how many ml of milk do you want to add:")
            self.milk += int(input())
            print("Write how many grams of coffee beans do you want to add:")
            self.beans += int(input())
            print("Write how many disposable cups of coffee do you want to add:")
            self.cups += int(input())

        elif action == "take":
            print("I gave you ${}".format(self.money))
            self.money = 0
            self.state = "select"
            self.handle()

        elif action == "remaining":
            print(self)
            self.state = "select"
            self.handle()

    def choose_coffee(self, type_of_coffee):
        self.state = "select"

        if type_of_coffee == "1":
            if self.water < 250:
                print("Sorry not enough water")
                return

            if self.beans < 16:
                print("Sorry not enough coffee beans")
                return

            if self.cups < 1:
                print("Sorry not enough cups")

            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4

        elif type_of_coffee == "2":

            if self.water < 350:
                print("Sorry not enough water")
                return

            if self.beans < 20:
                print("Sorry not enough coffee beans")
                return

            if self.milk < 75:
                print("Sorry not enough milk")
                return

            if self.cups < 1:
                print("Sorry not enough cups")

            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.beans -= 20
            self.milk -= 75
            self.cups -= 1
            self.money += 7

        elif type_of_coffee == "3":

            if self.water < 200:
                print("Sorry not enough water")
                return

            if self.beans < 12:
                print("Sorry not enough coffee beans")
                return

            if self.milk < 100:
                print("Sorry not enough milk")
                return

            if self.cups < 1:
                print("Sorry not enough cups")

            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.beans -= 12
            self.milk -= 100
            self.cups -= 1
            self.money += 6
        elif type_of_coffee == "back":
            return

        self.handle()

    def handle(self, data=None):
        if self.state == "action":
            self.choose_action(data)
        elif self.state == "buy":
            self.choose_coffee(data)


coffee_machine = CoffeeMachine()
user_input = ""

while user_input != "exit":
    coffee_machine.handle(user_input)
    user_input = input()
