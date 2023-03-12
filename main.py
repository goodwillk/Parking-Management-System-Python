from pprint import pprint

class Parking():
    """Base class which will get inherited by it's child classes"""
    def __init__(self, owner_name=0, vehicle_number=0, in_time=0):
        self.owner_name = owner_name
        self.vehicle_number = vehicle_number
        self.in_time = in_time

    def payment(self, hour, minute):
        t_hour = hour * 60
        t_minute = minute
        t_total = t_hour + t_minute 
        return t_total



class FourWheeler(Parking):
    """Perform functions for 4-Wheelers"""
    park_slot_f = [0] * 20        #Total 20 parking slots for 4-wheeler
    counter_f = 0

    def __init__(self, owner_name=0, vehicle_number=0, in_time=0):
        super().__init__(owner_name, vehicle_number, in_time)


    @classmethod
    def alot_parking(cls):
        for i in cls.park_slot_f:
            if cls.park_slot_f[i] == 0:
                print(f"Park at Slot {i+1} of 4-wheeler parking.")
                cls.park_slot_f[i] = 1
                return i+1
                break
            elif cls.park_slot_f[i] == 0:
                continue

    @classmethod
    def payment(cls, hour, minute): 
        t_total = super().payment(cls, hour, minute)
        result = (40) * (t_total/60)
        print("So, Your bill will be : {:.2f} Rs" .format(result)) 
        
        cls.counter_f += result

        return result



class TwoWheeler(Parking):
    """Perform functions for 2-Wheelers"""
    park_slot_t = [0] * 10         #Total 10 parking slots for 2-wheeler
    counter_t = 0

    def __init__(self, owner_name=0, vehicle_number=0, in_time=0):
        super().__init__(owner_name, vehicle_number, in_time) 


    @classmethod
    def alot_parking(cls):
        for i in cls.park_slot_t:
            if cls.park_slot_t[i] == 0:
                print(f"Park at Slot {i+1} of 2-wheeler parking.")
                cls.park_slot_t[i] = 1
                return i+1
                break
            elif cls.park_slot_t[i] == 0:
                continue

    @classmethod
    def payment(cls, hour, minute):
        t_total = super().payment(cls, hour, minute)
        result = (20) * (t_total/60)
        print("So, Your bill will be : {:.2f} Rs" .format(result)) 

        cls.counter_t += result 

        return result



class Revenue(FourWheeler, TwoWheeler):
    """Will calculate the total revenue"""
    
    @classmethod
    def profit(cls):
        two_profit = TwoWheeler()
        four_profit = FourWheeler()

        two = two_profit.counter_t
        four = four_profit.counter_f

        print("Profit from 2 wheeler parkings : {:.2f} Rs" .format(two))
        print("Profit from 4 wheeler parkings : {:.2f} Rs" .format(four))
        
        total_profit = two + four
        print("Total profit from parkings : {:.2f} Rs" .format(total_profit))



class Data(FourWheeler, TwoWheeler):
    """
    Will save the data regarding Vehicle Number and which parking slot is alloted to them.
    Which parking slot is empty and which one is filled.
    """
    data_dict_number= {}
    data_dict_time_t = {}
    data_dict_time_f = {}
    
    @classmethod
    def add_slot(cls, slot, number):
        cls.data_dict_number[slot] = number
        
    @classmethod
    def add_intime_t(cls, slot, intime):
        cls.data_dict_time_t[slot] = intime
        
    @classmethod
    def add_intime_f(cls, slot, intime):
        cls.data_dict_time_f[slot] = intime

    @classmethod
    def print_dict(cls):
        pprint(cls.data_dict_number)

    @classmethod
    def delete_dict_t(cls, num):
        del cls.data_dict_time_t[num]
        
    @classmethod
    def delete_dict_f(cls, num):
        del cls.data_dict_time_f[num]



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



def outtime():
    out_time = input("Enter your out-time in format (HH:MM): ").split()
    for time in out_time:
        hour1, minute1 = [int(i) for i in time.split(':')]
    return hour1, minute1


        
        
