# 💹 AI Finance Tracker

An AI-powered Finance Tracking and Analytics application built using **Python**, **Streamlit**, and **Groq LLM**. This tool enables users to upload CSV and Excel financial datasets, analyze spending patterns, generate interactive visualizations, and chat with an intelligent AI assistant for financial insights.

---

## 🚀 Overview

Managing finances can be overwhelming when dealing with large spreadsheets and transaction records. AI Finance Tracker simplifies financial analysis by combining data visualization, automated insights, and conversational AI into a single dashboard.

Simply upload your financial data and let AI help you understand your spending habits, income trends, savings opportunities, and financial performance.

---

## ✨ Features

### 📂 File Upload & Processing

* Upload CSV files
* Upload Excel (.xlsx) files
* Automatic data parsing and cleaning
* Supports large financial datasets

### 📊 Financial Analytics Dashboard

* Expense Analysis
* Income Analysis
* Category-wise Spending Breakdown
* Monthly Financial Trends
* Cash Flow Monitoring
* Budget Tracking

### 📈 Interactive Visualizations

* Bar Charts
* Line Charts
* Pie Charts
* Spending Distribution Graphs
* Income vs Expense Comparison
* Monthly Trend Analysis

### 🤖 AI Financial Assistant

Powered by **Groq API**

Ask questions such as:

* "Where am I spending the most money?"
* "What are my highest expenses this month?"
* "How can I improve my savings?"
* "Summarize my financial data."
* "Identify unusual transactions."

The AI analyzes uploaded data and provides intelligent insights in natural language.

### 🔍 Smart Insights

* Spending pattern detection
* Expense categorization
* Budget recommendations
* Financial summaries
* Trend identification
* Data-driven suggestions

---

## 🛠️ Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core Development     |
| Streamlit  | Frontend & Dashboard |
| Groq API   | AI-Powered Analysis  |
| Pandas     | Data Processing      |
| NumPy      | Numerical Operations |
| Plotly     | Interactive Charts   |
| Matplotlib | Data Visualization   |
| OpenPyXL   | Excel File Handling  |

---

## 📂 Project Structure

```bash
AI-Finance-Tracker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_finance_data.csv
│
├── uploads/
│   └── uploaded_files
│
├── utils/
│   ├── data_processor.py
│   ├── visualizer.py
│   ├── ai_assistant.py
│   └── insights.py
│
├── assets/
│   └── images
│
└── charts/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Finance-Tracker.git
cd AI-Finance-Tracker
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the value with your Groq API key.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will launch locally at:

```bash
http://localhost:8501
```

---

## 📊 Supported Data Formats

### CSV Example

```csv
Date,Category,Description,Amount
2025-01-01,Food,Restaurant,-500
2025-01-03,Salary,Monthly Salary,50000
2025-01-05,Transport,Cab,-250
```

### Excel Example

| Date       | Category  | Description    | Amount |
| ---------- | --------- | -------------- | ------ |
| 01-01-2025 | Food      | Restaurant     | -500   |
| 03-01-2025 | Salary    | Monthly Salary | 50000  |
| 05-01-2025 | Transport | Cab            | -250   |

---

## 🎯 Use Cases

* Personal Finance Management
* Expense Tracking
* Budget Monitoring
* Financial Reporting
* Spending Analysis
* Savings Planning
* Business Expense Analysis
* Cash Flow Monitoring

---

## 🔮 Future Enhancements

* Multi-User Authentication
* Cloud Database Integration
* AI Budget Planner
* Investment Tracking
* Financial Goal Management
* Automated Expense Categorization
* PDF Report Generation
* Email-Based Monthly Reports
* Real-Time Bank Data Integration

---

## 📸 Application Workflow

1. Upload CSV or Excel file
2. Data is processed and cleaned
3. Financial metrics are generated
4. Interactive charts are displayed
5. AI analyzes financial patterns
6. Users interact with the AI assistant
7. Personalized insights and recommendations are provided

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed with ❤️ using **Python**, **Streamlit**, and **Groq AI** to make financial analysis smarter, faster, and more accessible.

---

### ⭐ If you found this project helpful, please consider giving it a star on GitHub!
