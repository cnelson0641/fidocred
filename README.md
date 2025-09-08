# FidoCred API

This is the FidoCred internal API. It can be run locally for development and testing with sample data.

## Run Locally

Use the deploy script to start the API and install dependencies:

### Navigate to the repo and run the deploy script
./scripts/deploy_to_local.sh

This will:
1. Create/activate a Python virtual environment
2. Install dependencies from requirements.txt
3. Start the FastAPI server on http://127.0.0.1:8000

### Access Swagger UI

Once the server is running, open your browser to: http://127.0.0.1:8000/docs

### Test It

Test endpoints like `/users/`, `/pets/`

## Sample Data

TODO
The API loads sample users, pets, and documents from the `sample_data/` folder for development purposes. No database is required.

## Running Tests

TODO
pytest tests/

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

