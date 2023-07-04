SELECT DISTINCT e.officeID AS theOfficeID, e.electionDate AS theElectionDate, e.officeStartDate AS theOfficeStartDate, e.officeEndDate AS theOfficeEndDate
FROM Elections e, CandidatesForOffice c, Persons p
WHERE e.officeID = c.officeID 
    AND e.electionDate = c.electionDate 
    AND c.candidateID = p.personID
    AND p.isFelon = TRUE;
