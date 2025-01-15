import json
import base64
from addTwoNumbers import lambda_add_numbers, lambda_store_document  # Replace with the correct filename if needed

# Test lambda_add_numbers
event_add_numbers = {
    "num1": 5,
    "num2": 10
}
context = {}  # Context is not used in this case, so it's an empty dictionary
response_add_numbers = lambda_add_numbers(event_add_numbers, context)
print("lambda_add_numbers Response:", json.dumps(response_add_numbers, indent=4))

# Test lambda_store_document
event_store_document = {
    "bucket_name": "your-bucket-name",
    "file_name": "test_document.pdf",
    "file_content": base64.b64encode(b"Sample document content").decode('utf-8')  # Example base64 content
}
response_store_document = lambda_store_document(event_store_document, context)
print("lambda_store_document Response:", json.dumps(response_store_document, indent=4))
