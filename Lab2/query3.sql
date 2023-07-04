SELECT DISTINCT p.personID, p.occupation
FROM Persons p, CandidatesForOffice cfo
WHERE cfo.candidateID = p.personID
AND cfo.wonElection = FALSE 
AND cfo.candidateID NOT IN (
  SELECT oh.candidateID 
  FROM OfficeHolders oh
)
