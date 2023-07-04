#! /usr/bin/env python

#  runElectionsApplication Solution

import psycopg2, sys, datetime

# usage()
# Print error messages to stderr
def usage():
    print("Usage:  python3 runElectionsApplication.py userid pwd", file=sys.stderr)
    sys.exit(-1)
# end usage

# The three Python functions that for Lab4 should appear below.
# Write those functions, as described in Lab4 Section 4 (and Section 5,
# which describes the Stored Function used by the third Python function).
#
# Write the tests of those function in main, as described in Section 6
# of Lab4.


 # printNumPartyCandidatesAndOfficeHolders (myConn, theParty):
 # party is an attribute in the CandidatesForOffice table, indicating the candidate for office’s
 # party in an election.  A candidate for office in an election runs in a particular party.
 # Every office holder must be a candidate for office (referential integrity), but some
 # candidates for office are office holders and some are not.  Any office holder was in a
 # particular party in the election in which they were candidates for office.
 #
 # The arguments for the printNumPartyCandidatesAndOfficeHolders Python function are the database
 # connection and a string argument, theParty, which is a party.  This Python function prints
 # out the number of candidates for office and the number of offfice holders who were in myParty
 # when they ran as candidates for office in an election.
 #
 # For more details, including error handling and return codes, see the Lab4 pdf.

def printNumPartyCandidatesAndOfficeHolders (myConn, theParty):
    try:
        myCursor = myConn.cursor()
        # check that theParty has the value NULL and return -1 if it does
        if theParty is None:
            return -1

        # find the number of candidates associated with theParty
        candidateSql = "SELECT COUNT(*) FROM CandidatesForOffice WHERE party = %s"
        # theParty is passed as a tuple to the execute function because it needs to be passed as a sequence
        myCursor.execute(candidateSql, (theParty, ))
        # fetchone returns the next result and [0] returns the first row
        # (similar to the syntax in improveSomeRatings)
        candidateRow = myCursor.fetchone()[0]

        # find the number of officeholders associated with theParty
        officeHoldersSql = "SELECT COUNT(*) FROM CandidatesForOffice cfo, OfficeHolders oh WHERE cfo.party = %s AND oh.candidateID = cfo.candidateID AND oh.officeID = cfo.officeID AND oh.electionDate = cfo.electionDate"
        # theParty is passed as a tuple to the execute function because it needs to be passed as a sequence
        myCursor.execute(officeHoldersSql, (theParty, ))
        # fetchone returns the next result and [0] returns the first row
        # (similar to the syntax in improveSomeRatings)
        officeHolderRow = myCursor.fetchone()[0]

        print("Number of candidates from party " + str(theParty) + " is " + str(candidateRow) + ".")
        print("Number of office holders from party " + str(theParty) + " is " + str(officeHolderRow) + ".\n")
    
    except:
        myCursor.close()
        myConn.close()
        sys.exit(-1)
    
    myCursor.close()
    return 0
    
    
    # This number could be 0 in both cases. That is ok.

    # print statement
    # Number of candidates from party <theParty> is <number of candidates>.”
    # “Number of office holders from party <theParty> is <number of office holders>.”


    # Python function to be supplied by students

# end printNumPartyCandidatesAndOfficeHolders


# increaseLowSalaries (myConn, theSalaryIncrease, theLimitValue):
# salary is an attribute of the ElectedOffices table.  We’re going to increase the salary by a
# certain amount (theSalaryIncrease) for all the elected offices who salary value is less than
# or equal some salary limit (theLimitValue).'
#
# Besides the database connection, the increaseLowSalaries Python function has two arguments,
# a float argument theSalaryIncrease and another float argument, theLimitValue.  For every
# elected office in the ElectedOffices table (if any) whose salary is less than or equal to
# theLimitValue, increaseLowSalaries should increase that salary value by theSalaryIncrease.
#
# For more details, including error handling, see the Lab4 pdf.

def increaseLowSalaries (myConn, theSalaryIncrease, theLimitValue):
    # checks if the parameters fit the constraints and returns a negative number if not
    if theSalaryIncrease <= 0:
        return -1
    if theLimitValue <= 0:
        return -2
    try:
        myCursor = myConn.cursor()
        # updates the salary when the salary is <= the limit value
        sql = "UPDATE ElectedOffices SET salary = salary + %s WHERE salary <= %s"
        # executes the sql statement with the respective parameters
        myCursor.execute(sql, (theSalaryIncrease, theLimitValue))
        # rowcount counts the number of rows where the salary was updated
        updatedSalaryCount = myCursor.rowcount

    except:
        myCursor.close()
        myConn.close()
        sys.exit(-1)
    
    myCursor.close()
    return updatedSalaryCount
    # Python function to be supplied by students
    # You'll need to figure out value to return.

# end increaseLowSalaries


# improveSomeRatings (myConn, theParty, maxRatingImprovements):
# Besides the database connection, this Python function has two other parameters, theParty which
# is a string, and maxRatingImprovements which is an integer.
#
# improveSomeRatings invokes a Stored Function, improveSomeRatingsFunction, that you will need to
# implement and store in the database according to the description in Section 5.  The Stored
# Function improveSomeRatingsFunction has all the same parameters as improveSomeRatings (except
# for the database connection, which is not a parameter for the Stored Function), and it returns
# an integer.
#
# Section 5 of the Lab4 tells you which ratings to improve and how to improve them, and explains
# the integer value that improveSomeRatingsFunction returns.  The improveSomeRatings Python
# function returns the same integer value that the improveSomeRatingsFunction Stored Function
# returns.
#
# improveSomeRatingsFunction doesn’t print anything.  The improveSomeRatings function must only
# invoke the Stored Function improveSomeRatingsFunction, which does all of the work for this part
# of the assignment; improveSomeRatings should not do any of the work itself.
#
# For more details, see the Lab4 pdf.

