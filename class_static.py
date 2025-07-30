#class_method : 1

class employee:
    company_name="TCS"

    @classmethod
    def change_comapany(cls,new_name):
        cls.company_name=new_name

employee.change_comapany("Wipro")
print(employee.company_name)

# class_method : 2

class indians:
    state_name="Tamilnadu"

    @classmethod
    def change_state(cls,new_state):
        cls.state_name=new_state

indians.change_state("Andra Pradesh")
print(indians.state_name)