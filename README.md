# AI Customer Support Agent

A small AI customer-support proof of concept built with **FastAPI** and **Google Gemini**.

The project demonstrates how an LLM can use backend tools to retrieve reliable information instead of generating everything from its own knowledge.

## What It Does

The agent can understand customer requests and use a backend tool to retrieve order information.

For example:

> "What is the status of order 1001?"

The flow is:

```text
User
  ↓
FastAPI /chat
  ↓
Gemini
  ↓
Tool call
  ↓
get_order_status()
  ↓
Order data
  ↓
Gemini
  ↓
Final response
```

The order data is currently stored in a small in-memory Python dictionary for demonstration purposes.

## Key Concepts Demonstrated

* LLM integration with Gemini
* LLM tool/function calling
* FastAPI REST API
* Structured backend tools
* Separation between AI reasoning and application data
* Input validation
* Handling missing orders
* Basic automated testing with pytest
* Environment-based API key configuration

## Project Structure

```text
ai-support-agent/
├── .env
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   └── tools.py
└── tests/
    └── test_tools.py
```

## How It Works

### 1. User Request

The client sends a request to the FastAPI endpoint:

```http
POST /chat
```

Example:

```json
{
  "message": "What is the status of order 1001?"
}
```

### 2. Gemini Determines Whether a Tool Is Needed

The model receives instructions to use the `get_order_status` tool when it needs order information.

The model does not directly access the order data.

### 3. Backend Tool Retrieves the Data

The backend executes:

```python
get_order_status(order_id)
```

The tool returns structured data such as:

```json
{
  "order_id": "1001",
  "customer": "Ahmed",
  "status": "shipped",
  "total": 125.50,
  "estimated_delivery": "2026-10-05"
}
```

### 4. Gemini Generates the Response

Gemini receives the tool result and uses it to formulate the final response to the customer.

This keeps the application data separate from the model's generated knowledge and reduces the risk of the model inventing order information.

## Setup

### Requirements

* Python 3.12+
* Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-support-agent.git
cd ai-support-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install google-genai python-dotenv fastapi uvicorn pytest
```

### 4. Configure the API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

**Do not commit the `.env` file or expose your API key publicly.**

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Example Request

Using the `/chat` endpoint:

```json
{
  "message": "What is the status of order 1001?"
}
```

The agent can retrieve the order information through the backend tool and return a natural-language response.

You can also test an unknown order:

```json
{
  "message": "What is the status of order 9999?"
}
```

The backend tool returns an error instead of inventing order information.

## Testing

Run:

```bash
pytest
```

The current tests cover:

* Retrieving an existing order
* Handling an unknown order

## Design Principle

A key design principle of this project is:

> **The LLM handles language and reasoning, while the backend remains the source of truth for application data.**

This separation becomes particularly important in production systems where AI-generated information should not be trusted as the authoritative source for customer, financial, or operational data.

## Current Limitations

This is a learning/proof-of-concept project and is not intended to represent a production-ready customer-support system.

Currently:

* Order data is stored in memory
* No authentication or authorization
* No persistent database
* No production observability
* No rate limiting
* Basic error handling
* Limited test coverage

## Potential Production Improvements

A production implementation could add:

* PostgreSQL or another persistent database
* Authentication and authorization
* Tool-level permission controls
* Input validation and stricter schemas
* Timeouts and retry handling
* Structured logging and monitoring
* Rate limiting
* More comprehensive integration tests
* Conversation history
* Human escalation for complex cases
* Protection of sensitive customer information

## Purpose

This project was built as a hands-on exploration of **LLM tool calling and AI-assisted application architecture**, with a focus on keeping AI capabilities integrated with conventional backend engineering practices.
