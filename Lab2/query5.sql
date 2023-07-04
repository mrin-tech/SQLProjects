SELECT DISTINCT eo.officeID AS theOfficeID, eo.officeName AS theOfficeName, eo.city AS theOfficeCity
FROM ElectedOffices eo, OfficeHolders oh1, OfficeHolders oh2, Persons p, Persons p2
WHERE eo.state = 'CA'
    AND oh1.candidateID = p.personID
    AND oh2.candidateID = p2.personID
    AND oh1.candidateID <> oh2.candidateID
