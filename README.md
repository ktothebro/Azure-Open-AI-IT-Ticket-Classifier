# Azure-Open-AI-IT-Ticket-Classifier

**IT Ticket Classifier Beginner Project**  
Uses Azure OpenAI and related Azure tools to automatically classify IT support tickets and assist in routing and decision-making.

---

## 🎯 Objective

Automatically classify IT support tickets into categories:

- 🖥️ Hardware  
- 🌐 Network  
- 💾 Software  
- 🔐 Account Access  
- 📦 Other  

...and route or log them using automation tools.

---

## 🧱 Tech Stack Used

| Tool/Service          | Purpose                                               |
|-----------------------|-------------------------------------------------------|
| **Azure OpenAI**      | Text classification using GPT-3.5 / GPT-4             |
| **Azure Logic Apps**  | Workflow automation (e.g., ticket routing)            |
| **Power Apps**        | *(Optional)* Form-based UI for submitting tickets     |
| **Azure SQL / Blob**  | Store classified ticket logs and messages             |

---

## 🪜 How It Works – Step-by-Step

### 🔹 1. User Submits a Support Request
Submitted via:
- Email
- Power Apps form
- Webhook or other Logic App trigger

---

### 🔹 2. Logic App or API Receives the Ticket
The request body includes a plain-text description of the issue.

---

### 🔹 3. Azure OpenAI Classifies the Ticket
A prompt is sent to GPT using the Azure OpenAI API.

---

## 📂 Project Structure

```plaintext
azure_ai_foundry_starter/
├── .env                  # API keys and endpoint configuration
├── main.py               # Entry point to run classifier
├── azure_ai_client.py    # Azure OpenAI wrapper
├── tasks/
│   └── classify.py       # Ticket classification logic
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore .env and cache files
└── README.md             # This file
