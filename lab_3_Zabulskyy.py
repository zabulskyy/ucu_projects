class Property:
    """
    contains number of bathrooms, bedrooms and square_feet
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        """
        declare and assign properties
        :param square_feet: str, size of apartment/house
        :param beds: str, number of bedrooms
        :param baths: str, number of bathrooms
        :param kwargs: additional parameters
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        print all properties
        :return: None
        """
        print("\n================")
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        get arguments from input
        :return: dict with inputted strings
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    change all input to valid format
    input response till it is valid
    :param input_string: text, which will be asked to user
    :param valid_options: tuple, with which we will compare input
    :return:
    """
    input_string += " ({}) ".format((", ".join(valid_options)))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    """
    extends Property
    info about Apartment
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium") 

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        contains info about balconies and laundries
        :param balcony: str
        :param laundry: str
        :param kwargs: additional info
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        output all info
        :return: None
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        """
        get properties and update info
        :return: dict
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
                "What laundry facilities does "
                "the property have? ",
                Apartment.valid_laundries)
        balcony = get_valid_input(
                "Does the property have a balcony?",
                Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    extends Property
    info about House
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        contains info about garage and fenced
        :param num_stories: str (int)
        :param garage: str
        :param fenced: str
        :param kwargs: additional info
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        output all info
        :return: None
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        get info
        :return: dict
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase(Property):
    """
    info about price and taxes
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        contains info about price and taxes
        :param price: str
        :param taxes: str
        :param kwargs: additional info
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        output info
        :return: None
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        input info
        :return: dict
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    info about house if it is furnished or/and has utilities
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        contains info if house is furnished or/and has utilities
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: additional info
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        output info
        :return: None
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        input info
        :return: dict
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    asks all stuff about house
    """
    def prompt_init():
        """
        updates info about house rental
        :return: dict
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    asks all stuff about apartment
    """
    def prompt_init():
        """
        updates info about apartment rental
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    add an purchasing info to Apartment
    """
    def prompt_init():
        """
        add an purchasing info to Apartment
        :return: dict
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    add an purchasing info to House
    """
    def prompt_init():
        """
        add an purchasing info to House
        :return: dict
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    holds a list of all properties, display those properties, and allows to create new ones
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }

    def __init__(self):
        """
        list of properties
        """
        self.property_list = []

    def display_properties(self, num=False):
        """
        display all properties
        """
        if num:
            for property in self.property_list[num]:
                property.display()
        else:
            for property in self.property_list:
                for sub_property in property:
                    sub_property.display()

    def add_property(self):
        """
        add a new property
        """
        property_type = get_valid_input(
                "What type of property? ",
                ("house", "apartment")).lower()
        payment_type = get_valid_input(
                "What payment type? ",
                ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append([PropertyClass(**init_args)])

    def delete_property(self):
        """
        remove property from list
        """
        really = input("are you sure? (type yes or no): ")
        while really not in ["yes", "no"]:
            really = input("expression is invalid, please type yes or no: ")
        really = ["no", "yes"].index(really)
        if not really:
            return

        which = int(input("set the number of option you would like to delete: "))
        while which not in range(1, len(self.property_list) + 1):
            which = int(input("this number is invalid, please set another: "))
        self.display_properties()

        sure = input("\nis it the property you want to delete? (type yes or no): ")
        while sure not in ["yes", "no"]:
            sure = input("expression is invalid, please type yes or no: ")
        sure = ["no", "yes"].index(sure)

        if sure:
            self.property_list.remove(self.property_list[which - 1])
        else:
            self.delete_property()

    def create_ad(self):
        """
        create flashing ad with property
        """
        from time import sleep
        from os import system
        if len(self.property_list) == 0:
            print('there no properties to show')
            return
        which = int(input("set the number of option you would like to show: "))
        while which not in range(1, len(self.property_list) + 1):
            which = int(input("this number is invalid, please set another: "))
        try:
            print("press ctrl+C to stop")
            sleep(1)
            while True:
                sleep(0.5)
                system('cls')
                sleep(0.2)
                print("!!!BEST OFFER!!!")
                self.display_properties()
        except KeyboardInterrupt:
            system('cls')


def welcome():
    """
    interface, reading commands, contains all functions
    """
    option = input("please, set the option (without brackets):\n"
                   "<add> to add a property\n"
                   "<display> to display all your properties\n"
                   "<delete> to delete some of your properties\n"
                   "<ad> to show an ad of one of your properties\n")
    option = option.replace('<', '').replace('>', '').lower()
    while option not in ['add', 'display', 'delete', 'ad']:
        option = input('wrong command\n')
    if option == 'add':
        user.add_property()
        print('\n--changes saved--\n')
    elif option == 'display':
        user.display_properties()
    elif option == 'delete':
        user.delete_property()
        print('\n--changes saved--\n')
    elif option == 'ad':
        user.create_ad()
    else:
        print('something wrong, bye\n')
        return


user = Agent()
while True:
    from os import system
    welcome()
    print('\n-----------------\n')
