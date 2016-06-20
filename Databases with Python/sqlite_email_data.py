import sqlite3
import re

# We make a connection and create a cursor object
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# If the table Counts already exists, we drop it. Then we create the table.
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# We specify our file name
# We want to find all the domain names of the email addresses
fname = raw_input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
with open(fname) as fh:
        for line in fh:
            if line.startswith('From: ') and re.findall('@', line) == ['@']:
                line = line.rstrip('\n')
                pieces = line.split()
                for item in pieces:
                    if '@' in item:
                        org = item
                        org = org.split('@')[-1]
                cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
                try:
                    # If we have found the domain name we update the count
                    count = cur.fetchone()[0]
                    cur.execute('UPDATE Counts SET Count=Count+1 WHERE org = ?', (org, ))
                except:
                    # otherwise we insert it
                    cur.execute('''INSERT INTO Counts (org, count)
                        VALUES ( ?, 1 )''', ( org, ))

                # This statement commits outstanding changes to disk each
                # time through the loop - the program can be made faster
                # by moving the commit so it runs only after the loop completes
                conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

# We print out our results. We use str(row[0]) for the email, to avoid any Unicode drama
print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

# We close the cursor object
cur.close()