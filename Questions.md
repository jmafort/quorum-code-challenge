# Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

Since time is valuable resource, I decided to use FastAPI to build the application, as it is a fast, easy to use and easy understand framework. It also has great integrations with some other tools I'll be discussing here, including automatic documentation generation.

Pydantic was used to create the DTOs, as it is a powerful library to validate and transfer data inside and outside the application with its built-in serialization.

To read the CSV files, I used the built-in Python library `csv`, as it is a simple and easy to use library to handle CSV files. I could've used `pandas` to handle the CSV files, but I was trying to limit the number of external dependencies. Maybe it should be a good ideia to implement with a little more time, since it makes querying the data easier, and would make the service layer more performatic when dealing with bigger CSVs.

I used Jinja2 to create the HTML templates, as it is a powerful and easy to use library to create HTML templates. It also has a great integration with FastAPI, making it easy to use.

The use of Docker and Pytest was to show what my usual development proccess looks like. It would be great to add more tests to the application, but I was trying to limit the time spent on things that were not the main focus of the assignment.

As for the extensibility of the application, I tried to make it as modular as possible, so it would be easy to add new features and endpoints to the application. The use of the adapter pattern and Dependecy Injection in the service layer makes it easier to change the data source, to a database for example, as the DTOs can be used in ORM-Mode to validade data from database models and would not require significant changes.

As for the time complexity, it would be O(n) for the CSV parsing, as it would need to read the entire file of each CSV to parse it. The space complexity in this specific case is also O(n), since all the information present in the CSV is being used, but could be smaller, since the use of generators makes it possible to only load into the memory the data that will be really used. The service layer would have a time complexity of O(n*m) in the worst cases. This time complexity can be reduced using a database, gaining access to joins, indexes and other optimizations present in this kind of data source.

### How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

As I'm using pydantic models as DTOs, I would just need to add the new fields to the models and the CSV parsing would be able to handle these new fields automatically. The only scenario I would need to do anything more is in case other new columns have a significant impact in the business rules, but even then it would be just an adaptative change in the code present in the service layer.

### How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

Since the solution I built is separated by modules, each one with its own responsabilities, it would be easy to build a new module to parse the given data into a CSV file. From there, I could continue to use the same solution.

### How long did you spend working on the assignment?

I spent about 4 hours working on the assignment.
