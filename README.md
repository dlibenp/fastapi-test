# fastapi-test
## Backend developer test use fastapi

### ⚡ Install
1. Create dir:
   ```shell
   mkdir dirname && cd dirname
   ```
3. Clone repository:
   ```shell
   git clone https://github.com/dlibenp/fastapi-test.git
   ```
4. Create virtual environment:
   ```shell
   python3 -m venv venv
   ```
6. Init virtual environment:
   ```shell
   source venv/bin/activate
   ```
8. Install requirenment:
   ```shell
   pip install -r requirenment.txt
   ```

### ⚡ Run
```shell
uvicorn main:app --port 8000 --reload
```

### ⚡ Use
```shell
curl -X 'POST' 'http://localhost:8000/solution?criterion=completed'
-H 'accept: application/json' -H 'Content-Type: application/json'
-d '[{"id": 1,"item": "New Order","quantity":1,"price": 1,"status": "completed"}]'
```

### ⚡ Test:
```shell
python -m unittest test/test_order.py
```

### ⚡ Create docker image:
1. ```shell
   docker build -t fastapi-test .
   ```
2. ```shell
   docker run -d -p 8000:8000 fastapi-test
   ```
