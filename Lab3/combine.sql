BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

UPDATE ElectedOffices eo
SET officeID = meo.officeID,
    officeName = meo.officeName,
    city = meo.city,
    state = meo.state,
    salary = NULL 
FROM ModifyElectedOffices meo
WHERE eo.officeID = meo.officeID;

INSERT INTO ElectedOffices(officeID, officeName, city, state, salary)
    SELECT officeID, officeName, city, state, 12345.67
    FROM ModifyElectedOffices meo
    WHERE NOT EXISTS (
        SELECT *
        FROM ElectedOffices eo
        WHERE eo.officeID = meo.officeID
    );

COMMIT TRANSACTION;
