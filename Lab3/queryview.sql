--1) Your Fraudulent Officeholder SQL query.
SELECT cfo.candidateID, p.personName, cfo.officeID, cfo.electionDate
FROM Persons p, CandidatesForOffice cfo, OfficeHolders oh, WronglyDeclaredWinnerView wdwv
WHERE cfo.candidateID = p.personID
  AND cfo.candidateID = wdwv.candidateID
  AND cfo.candidateID = oh.candidateID
  AND cfo.officeID = oh.officeID
  AND cfo.officeID = wdwv.officeID
  AND cfo.electionDate = oh.electionDate
  AND cfo.electionDate = wdwv.electionDate
GROUP BY cfo.candidateID, p.personName, cfo.officeID, cfo.electionDate;

--2) A comment with the output of that query on the load data before the update.
/*
 candidateid |    personname    | officeid | electiondate 
-------------+------------------+----------+--------------
           3 | Alexander Hilton |      101 | 2018-01-31
           5 | Javier Lopez     |      107 | 1987-07-19
           9 | Penny Taylor     |      106 | 2005-05-15
(3 rows)
*/

--3) A SQL statement which performs the update.
UPDATE CandidatesForOffice
SET wonElection = FALSE
WHERE candidateID = 9
  AND officeID = 106
  AND electionDate = '2005-05-15'; 

--4) Repeat your Fraudulent Officeholder SQL query.
SELECT cfo.candidateID, p.personName, cfo.officeID, cfo.electionDate
FROM Persons p, CandidatesForOffice cfo, OfficeHolders oh, WronglyDeclaredWinnerView wdwv
WHERE cfo.candidateID = p.personID
  AND cfo.candidateID = wdwv.candidateID
  AND cfo.candidateID = oh.candidateID
  AND cfo.officeID = oh.officeID
  AND cfo.officeID = wdwv.officeID
  AND cfo.electionDate = oh.electionDate
  AND cfo.electionDate = wdwv.electionDate
GROUP BY cfo.candidateID, p.personName, cfo.officeID, cfo.electionDate;

--5) A second comment with the output of that query after the update.
/*
candidateid |    personname    | officeid | electiondate 
--------------+------------------+----------+--------------
           3 | Alexander Hilton |      101 | 2018-01-31
           5 | Javier Lopez     |      107 | 1987-07-19
(2 rows)
*/
