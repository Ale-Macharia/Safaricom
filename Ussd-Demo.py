Customer_name = 'Alex', 'MK'

print(f'''
Helloo {Customer_name[0]},
Welcome to Safaricom ussd'
'''
   )
print(f'''
      This is Safaricom Customer self service (*100#)
      1. Buy Data
      2. M-pesa Services
      3. My Account
    ''')


def safaricom_data():
    global choice
    global Customer_name


    choice = input('What service do you want: ')
    if choice == '*544#' or 'Data'.casefold:
        print('''
          Welcome To Safaricom Data
          1. Buy Data
          2. Check Balance
          3. Sambaza Data
          4. New Data Offers 
          5. more...
        ''')
    data_ussd = input('What\'s your data choice: ')
    if data_ussd == '1':
        print('''
              Buy Data
              1.sh 20 = 200mb 24 hours
              2.sh 15 = 1gb 1hour
              3.sh 50 = 350mb 7days
              00. Go Back
        ''')
        data_choice = input('What data do you want to buy: ')
        if data_choice == '1':
            pin = int(input('Enter Pin confirm you ksh 20 from you m-pesa: '))
            if pin:
                print(f'''
                      
### messages ###
{Customer_name[0]}
Confirmed !! You Have Bought 200mbs for 24 hours @ ksh20 from m-pesa
                      ''')
        if data_choice == '2':
            pin = int(input('Enter Pin confirm you ksh 15 from you m-pesa: '))
            if pin:
                print('Confirmed !! You Have Bought 1024mbs for 1 hour @ ksh15 from m-pesa')
        if data_choice == '3':
            pin = int(input('Enter Pin confirm you ksh 50 from you m-pesa: '))
            if pin:
                print('Confirmed !! You Have Bought 350mbs @ ksh50 from m-pesa')
        if data_choice == '00':
                safaricom_data()

safaricom_data()
