username='priya'
password='priya123'

user_name=input('enter name')
pass_word=input('enter password')

if user_name==username and pass_word==password:

 print(''' 
     1.credit
     2.debit
     3.ministatement
     4.exit
''')
 Amt=20000
else:
 print('enter valid name:')

option=int(input('select option:'))
if option==1:
    cre=int(input('enter the amount:'))
    Amt+=cre
    print ('total amount:',Amt)
elif option==2:
    debit= int(input('enter the amount:'))
    Amt-=debit
    print ('total amount:,',Amt)

elif option==3:
    print('========ATM=========')
    print('username:',username)
    print('show the blc Amt',Amt)
    print('THANKU FOR VISITING')
    print('=========ATM=========')

elif option==4:
    print('exit:')
else:
    print('chose corect option:')    
