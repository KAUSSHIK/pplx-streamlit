# PPLX-Streamlit-App

This Streamlit application provides an intuitive interface for interacting with the Perplexity AI API, allowing users to perform advanced searches and customize various parameters.

## Features

- User-friendly interface for querying Perplexity AI
- Customizable search parameters including temperature, top_p, and max_tokens
- Support for citations, related questions, and image results
- Domain filtering and search recency options
- Real-time response display with formatted markdown

## Prerequisites

- Python 3.7+
- Streamlit
- Requests
- python-dotenv

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/KAUSSHIK/pplx-streamlit
   cd pplx-streamlit
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Perplexity AI API key:
   ```
   PERPLEXITY_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run perplexity_app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit.

3. Enter your query in the text input field.

4. Adjust the search parameters as needed using the provided controls.

5. Click the "Search" button to submit your query.

6. View the results, including the AI's response, citations (if enabled), and related questions (if enabled).

## Customization

You can easily customize the app by modifying the `perplexity_app.py` file. Some areas you might want to adjust include:

- Default values for search parameters
- Layout and styling of the Streamlit components
- Additional features or integrations with other APIs

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [Perplexity AI](https://www.perplexity.ai/) for providing the API
- [Streamlit](https://streamlit.io/) for the amazing app framework

---

Created with ❤️ by Kausshik
