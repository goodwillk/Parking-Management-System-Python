class Parking:
    """Base class which will get inherited by it's child classes"""
    price = 0
    i = 1
    
    def __init__(self, owner_name=0, vehicle_number=0, in_time=0):
        self.owner_name = owner_name
        self.vehicle_number = vehicle_number
        self.in_time = in_time

    @classmethod
    def alot_parking(cls, data_dict, value, prefix):
        for slot, (key,value1) in enumerate(data_dict.items(), start = 1):
            if value1 is None:
                Data.add_slot(slot, value, data_dict)
                print(f"\nPark at slot {slot} of {prefix}-wheeler Parking.")
                break

    def payment(self, hour, minute):
        t_hour = hour * 60
        t_minute = minute
        t_total = t_hour + t_minute
        result = (self.price) * (t_total/60)
        print("So, Your bill will be : {:.2f} Rs" .format(result))
        return result


class FourWheeler(Parking):
    """Perform functions for 4-Wheelers"""
    data_dict_f = {key: None for key in range(1, 301)}               #Total 300 Parking Slots For 4 wheeler
    revenue = 0
    price = 40

    def __init__(self, owner_name=0, vehicle_number=0, in_time=0):
        super().__init__(owner_name, vehicle_number, in_time)

    def __str__(self) -> str:
        return f"Owner Name : {self.owner_name}\nVehicle Number : {self.vehicle_number}\nIn-Time : {self.in_time}"

    @classmethod
    def alot_parking(cls, value):
        super().alot_parking(cls.data_dict_f, value, prefix = 4)

    @classmethod
    def payment(cls, hour, minute): 
        result = super().payment(cls, hour, minute)
        cls.revenue += result
        return result


class TwoWheeler(Parking):
    """Perform functions for 2-Wheelers"""
    data_dict_t = {key: None for key in range(1, 201)}               #Total 200 Parking Slots For 2 wheeler
    revenue = 0
    price = 20

    def __init__(self, owner_name=0, vehicle_number=0, in_time=0):
        super().__init__(owner_name, vehicle_number, in_time) 

    def __str__(self) -> str:
        return f"Owner Name : {self.owner_name}\nVehicle Number : {self.vehicle_number}\nIn-Time : {self.in_time}"

    @classmethod
    def alot_parking(cls, value):
        super().alot_parking(cls.data_dict_t, value, prefix = 2)

    @classmethod
    def payment(cls, hour, minute):
        result = super().payment(cls, hour, minute)
        cls.revenue += result 
        return result


class Revenue:
    """Will calculate the total revenue"""
    @classmethod
    def profit(cls):
        print("Profit from 2 wheeler parkings : {:.2f} Rs" .format(TwoWheeler.revenue))
        print("Profit from 4 wheeler parkings : {:.2f} Rs" .format(FourWheeler.revenue))
        total_profit = TwoWheeler.revenue + FourWheeler.revenue
        print("\nTotal profit from parkings : {:.2f} Rs" .format(total_profit))


class Data:
    """ Will be used to manipulate data in dictionary """
    @classmethod
    def add_slot(cls, slot, obj, data_dict):
        data_dict[slot] = obj

    @classmethod
    def delete_slot(cls, num, data_dict):
        data_dict.update({num:None})
        
    @classmethod
    def print_dict(cls, data_dict):
        for key, value in data_dict.items():
            if value is None:
                continue
            print(f"\nSlot {key} is occupied by  - \n{value}")


