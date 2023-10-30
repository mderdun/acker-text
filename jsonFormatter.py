import json

def format_text_as_json(content_lines):
    # Join the content lines to create the content field
    content = "\n".join(content_lines)

    # Create a JSON object with just the content field
    text_json = {
        "content": content
    }

    return text_json

# Function to read content from a text file
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]

# Example usage:
if __name__ == "__main__":
    # Replace 'sample.txt' with the path to your text file
    file_path = "./blackTarantula/1.txt"

    # Read content from the text file
    content_lines = read_text_file(file_path)

    # Format the content as a JSON object
    formatted_json = format_text_as_json(content_lines)

    # Print the JSON object
    print(json.dumps(formatted_json, indent=4))
