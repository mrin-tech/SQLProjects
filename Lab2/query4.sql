SELECT DISTINCT p.personName, oh.rating, eo.salary, p.occupation, eo.officeName
FROM OfficeHolders oh, ElectedOffices eo, Persons p, Elections e
WHERE oh.candidateID = p.personID
    AND oh.officeID = e.officeID
    AND oh.officeID = eo.officeID
    AND oh.electionDate = e.electionDate 
    AND oh.rating IN ('A', 'B')
    AND eo.salary > 125000
    AND p.occupation IS NOT NULL
    AND eo.officeName LIKE '%or'
    
