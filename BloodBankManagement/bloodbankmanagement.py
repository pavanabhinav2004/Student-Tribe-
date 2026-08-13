class Donor:
    def __init__(self,donor_id,name,age,blood_group,phno,city):
        self.donor_id = donor_id
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.phno = phno
        self.city = city 
class BloodBank:
  def __init__(self):
    self.donations = {}
    self.stock = {}
    self.requests = []
   
  def donate_blood(self):
    donor_id = input("Enter your donor id :") 
    for donor in donors:
      if donor.donor_id  == donor_id:
        blood_group = donor.blood_group
        if donor_id in self.donations.keys():
          self.donations[donor_id] += 1
        else:
          self.donations[donor_id] = 1
        if blood_group in self.stock.keys():
          self.stock[blood_group] += 1
        else:
          self.stock[blood_group] = 1
        print(f"Donation of {donor_id} recorded successfully!")
        return
    print("Donor not found!")
  
  def request_blood(self):
    blood_group = input("Enter Blood Group :")
    packets_needed = int(input("No. of packets required: "))
    if self.stock[blood_group] >= packets_needed:
      self.stock[blood_group] -= packets_needed
      print(f"{packets_needed} packets of blood group {blood_group} has been dispatched !")
    else:
      print("Sorry, Insufficient Stock")
  def view_stock(self):
    for blood_group in self.stock:
      print(f"{blood_group}:{self.stock[blood_group]}")
  def view_donations(self):
    for donor_id,count in self.donations.items():
      print(f"{donor_id}:{count}")

donors = []
bank = BloodBank()
def add_donors():
  name = input("Please enter your name: ")
  age = int(input("Please enter your age: "))
  blood_group = int(input("Choose blood group: *** 1.A+ 2.A- 3.B+ 4.B- 5.AB+ 6. AB- 7.O+ 8.O- *** "))
  if blood_group == 1:
    blood_group = 'A+'
  elif blood_group == 2:
    blood_group = 'A-'
  elif blood_group == 3:
    blood_group = 'B+'
  elif blood_group == 4:
    blood_group = 'B-'
  elif blood_group == 5:
    blood_group = 'AB+'
  elif blood_group == 6:
    blood_group = 'AB-'
  elif blood_group == 7:
    blood_group = 'O+'
  elif blood_group == 8:
    blood_group = 'O-'
  else:
    print("Invalid Input")
  phno = int(input("Please Enter your phone number: "))
  city = input("Please enter name of your city:" )

  donor_id = f"D00{0 + len(donors)+1}"

  donor = Donor(donor_id,name,age,blood_group,phno,city)

  donors.append(donor)
  print(f"Donor {donor_id} 1Added Successfully!")

def view_donor():
  if not donors:
    print("No donors available!")
    return

  print("\n----- Donor Details -----")
  for donor in donors:
      print("Donor ID:", donor.donor_id)
      print("Name:", donor.name)
      print("Age:", donor.age)
      print("Blood Group:", donor.blood_group)
      print("Phone Number:", donor.phno)
      print("City:", donor.city)
      print("------------------------")

def search_donor():
  search = input("Enter Donor id: ")
  for donor in donors:
    if donor.donor_id == search:
      print("Donor ID:", donor.donor_id)
      print("Name:", donor.name)
      print("Age:", donor.age)
      print("Blood Group:", donor.blood_group)
      print("Phone Number:", donor.phno)
      print("City:", donor.city)
      print("------------------------")
      return
    
  print("Donor not found!")
def update_donor():
  update = input("Enter Donor id to update :")
  for donor in donors:
    if donor.donor_id == update:
      donor.name = input("Enter New Name: ")
      donor.age = int(input("Enter New Age: "))
      donor.blood_group = input("Enter New Blood Group: ")
      donor.phno = int(input("Enter New Phone Number: "))
      donor.city = input("Enter New City: ")
      return  
    
  print("Donor not found!")

def delete_donor():
  delete = input("Enter Donor id to delete:")
  for donor in donors:
    if donor.donor_id  == delete:
      donors.remove(donor)
      return
      print("Donor deleted!")
    else:
      print("Donor not found!")

while True:
  print("\n========== BLOOD BANK MANAGEMENT ==========")
  print("1. Add Donor")
  print("2. View Donors")
  print("3.Search Donor")
  print("4.Update Donor")
  print("5.Delete Donor")
  print("6.Donate Blood")
  print("7.Request Blood")
  print("8.View Blood Stock")
  print("9.View Donations")
  print("10.Exit")
  print("\n============================================")
  choice = int(input("Enter Your Choice: "))
  if choice == 1:
    add_donors()
  elif choice == 2:
    view_donor()
  elif choice == 3:
     search_donor()
  elif choice == 4:
     update_donor()
  elif choice == 5:
     delete_donor()
  elif choice == 6:
     bank.donate_blood()
  elif choice == 7:
     bank.request_blood()
  elif choice == 8:
     bank.view_stock()
  elif choice == 9:
     bank.view_donations()
  elif choice == 10:
    print("Thank You !") 
    break
  else:
    print("Invalid choice! Please try again")