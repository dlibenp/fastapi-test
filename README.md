# fastapi-test
Backend developer test use fastapi

### Install
* ⚡ create dir: mkdir dirname && cd dirname
* ⚡ clone repository: git clone https://github.com/dlibenp/fastapi-test.git
* ⚡ create virtual environment: python3 -m venv venv
* ⚡ init virtual environment: source venv/bin/activate
* ⚡ install requirenment: pip install -r requirenment.txt

### Run
* ⚡ uvicorn main:app --port 8000 --reload

### Use
* ⚡ curl -X 'POST' 'http://localhost:8000/solution?criterion=completed' -H 'accept: application/json' -H 'Content-Type: application/json' -d '[{"id": 1,"item": "New Order","quantity":1,"price": 1,"status": "completed"}]'

# Test:
* ⚡ python -m unittest test/test_order.py