def improveSomeRatings (myConn, theParty, maxRatingImprovements):

# We're giving you the code for improveSomeRatings, but you'll have to write the
# Stored Function improveSomeRatingsFunction yourselves in a PL/pgSQL file named
# improveSomeRatingsFunction.pgsql
        
    try:
        myCursor = myConn.cursor()
        sql = "SELECT improveSomeRatingsFunction(%s, %s)"
        myCursor.execute(sql, (theParty, maxRatingImprovements))
    except:
        print("Call of improveSomeRatingsFunction with arguments", theParty, maxRatingImprovements, "had error", file=sys.stderr)
        myCursor.close()
        myConn.close()
        sys.exit(-1)
    
    row = myCursor.fetchone()
    myCursor.close()
    return(row[0])

#end improveSomeRatings


def main():

    if len(sys.argv)!=3:
       usage()

    hostname = "cse182-db.lt.ucsc.edu"
    userID = sys.argv[1]
    pwd = sys.argv[2]

    # Try to make a connection to the database
    try:
        myConn = psycopg2.connect(host=hostname, user=userID, password=pwd)
    except:
        print("Connection to database failed", file=sys.stderr)
        sys.exit(-1)
        
    # We're making every SQL statement a transaction that commits.
    # Don't need to explicitly begin a transaction.
    # Could have multiple statement in a transaction, using myConn.commit when we want to commit.
    
    myConn.autocommit = True
    
    # There are other correct ways of writing all of these calls correctly in Python.
        
    # Perform tests of printNumPartyCandidatesAndOfficeHolders, as described in Section 6 of
    # Lab4.  That Python function handles printing when there is no error.
    # Print error outputs here. You may use a Python method to help you do the printing.
    test1 = printNumPartyCandidatesAndOfficeHolders(myConn, 'Silver')
    if test1 < 0:
        print("Error in printNumPartyCandidatesAndOfficeHolders with parameter theParty='Silver'\n")
    
    test2 = printNumPartyCandidatesAndOfficeHolders(myConn, 'Copper')
    if test2 < 0:
        print("Error in printNumPartyCandidatesAndOfficeHolders with parameter theParty='Copper'\n")

    # Perform tests of increaseLowSalaries, as described in Section 6 of Lab4.
    # Print their outputs (including error outputs) here, not in increaseLowSalaries.
    # You may use a Python method to help you do the printing.
    increaseLowSalariesTest1 = increaseLowSalaries(myConn, 6000, 125000)
    if increaseLowSalariesTest1 < 0:
        print("Error in increaseLowSalaries with parameters theSalaryIncrease=6000, theLimitValue=125000\n")
      
    else:
        print("Number of elected offices whose salaries under 125000 were updated by 6000 is", increaseLowSalariesTest1, "\n")

    increaseLowSalariesTest2 = increaseLowSalaries(myConn, 4000, 131000)
    if increaseLowSalariesTest2 < 0:
        print("Error in increaseLowSalaries with parameters theSalaryIncrease=4000, theLimitValue=131000\n")
     
    else:
        print("Number of elected offices whose salaries under 131000 were updated by 4000 is", increaseLowSalariesTest2, "\n")
      

    # Perform tests of improveSomeRatings, as described in Section 6 of Lab4,
    # Print their outputs (including error outputs) here, not in improveSomeRatings.
    # You may use a Python method to help you do the printing.
    # test1
    improveSomeRatingsTest1 = improveSomeRatings(myConn, 'Copper', 6)
    if improveSomeRatingsTest1 >= 0:
        print("Number of ratings which improved for party 'Copper' for maxRatingImprovements value 6 is", improveSomeRatingsTest1, "\n")
    else:
        print("Error in improveSomeRatings with parameters theParty='Copper', maxRatingImprovements=6\n")

    # test2
    improveSomeRatingsTest2 = improveSomeRatings(myConn, 'Gold', 1)
    if improveSomeRatingsTest2 >= 0:
        print("Number of ratings which improved for party 'Gold' for maxRatingImprovements value 1 is", improveSomeRatingsTest2, "\n")
    else:
        print("Error in improveSomeRatings with parameters theParty='Gold', maxRatingImprovements=1\n")

    # test3
    improveSomeRatingsTest3 = improveSomeRatings(myConn, 'Silver', 1)
    if improveSomeRatingsTest3 >= 0:
        print("Number of ratings which improved for party 'Silver' for maxRatingImprovements value 1 is", improveSomeRatingsTest3, "\n")
    else:
        print("Error in improveSomeRatings with parameters theParty='Silver', maxRatingImprovements=1\n")

    # test4
    improveSomeRatingsTest4 = improveSomeRatings(myConn, 'Platinum', 0)
    if improveSomeRatingsTest4 >= 0:
        print("Number of ratings which improved for party 'Platinum' for maxRatingImprovements value 0 is", improveSomeRatingsTest4, "\n")
    else:
        print("Error in improveSomeRatings with parameters theParty='Platinum', maxRatingImprovements=0\n")

    # test5
    improveSomeRatingsTest5 = improveSomeRatings(myConn, 'Copper', 6)
    if improveSomeRatingsTest5 >= 0:
        print("Number of ratings which improved for party 'Copper' for maxRatingImprovements value 6 is", improveSomeRatingsTest5, "\n")
    else:
        print("Error in improveSomeRatings with parameters theParty='Copper', maxRatingImprovements=6\n")
  
    myConn.close()
    sys.exit(0)
#end

#------------------------------------------------------------------------------
if __name__=='__main__':

    main()

# end
