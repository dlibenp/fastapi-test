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
uvicorn main:app --host 0.0.0.0 --port 8000 --reload --env-file=.env
```

### ⚡ Use
```shell
curl -X 'POST' 'https://localhost:8000/solution?criterion=completed' -H 'accept: application/json' -H 'Content-Type: application/json'
-d '{
   "orders": [
      { "id": "1b668a45-1473-4769-9984-bd08083e38be", "item": "New Order", "quantity": 3, "price": 2, "status": "completed",
      "created_at": "2023-10-07T22:56:42.327339" }
   ]
}'
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
