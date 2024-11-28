# Integration Test for MySQL

This GitHub Action performs an integration test for a Python application communicating with a MySQL database. It spins up a MySQL container, creates tables, and runs the Python application to write and verify data in the database.

## Features

- **Automated MySQL Setup**: Starts a MySQL database in a Docker container.
- **Database Table Creation**: Creates the required `users` and `products` tables.
- **Python Application Testing**: Executes the Python application to insert and verify data in the database.
- **Customizable Checkout**: Optionally skips code checkout for flexibility.

### Inputs

| Argument        | Description                         | Required | Default |
| --------------- | ----------------------------------- | -------- | ------- |
| `skip_checkout` | Skip code checkout in the workflow. | No       | `true`  |

---

### Usage

#### Example Workflow

```yaml
name: Integration Test

on: [push, pull_request]

jobs:
  integration-test:
    runs-on: ubuntu-latest
    steps:
      - name: Integration Test for MySQL
        uses: ./
        with:
          skip_checkout: 'false'
```


## Steps Explained

	1.	Checkout Code: Clones the repository unless skip_checkout is set to true.
	2.	Start MySQL: Runs a MySQL 5.7 container with required environment variables.
	3.	Wait for MySQL: Ensures the MySQL container is ready to accept connections.
	4.	Create Tables: Initializes the users and products tables in the MySQL database.
	5.	Build Docker Image: Builds the Docker image for the Python application.
	6.	Run Write Data: Executes the Python application to fetch users and insert them into the database.
	7.	Run Check Data: Runs the Python application to verify the data in the database.

## Example Commands
### Skip Checkout

```yaml
with:
  skip_checkout: 'true'
```

### Run Integration Test
```yaml
with:
  skip_checkout: 'false'
```

## Error Handling

	•	MySQL Initialization: Ensures MySQL is running and healthy before proceeding.
	•	Python Application: Logs errors if data writing or verification fails.
	•	Docker Network: Ensures the application and database communicate via Docker’s host network.

This action provides a streamlined and repeatable process for integration testing with MySQL and Docker, ensuring robust application testing.
