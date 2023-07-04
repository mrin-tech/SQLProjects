CREATE OR REPLACE FUNCTION
improveSomeRatingsFunction(theParty VARCHAR, maxRatingImprovements INTEGER)
RETURNS INTEGER AS $$

    DECLARE
        numRatings  INTEGER;
        theCandidateID INTEGER;

    DECLARE ratingCursor CURSOR FOR 
            SELECT oh.candidateID
            FROM OfficeHolders oh, CandidatesForOffice cfo
            WHERE oh.candidateID = cfo.candidateID
            AND oh.electionDate = cfo.electionDate
            AND cfo.party = theParty
            AND oh.rating IN ('B', 'C', 'D', 'F')
            ORDER BY oh.electionDate DESC;


    BEGIN

    -- Input Validation
	IF maxRatingImprovements <= 0 THEN  
        RETURN -1;
        END IF;

        numRatings := 0;

        OPEN ratingCursor;
        LOOP

            FETCH ratingCursor INTO theCandidateID;

            EXIT WHEN NOT FOUND OR numRatings >= maxRatingImprovements;

            UPDATE OfficeHolders
            SET rating = CASE
                    WHEN rating = 'B' THEN 'A'
                    WHEN rating = 'C' THEN 'B'
                    WHEN rating = 'D' THEN 'C'
                    WHEN rating = 'F' THEN 'D'
            END
            WHERE candidateID = theCandidateID;

        numRatings := numRatings + 1;

        END LOOP;
        CLOSE ratingCursor;

        RETURN numRatings;

    END

$$ LANGUAGE plpgsql;
