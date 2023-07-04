CREATE VIEW WronglyDeclaredWinnerView AS
SELECT DISTINCT cfo1.candidateID, cfo1.officeID, cfo1.electionDate, COUNT(cfo2.candidateID) AS numCandidatesWithMoreVotes
FROM CandidatesForOffice cfo1, CandidatesForOffice cfo2, OfficeHolders oh
WHERE cfo1.officeID = cfo2.officeID
    AND cfo1.candidateID = oh.candidateID 
    AND cfo1.wonElection = TRUE
    AND cfo1.electionDate = cfo2.electionDate
    AND cfo1.votes < cfo2.votes
GROUP BY cfo1.candidateID, cfo1.officeID, cfo1.electionDate
HAVING COUNT(cfo2.candidateID) >= 2;
