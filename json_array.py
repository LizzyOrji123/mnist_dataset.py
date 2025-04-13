import json

# Create an array with 784 zeros
payload = {
    "image": [0] * 784
}

# Print the JSON string with indentation for clarity
print(json.dumps(payload, indent=4))

if __name__ == '__main__':
    # Example content to test the script
    print("This script is now executable.")

