# Qdrant Project

## Overview
Qdrant is a high-performance, vector similarity search engine and database. It is designed to handle large-scale, high-dimensional data and provide fast and accurate search results.

## Features
- **High Performance**: Optimized for speed and efficiency.
- **Scalability**: Easily handles large datasets.
- **Accuracy**: Provides precise similarity search results.
- **Flexibility**: Supports various data types and configurations.

## Installation
To install Qdrant, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/qdrant.git

# Navigate to the project directory
cd qdrant

# Install dependencies
pip install -r requirements.txt
```

## Usage
Here is a basic example of how to use Qdrant:

```python
import qdrant

# Initialize the Qdrant client
client = qdrant.Client()

# Add data to the database
client.add_data(data)

# Perform a similarity search
results = client.search(query)
```

## Contributing
We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions or feedback, please contact us at [email@example.com](mailto:email@example.com).

####create '.env' file and add this
GOOGLE_API_KEY = "gemini key"
FETCH_URL = "**qdrant url**/dashboard#/collections/web_scrapper"
QDRANT_URL = "qdrant url"
QDRANT_API="qdrant api"
