# coinsnark/run.py
import logging
from coinsnark.app import create_app

# app = create_app()

# if __name__ == "__main__":
	# app.run()

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        app.run()
