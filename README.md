Code for extracting deposits from csv file and updating the database.

note this is a naive implementation and does not validate if the csv file has already been handled.

For a non naive implementation it is required that we store all information from all files in a database so they rejected
if they are already been handled.

Note, if we can access to the API directly we can record deposits as they happen or once daily.

Furthermore this is a experimental script and should not be used in production before QA has checked the code.