import os
import time

VENV = True

# Exit out of the scripts directory
# os.system("cd ..")

serve_command = "mkdocs serve"

# Enter the virtual environment
if VENV:
    # os.system(".\\venv\\Scripts\\activate")
    serve_command = f"./venv/bin/python -m {serve_command}"

while True:
    os.system("./venv/bin/python -m mkdocs serve")
    time.sleep(1.5)
