Wagging Rights
Wagging Rights is a simple program that allows users to create, read, update, and delete information about pets, owners, providers, and services. The program uses SQLAlchemy to connect to a SQLite database, and allows users to perform CRUD operations via a command line interface.

Installation
Clone the repository to your local machine using git clone https://github.com/<your-username>/wagging-rights.git.
Navigate to the project directory using cd wagging-rights.
Install the required packages using pip install -r requirements.txt.
Run the program using python main.py.

Usage

To navigate the SQLite tables in VSCODE, you will need to enter commands 'pipenv install; pipenv shell' and 'alembic upgrade head' to create the wagging_rights.db file. Afterwards you can open 'wagging_rights.db' with SQLITE.

To open the Command Line Interpreter, make sure to run 'python seeds.py' inside of the terminal within the 'app' directory, and then run './cli.py' in terminal to open the CLI.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure to follow the project's coding standards, and include tests for any new features or bug fixes.

License
This project is licensed under the MIT License. See LICENSE for more information.