class Basic:
    def park(self):
        name = input("\nEnter your name : ")
        number = int(input("Enter your vehicle's number (Four Digits): "))
        time = str(input("Enter your in-time in format (HH:MM) and (meridiam) : "))

        print("\nFor 4-wheeler ticket price for 60 minutes is 40 Rs.")
        print("For 2-wheeler ticket price for 60 minutes is 20 Rs.")
        type_vehicle = input("\nEnter Your vehicle type (i.e., '4' for 4-wheeler or '2' for 2-wheeler) : ")
        if type_vehicle == '4':
            four = FourWheeler(name, number, time)
            FourWheeler.alot_parking(four)

        elif type_vehicle == '2':
            two = TwoWheeler(name, number, time)
            TwoWheeler.alot_parking(two)

        else:
            print("Please, Enter your vehicle type correctly.")
 
    def intime(time):
        for t in time:
            hour_minute, in_meridiam = [t for t in time.split(' ')]
            for i in hour_minute:
                hour, minute = [int(i) for i in hour_minute.split(':')]
        return hour, minute, in_meridiam
    
    def outtime():
        time = input("\nEnter your out-time in format (HH:MM) and (meridiam) : ")
        for t in time:
            hour_minute, out_meridiam= [t for t in time.split(' ')]
            for i in hour_minute :
                hour1, minute1 = [int(i) for i in hour_minute.split(':')]
        return hour1, minute1, out_meridiam
        
    @classmethod
    def checkout(cls):
        type_vehicle = input("\nEnter vehicle type (i.e., '2' or '4'):")
        num = int(input("Enter vehicle's parking slot number for it's checkout :"))
        
        if type_vehicle == '2' :
            time = TwoWheeler.data_dict_t.get(num)
            time = time.in_time
            hour, minute, in_meridiam = Basic.intime(time)
            Data.delete_slot(num, TwoWheeler.data_dict_t)
                    
        elif type_vehicle == '4' :
            time = FourWheeler.data_dict_f.get(num)
            time = time.in_time
            hour, minute, in_meridiam = Basic.intime(time)
            Data.delete_slot(num, FourWheeler.data_dict_f)

        hour1, minute1, out_meridiam = Basic.outtime()
        hour, minute = Basic.meridiam(hour1, hour, minute1, minute, in_meridiam, out_meridiam)
        
        if type_vehicle == '4' :
            FourWheeler.payment(hour, minute)
        elif type_vehicle == '2' :
            TwoWheeler.payment(hour, minute)

    def track(self):
        print("\nIn Two-Wheeler : ")
        Data.print_dict(TwoWheeler.data_dict_t)
        print("\nIn Four-Wheeler : ")
        Data.print_dict(FourWheeler.data_dict_f)
        print("\nOther than the slots which are listed above - Are vacant.\n")
        
    def meridiam(hour1, hour, minute1, minute, in_meridiam, out_meridiam):
        if in_meridiam == 'am' and out_meridiam =='am':
            t_hour = hour1 - hour
            t_minute = minute1-minute
        elif in_meridiam == 'am' and out_meridiam =='pm':
            t_hour = (12 - hour) + (0 + hour1)
            t_minute = minute1-minute
        elif in_meridiam == 'pm' and out_meridiam =='am':
            t_hour = (12 - hour) + (0 + hour1)
            t_minute = minute1-minute
        elif in_meridiam == 'pm' and out_meridiam =='pm':
            t_hour = hour1 - hour
            t_minute = minute1-minute

        result = [t_hour, t_minute]
        return result 

    def choice(self):
        choice = input("\nEnter a choice - \nType 'p' - To park another vehicle \nType 'c' - To checkout a parked vehicle\nType 't' - To track parking\nType 'n' - To not do anything from the given choice\n")
        if choice == 'p' or choice == 'P':
            self.park()
        elif choice == 'c' or choice == 'C':
            Basic.checkout()
        elif choice == 't' or choice == 'T': 
            self.track()
        elif choice == 'n' or choice == 'N':
            return False
        else:
            print("Please enter a valid choice.\n")


if __name__ == "__main__":
    print("Welcome to our Parking Facility !!") 
    call = Basic()   
    call.park()
    while True:
        x = call.choice()
        if x == False:
            break 

    rev = input("\nDo you want to see the profit (y/n  or  Y/N)? ")
    if rev == 'y' or rev == 'Y':
        Revenue.profit()
    elif rev == 'n' or rev == 'N':
        print("Thank You.")
    else :
        print("You should have entered a valid choice.")
