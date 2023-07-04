ALTER TABLE Contributions
ADD CONSTRAINT FkContributorPerson
FOREIGN KEY (contributorID) REFERENCES Persons(personID)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

ALTER TABLE Contributions
ADD CONSTRAINT FkContributorCandidate
FOREIGN KEY (candidateID, officeID, electionDate) REFERENCES CandidatesForOffice(candidateID, officeID, electionDate)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;

ALTER TABLE OfficeHolders
ADD CONSTRAINT FkOfficeHolderCandidate
FOREIGN KEY (candidateID, officeID, electionDate) REFERENCES CandidatesForOffice(candidateID, officeID, electionDate)
    ON DELETE CASCADE
    ON UPDATE RESTRICT;
