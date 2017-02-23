from building import Building

class Classroom:
    def __init__(self, number, capacity, equipment):
        """
        :param number: str
        :param capacity: int
        :param equipment: list<str>
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom_2):
        """
        :param classroom_2: object
        :return: bool
        """
        return self.capacity > classroom_2.capacity

    def equipment_differences(self, classroom_2):
        """
        :param classroom_2: object
        :return: bool
        """
        return list(set(self.equipment).difference(set(classroom_2.equipment)))

    def __str__(self):
        """
        :return: str
        """
        equipment = ''
        for i in self.equipment:
            equipment += i + ', '
        return 'Classroom {0} has a capacity of {1} persons and has the following equipment: {2}'\
            .format(self.number, self.capacity, equipment[:-2] + '.')

    def __repr__(self):
        """
        :return: str
        """
        equipment = ''
        for i in self.equipment:
            equipment += i + ', '
        return 'Classroom(\'{0}\', {1}, [{2}])'.format(self.number, self.capacity, equipment[:-2] + '.')


class AcademicBuilding(Building):
    def __init__(self, address, classrooms):
        """
        :param address: str
        :param classrooms: list<object>
        """
        self.classrooms = classrooms
        super.__init__(address)

    def total_equipment(self):
        """
        :return: list<tuple<str, int>>
        """
        equipment = {}
        for classroom in self.classrooms:
            for item in classroom.equipment:
                if item not in equipment:
                    equipment[item] = 1
                else:
                    equipment[item] += 1
        return [(item, equipment[item]) for item in equipment]

    def __str__(self):
        """
        :return: str
        """
        list = [str(classroom) + '\n' for classroom in self.classrooms]
        string = ''
        for item in list:
            string += item
        return self.address + '\n' + string
