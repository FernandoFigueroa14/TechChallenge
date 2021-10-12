#Stori Tech Challenge
#Fernando Figueroa

#import libraries
import csv
# import numpy as np
import smtplib
import email.message
import pymysql

#input filename
# filename = input("Account file (.csv): ")
filename = 'account2'

#variables
colNames = []
rows = []
account = {}
credit = []
debit = []
totalBalance = 0
transactionMonth = {}
months = []
meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# reading csv file
with open('./tests/'+filename+'.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting column names through first row
    colNames = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

#Dictionary with all the data of each column
for col in colNames:
    array = []
    for row in rows:
        array.append(row.pop(0))
    account[col] = array

print(account)
#print(account['Transaction'])

for t in account['Transaction']:
    #Calculations for the total Balance
    totalBalance = totalBalance + float(t)

    # Array for all the credit transactions
    if(t[0] == '+'):
        credit.append(float(t))

    # Array for all the debit transactions
    elif(t[0] == '-'):
        debit.append(float(t))

#credit and debit averages using numpy
# creditAverage = np.average(credit)
# debitAverage = np.average(debit)
creditAverage = sum(credit)/len(credit)
debitAverage = sum(debit)/len(debit)

#
for mes in account['Date']:
    months.append(int(mes[0:mes.find('/')])-1)

# print(months)

for i in range(12):
    transactionMonth[meses[i]] = months.count(i)

# print(transactionMonth)
monthTransactions = ''
for mes in meses:
    if(transactionMonth[mes] != 0):
        monthTransactions = monthTransactions + 'Number of transactions in ' + mes + ': ' + str(transactionMonth[mes]) + '<br>'

#Important information
print('Total Balanca is: ', totalBalance)
#print(credit)
print('Average debit amount: ', debitAverage)
#print(debit)
print('Average credit amount: ',creditAverage)
print(monthTransactions)


#Opening Email Template
email_content = open('email.html', 'r').read().format(totalBalance = totalBalance, monthTransactions = monthTransactions, debitAverage = debitAverage, creditAverage = creditAverage)

#Email configuration
msg = email.message.Message()
msg['Subject'] = 'Prueba 1'

msg['From'] = 'storichallenge@gmail.com'
msg['To'] = 'A01746139@itesm.mx'
password = "sendEmail123"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

#Conection with the email server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

#Send email
server.sendmail(msg['From'], [msg['To']], msg.as_string())

#Data Base Conection
connection = pymysql.connect( host='127.0.0.1', port= 3307, user= 'ferfigue14', passwd='root', db='challenge' )
cursor = connection.cursor()
table = 'CREATE TABLE IF NOT EXISTS {tableName}(id BIGINT(255), date_ VARCHAR(100), transactions FLOAT)'.format(tableName=filename)
cursor.execute(table)
print('Tabla creada')

for i in range(len(account['Id'])):
    query = "INSERT INTO {tableName}(id, date_, transactions) VALUES ({id}, {date}, {transactions});".format(tableName=filename, id=account['Id'][i], date=account['Date'][i], transactions=account['Transaction'][i])
    cursor.execute(query)
connection.commit()

print('Base de datos actualizada')

connection.close()