class basic:
    def park(self):
        store = data()
        name = input("Enter your name : ")
        number = int(input("Enter your vehicle's number (Four Digits): "))
        
        in_time = str(input("Enter your in-time in format (HH:MM): "))
        in_meridiam = input("Enter am or pm : ")

        time = f"{in_time},{in_meridiam}"

        print("For 4-wheeler ticket price for 60 minutes is 40 Rs.")
        print("For 2-wheeler ticket price for 60 minutes is 20 Rs.")
        type = input("Enter Your vehicle type (i.e., 4-wheeler or 2-wheeler) : ")

        if type == '4-wheeler':
            four = FourWheeler(name, number, time)
            slot = four.alot_parking()
            store.add_intime_f(slot, time)
            store.add_slot(slot, number)
            
        elif type == '2-wheeler':
            two = TwoWheeler(name, number, time)
            slot = two.alot_parking()
            store.add_intime_t(slot, time)
            store.add_slot(slot, number)
            
        else:
            print("Please, Enter your vehicle type correctly.")
            
            
    @classmethod
    def checkout(cls):
        data1 = data()
        
        type = input("Enter vehicle type :")
        
        if type == '2-wheeler' :
            num = int(input("Enter vehicle's parking slot number for it's checkout :"))
            time = data1.data_dict_time_t.get(int(num))
            for t in time:
                hour_minute, in_meridiam = [t for t in time.split(',')]
                for i in hour_minute:
                    hour, minute = [i for i in hour_minute.split(':')]
            data1.delete_dict_t(num)
                    
        elif type == '4-wheeler' :
            num = int(input("Enter vehicle's parking slot number for it's checkout :"))
            time = data1.data_dict_time_f.get(int(num))
            for t in time:
                hour_minute, in_meridiam = [t for t in time.split(',')]
                for i in hour_minute:
                    hour, minute = [i for i in hour_minute.split(':')]
                    
            data1.delete_dict_f(num)
            
        hour = int(hour)
        minute = int(minute)

        hour1, minute1 = outtime()
        out_meridiam = input("Enter am or pm : ")
        print(f"Out-Time is at {hour1}:{minute1} .")

        hour, minute = meridiam(hour1, hour, minute1, minute, in_meridiam, out_meridiam)
        
        if type == '4-wheeler' :
            four = FourWheeler
            four.payment(hour, minute)
        elif type == '2-wheeler' :
            two = TwoWheeler
            two.payment(hour, minute)
        
    def track(self):
        check = data()
        choice = input("Enter which type of parking you want to track (i.e., 4-wheeler or 2-wheeler) ? ")
        
        if choice == '4-wheeler' :
            track = list(check.data_dict_time_f)
            for t in track:
                print(f"Parking '{t}' is occupied")
            print(f"Other than the parking's listed above - Are vacant.")
        elif choice == '2-wheeler' :
            track = list(check.data_dict_time_f)
            for t in track:
                print(f"Parking '{t}' is occupied")
            print(f"Other than the parking's listed above - Are vacant.")
        else:
            print("You should have entered a valid choice.")


    def choice(self):
        choice = input("Enter a choice :\nType 'park' - To park another vehicle \nType 'checkout' - To checkout parked vehicle \nType 'track' - To track parking\nType'none' - To not do anything from the given choice\n")

        if choice == 'park' or choice == 'Park':
            self.park()
            return True
        elif choice == 'checkout' or choice == 'Checkout':
            basic.checkout()
            return True
        elif choice == 'track' or choice == 'Track': 
            self.track()
            return True
        elif choice == 'none' or choice == 'None':
            return False
        else:
            print("Please enter a valid choice.")



if __name__ == "__main__":
    print("Welcome to our Parking Facility ")
    
    abc = basic()
    abc.park()

    while True:
        x = abc.choice()
        if x == False:
            break 

    rev = input("Do you want to see the profit (y/n  or  Y/N)? ")
    if rev == 'y' or rev == 'Y':
        rev_profit = Revenue()
        rev_profit.profit()
    elif rev == 'n' or rev == 'N':
        print("Thank You.")
    else :
        print("You should have entered a valid choice.")

    rec = data()

    record = input("Do you want to track all parking slots, like which one was occupied by which Vehicle (y/n  or  Y/N)? ")
    if record == 'y' or record == 'Y':
        rec.print_dict()
    elif record == 'n' or record == 'N':
        print("It's OK. Thank you")
    else:
        print("You should have entered a valid choice.")
