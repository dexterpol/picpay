import requests

def validate_transaction(mock_response_url):
    """
    Function to validate a transaction using a mock authorization response.

    Args:
        mock_response_url (str): URL of the mock authorization response.

    Returns:
        bool: True if the transaction is authorized, False otherwise.
    """

    # Send a GET request to the mock authorization response URL
    response = requests.get(mock_response_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Check if the transaction is authorized
        if response_data["autorized"] == True:
 

                print(f"Transaction  authorized.")
                return True
        else:
                # Transaction is not valid
                print(f"Transaction not valid.")
                return False
     
    else:
        # Error fetching mock authorization response
        print(f"Error fetching mock authorization response: {response.status_code}")
        return False



