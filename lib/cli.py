# Shebang to make the CLI script executable:
#!/usr/bin/env python3

# Import SQLAlchemy:
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# Import classes/data models
# from db.models import {MODEL(S)}

# Import helper functions:
# from helpers import ({HELPER FUNCTIONS})

# Create SQLAlchemy Engine and Session:
# engine = create_engine({DATABASE URL})
# session = sessionmaker(bind=engine)()

# This block tells the interpreter to run the script only if the cli.py file itself is being executed.
if __name__== '__main__':
    print("CLI up and running!")