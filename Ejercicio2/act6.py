class Family():
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.members_list = []

    def add_member(self, member):
        self.members_list.append(member)

    def __str__(self):
        return "Family: " + self.name + " Members: " + self.members_list

familia = Family()
familia.name = "Retra"
familia.members = "4"
familia.add_member("Mora")
familia.add_member("Lichi")
familia.add_member("Alejo")
familia.add_member("JP Genaro")
print(familia)


