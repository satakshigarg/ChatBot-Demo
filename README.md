# Chatbot using VueJS and FastAPI

This project is a chatbot that can scrape text from an article and search for specific keywords in the scraped text. The frontend of the chatbot is built using VueJS, while the backend is built using FastAPI and uses Postgres with Supabase for text search.

## Requirements

To run this project, you need to have the following installed:

- Node.js and npm
- Python 3.7 or higher
- Docker (optional)

## Installation

1. Clone this repository to your local machine.
git clone https://github.com/your_username/chatbot-vuejs-fastapi.git

2. Navigate to the `frontend` directory and install the dependencies.
cd chatbot-vuejs-fastapi/frontend
npm install

3. Navigate to the `backend` directory and create a virtual environment.

`cd ../backend`

`python3 -m venv env`

4. Activate the virtual environment.

On macOS and Linux:
`source env/bin/activate`

On Windows:
`.\env\Scripts\activate`

5. Install the Python dependencies.
`pip install -r requirements.txt`

6. (Optional) Set up a Supabase project for text search.

If you want to use Supabase for text search, you need to set up a Supabase project and create a table with the name `articles` and a full-text search column with the name `content`. You also need to set the Supabase URL and API key in the `backend/.env` file. See the `.env.example` file for an example.

7. (Optional) Set up a Postgres database for text search.

If you don't want to use Supabase for text search, you can set up a Postgres database and create a table with the name `articles` and a full-text search column with the name `content`. You also need to set the database URL in the `backend/.env` file. See the `.env.example` file for an example.

8. Start the backend server.
`uvicorn main:app --reload`

9. Start the frontend server.
`cd ../frontend`
`npm run serve`

10. Open http://localhost:8080/ in your browser.

## Usage

1. Enter an article URL in the chatbot.
2. The chatbot will scrape the text from the article and display it in the chat.
3. To search for specific keywords in the scraped text, enter the keywords in the chat.
4. The chatbot will display the search results in the chat.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.




