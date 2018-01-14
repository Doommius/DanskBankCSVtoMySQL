'''
Created by Pycharm.
User: Jervelund
Date: 11 / 9 / 17
Time: 12:21 AM

Code for extracting deposits from csv file and updating the database.

note this is a naive implementation and does not validate if the csv file has already been handled.

For a non naive implementation it is required that we store all information from all files in a database so they rejected
if they are already been handled.

Note, if we can access to the API directly we can record deposits as they happen or once daily.

Furthermore this is a experimental script and should not be used in production before QA has checked the code.

'''
from IPython.lib.deepreload import reload
import mysql.connector
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



# encoding: latin1
filename = "1.txt"
list = []
i = 0
# total = 0


cnx = mysql.connector.connect(user='user', password="password",
                              host='server',
                              database='schema')
cursor = cnx.cursor()

with open(filename) as f:
    for line in f:
        tmplist = line.split(';')
        # this needs to be done by checking tmplist[1] agiast the database to see if the username is in the database,
        # maybe wildcard? (needs to be protected agaist attempted exploits.
        if (("mjerv15") in tmplist[1]):
            print(tmplist[0] + "    " + tmplist[1] + "    " + tmplist[2] + "    " + tmplist[4])
        list.append([tmplist[0], tmplist[1], tmplist[2]])
        # i = 0
# print (total)
for line in list:
    add_user = ("INSERT INTO TRANSACTION"
                "(bank_note, amount, date_transfered, status) "
                "VALUES (%(note)s, %(amount)f, %(balance)s,%(status)s)")

    # Insert salary information
    data_user = {
        'note': line[1],
        'amount': line[2],
        'date': line[0],
        'status': 0
    }
    print(data_user)
    cursor.execute(add_user, data_user)

    # Make sure data is committed to the database
    cnx.commit()

cursor.close()
cnx.close()
