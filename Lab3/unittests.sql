INSERT INTO Contributions VALUES (16, 2, 107, '4/15/15', 60000.06);

INSERT INTO Contributions VALUES (16, 80, 102, '9/25/18', 60.87);

INSERT INTO OfficeHolders VALUES (15, 102, '10/03/23', 'A');

----------------------------------------
-- First General Constraint
-- meets the constraint
UPDATE Contributions
SET contribution = 1000
WHERE contributorID = 12 AND candidateID = 3 AND officeID = 107 AND electionDate = '5/18/23';

-- violates the constraint
UPDATE Contributions
SET contribution = -10
WHERE contributorID = 12 AND candidateID = 3 AND officeID = 107 AND electionDate = '5/18/23';

----------------------------------------
-- Second General Constraint
-- meets the constraint
UPDATE Elections
SET officeEndDate = '2/2/20'
WHERE officeStartDate = '2/15/18' AND officeID = 102 AND electionDate = '5/2/34';


-- violates the constraint
UPDATE Elections
SET officeEndDate = '2/15/18'
WHERE officeStartDate = '2/2/20' AND officeID = 102 AND electionDate = '5/2/34';

----------------------------------------
-- Third General Constraint
-- meets the constraint
UPDATE CandidatesForOffice
SET votes = NULL, wonElection = NULL
WHERE candidateID = 10 AND officeID = 101 AND electionDate = '5/15/05';

-- violates the constraint
UPDATE CandidatesForOffice
SET votes = NULL, wonElection = FALSE
WHERE candidateID = 10 AND officeID = 101 AND electionDate = '5/15/05';


