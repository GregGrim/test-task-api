## test task

### Instrucions
#### To test API :
1. Clone the repository
2. Run the command `pip install -r requirements.txt`
3. create .env file in the root directory and add the following variables
    ```
    DATABASE_URL = sqlite:///./product_database.db
    API_KEY = mysecretapikey
    API_KEY_NAME = access_token
    HOST = localhost
    PORT = 8001
    ```
4. Run the command `python asgi.py`
5. Open the browser and go to `http://127.0.0.1:8001/docs#/products` to test the API