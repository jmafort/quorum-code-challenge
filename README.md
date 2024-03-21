# quorum-code-challenge

This project was developed to fulfil the requirements of a hiring process at Quorum.

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)

## Running the project locally

### Without Docker

To run the code without using Docker, you need to have Python 3.11 or higher installed in your machine, and then follow these steps:
- Clone the repository.
- Create a Python virtual environment using `python -m venv .venv`.
- Activate the virtual environment using `source .venv/bin/activate` (Linux) or `.\.venv\Scripts\activate` (Windows).
- Install the dependencies using `pip install -r requirements.txt`.
- Create a `.env` file in the root of the project. You can use the `.env.dist` file as a template.
- Run the server using `uvicorn app:app --reload`.

### Using Docker

To run the code using Docker, you need to have Docker installed in your machine, and then follow these steps:
- Clone the repository.
- Create a `.env` file in the root of the project. You can use the `.env.dist` file as a template.
- Build the Docker image using `docker build -t quorum-code-challenge .`.
- Run the Docker container using `docker run -p 8000:8000 quorum-code-challenge`.

## Endpoints documentation

After running the project, you can check out the endpoints documentation by accessing `http://host:port/docs` in your browser.

## Running the tests

There are just a few tests to assert the correctness of the response structure and data types. To run the tests, you need to have the project running locally, and then follow these steps:
- Activate the virtual environment using `source .venv/bin/activate` (Linux) or `.\.venv\Scripts\activate` (Windows).
- Run the tests using `pytest`.
