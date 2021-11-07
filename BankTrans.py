def new_acct():
  # print("here")
  name = input("Enter your name: ")
  mob = int(input("Enter your phone number: "))
  email_id = input("Enter your email: ")
  if "@gmail.com" in email_id:
    pass
  else:
    print("Incorrect email!")
    email_id = input("Please re-enter your email: ")
  
  aadhar = int(input("Enter your Aadhar Number: "))
  if not len(str(aadhar)) == 12:
    print("Please enter correct Aadhar number.")
  pan = input("Enter your PAN: ")
  
  details = {
		'Name': name,
		'Phone number': mob,
		'Email': email_id,
		'Aadhar': aadhar,
		'Pan': pan
	}
  
  records.insert_one(details)
  print("Your account has been created!")


def deposit_mon():
  depo_aadhar = int(input("Verify your Aadhar: "))
  depo_amt = int(input("Enter the amount to be deposited: "))
  # print(depo_amt)
  
  for x in records.find({'Aadhar' : depo_aadhar}):
    if depo_aadhar == x['Aadhar']:
      # print(x['Aadhar'])
      if records.find({'Total Amount': {'$exists': True}}): #Checking if the amount attribute is already present
        total_depo = x['Total Amount'] + depo_amt

        update_user_details_depo = {'Aadhar': depo_aadhar}
        update_user_value_depo = {'$set': {'Total Amount': total_depo}}
        
        records.update_one(update_user_details_depo, update_user_value_depo)
        print(str(depo_amt) + " has been deposited in your account.")

      #if the amount attribute is not present, inserting one in the document
      else: 
        update_user_details_depo = {'Aadhar': depo_aadhar}
        update_user_value_depo = {'$set': {'Total Amount': depo_amt}}
        
        records.update_one(update_user_details_depo, update_user_value_depo)
        print(depo_amt + " has been deposited in your account.")
        
    else:
        depo_aadhar = int(input("Please verify your Aadhar: "))

def withdraw_mon():
  with_aadhar = int(input("Verify your Aadhar: "))
  with_amt = int(input("Enter the amount to be withdrawn: "))

  for x in records.find({'Aadhar': with_aadhar}):
    if with_aadhar == x['Aadhar']:
      # print(x['Total Amount'])
      total_with = x['Total Amount'] - with_amt
      # print(total_with)
      update_user_details_with = {'Aadhar': with_aadhar}
      update_user_value_with = {'$set': {'Total Amount': total_with}}
      
      records.update_one(update_user_details_with, update_user_value_with)

      print("Please collect your ", with_amt)
      print("Remaining balance: ", total_With)
    else:
      with_aadhar = int(input("Please verify your Aadhar: "))

print("What are you here for?")
action = int(input("""
	1. Create an Account
	2. Deposit money
	3. Withdraw money
	"""))

if action == 1:
	new_acct()
elif action == 2:
	deposit_mon()
elif action == 3:
	withdraw_mon()
elif action > 3:
  print("Invalid input!")
  action = int(input("""
	1. Create an Account
	2. Deposit money
	3. Withdraw money
	"""))