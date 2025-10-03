# FidoCred API

This is the FidoCred internal API, deployed to AWS, and available at the following API endpoints (Swagger UI docs linked):

1. Dev:  https://w60ru8v9t1.execute-api.us-east-1.amazonaws.com/docs
2. Test: https://bt0sknaq4i.execute-api.us-east-1.amazonaws.com/docs
3. PROD: TODO

## Quick Note on Source Code

All development (including CI/CD) is done through GitLab at https://gitlab.com/cnelson0641-group/fidocred and mirrored to GitHub at https://github.com/cnelson0641/fidocred .

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

## CI/CD

TODO
Everything is tightly integrated with source control, and deployment will be managed through GitLab CI/CD, with as much as possible stored in source control here.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

