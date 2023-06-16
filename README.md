# ML-Service

This repository contains the ML-Service project for the Rahayoo Bangkit Capstone 2023. The ML-Service is responsible for providing machine learning capabilities to the Rahayoo application.

## About

The ML-Service utilizes natural language processing and machine learning techniques to power the chatbot feature of the Rahayoo application. It provides a chatbot interface for users to interact with the application and get responses based on their inputs.

## Installation

To install and run the ML-Service, follow these steps:

1. Clone this repository to your local machine: `git clone https://github.com/rahayoo-bangkit-capstone-2023/ML-Service.git`.
2. Open the project in your preferred Python development environment.
3. Install the required dependencies listed in the `requirements.txt` file: `pip install -r requirements.txt`.
4. Run the Flask application by executing the `app.py` file: `python app.py`.

Note: Make sure you have Python and the necessary dependencies installed to run the ML-Service successfully.

## Usage

Once the ML-Service is up and running, you can interact with the chatbot by sending POST requests to the `/get` endpoint. The chatbot will respond with appropriate messages based on the input provided.

Example usage:

```python
import requests

# Send a POST request to the ML-Service
response = requests.post('http://localhost:8080/get', data={'msg': 'Hi, how are you?'})

# Get the chatbot's response
print(response.json())
```

## Contributing

Contributions to the ML-Service are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or fix: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository: `git push origin feature/your-feature-name`.
5. Open a pull request on the original repository, describing your changes and referencing any related issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

If you have any questions or would like to contact the contributors, please email:

- Itsfanyy
- Rizky Pramudita

Feel free to reach out for any inquiries or further information about the ML-Service project.
