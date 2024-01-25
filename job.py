!pip install openpyxl

import requests

def get_python_jobs_count(api_url, params):
    try:
        # Make a GET request to the API with the specified parameters
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Filter jobs for the Python technology
            python_jobs = [job for job in data if 'Key Skills' in job and 'Python' in job['Key Skills']]

            # Get the count of Python jobs
            python_jobs_count = len(python_jobs)

            return python_jobs_count

        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        # Print an error message if an exception occurs
        print(f"An error occurred: {str(e)}")
        return None

# Example usage:
api_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
params = {}  # You may need to provide specific parameters based on the API documentation

python_jobs_count = get_python_jobs_count(api_url, params)

if python_jobs_count is not None:
    print(f"Number of Python jobs: {python_jobs_count}")
else:
    print("Failed to retrieve Python jobs count.")
