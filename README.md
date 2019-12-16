# Records App


## Getting Started

### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [ ] [PostgreSQL](https://www.postgresql.org/)

### Setting up + Running

1. Clone the repo:

    ```
    $ git clone https://github.com/ro6ley/records_app.git
    $ cd records_app
    ```

2. With Python 3.6 and Pip installed:

    ```
    $ virtualenv --python=python3 env --no-site-packages
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```

3. Create a PostgreSQL user with the username and password `demouser` and create a database called `records_app`:

    ```
    $ createuser --interactive --pwprompt
    $ createdb records_app
    ```

4. Transfer the task data into the database by executing the `dt_transfer.py` script:

    ```
    $ python db_transfer.py

    # Output
    Skipping row with column titles
    Processed 501 entries.
    ```

5. Run Django Migrations:

    ```
    $ cd records_app
    $ python manage.py migrate
    ```

6. Start the Web Application:

    ```
    $ python manage.py runserver
    ```

7. Navigate to `http://localhost:8000/entries` to view the served data.

## Stack + Justifications

Web Application built using **Django Framework**.

Justification:
- It is a well-established feature-rich framework 
- It comes equipped with an ORM
- Easy and fast setup process

