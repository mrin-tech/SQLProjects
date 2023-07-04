SELECT p.personName AS contributorName, p2.personName AS candidateName, co.contribution AS contribution
FROM Contributions co, CandidatesForOffice cfo, Persons p,  Persons p2, ElectedOffices eo
WHERE cfo.party = 'Gold'
AND co.candidateID = cfo.candidateID
AND co.officeID = cfo.officeID
AND eo.officeID = cfo.officeID
AND co.contributorID = p.personID
AND cfo.candidateID = p2.personID
AND co.candidateID = cfo.candidateID
AND eo.officeID = cfo.officeID
AND co.officeID = cfo.officeID
AND co.electionDate = cfo.electionDate
ORDER BY contribution DESC, contributorName ASC;
