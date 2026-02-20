# HRMS-Assistant  
### AI-Ready HR Management System powered by FastMCP and Python

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Architecture](https://img.shields.io/badge/Architecture-Service%20Oriented-orange.svg)]()

Production-style Human Resource Management backend exposed as a Model Context Protocol (MCP) server, enabling AI agents to autonomously perform HR workflows such as employee onboarding, leave management, meeting scheduling, ticket creation, and email notifications.

This project demonstrates real-world AI system design patterns used in modern GenAI infrastructure.

---

# Architecture Overview

```
AI Agent / MCP Client
        │
        ▼
FastMCP Server (servers.py)
        │
        ├── Employee Manager
        ├── Leave Manager
        ├── Meeting Manager
        ├── Ticket Manager
        └── Email Service (SMTP)
```

This architecture enables AI agents to safely interact with enterprise systems via structured tools.

---

# Key Highlights

Agent-ready backend using Model Context Protocol (MCP)

Production-style modular service architecture

Autonomous onboarding workflow support

Schema validation using Pydantic

Email integration using SMTP

Fully extensible backend design

Portfolio-ready GenAI infrastructure project

Demonstrates enterprise AI system design patterns

---

# Features

## Employee Management

Create employees  
Retrieve employee details with fuzzy matching  
Maintain employee hierarchy  

## Leave Management

Apply leave  
Track leave balances  
View leave history  

## Meeting Management

Schedule meetings  
Track employee meetings  

## Ticket Management

Create onboarding tickets  
Create IT provisioning tickets  
Track ticket assignments  

## Email Integration

Send welcome emails  
Send onboarding notifications  
Send meeting invitations  

## MCP Tool Integration

Expose backend as structured tools callable by AI agents  

## Seeded Demo Data

Preloaded employee hierarchy  
Preloaded leave balances  
Preloaded tickets and meetings  

---

# Tech Stack

Language  
Python 3.12+

AI Integration  
FastMCP (Model Context Protocol)

Validation  
Pydantic

Environment Management  
python-dotenv

Email  
SMTP

Architecture  
Service-oriented modular backend

---

# Project Structure

```
HRMS-Assistant/
│
├── HRMS/
│   ├── employee_manager.py
│   ├── leave_manager.py
│   ├── meeting_manager.py
│   ├── ticket_manager.py
│   └── schemas.py
│
├── servers.py
├── emails.py
├── utils.py
├── main.py
├── pyproject.toml
└── .env
```

servers.py contains MCP server and tool definitions  
HRMS folder contains core HR business logic  
emails.py handles SMTP email sending  
utils.py seeds demo employee data  

---

# Installation

## Step 1: Clone repository

```
git clone https://github.com/MaheshPonnam6842/HRMS-Assistant.git
cd HRMS-Assistant
```

## Step 2: Create virtual environment

Windows

```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install dependencies

```
pip install -U pip
pip install "mcp[cli]>=1.17.0" python-dotenv pydantic
```

---

# Environment Setup

Create a `.env` file in root directory

```
EMAIL=your_email@gmail.com
EMAIL_PWD=your_app_password
```

If using Gmail, use an App Password instead of your normal password.

Never commit `.env` to GitHub.

---

# Running the MCP Server

Start the MCP server

```
python servers.py
```

The server runs using stdio transport and exposes HR tools to MCP clients and AI agents.

---

# Available MCP Tools

## Add employee

```
add_employee(emp_name, manager_id, email)
```

## Get employee details

```
et_employee_details(name)
```

## Create ticket

```
create_ticket(emp_id, item, reason)
```

## Send email

```
send_mail(subject, body, to_emails)
```

## Schedule meeting

```
schedule_meeting(employee_id, meeting_datetime, topic)
```

---

# Available MCP Prompts

## Apply leave

```
apply_leave(emp_id, leave_dates)
```

## Onboard employee

```
Onboard new employee(employee_name, manager_name)
```

This performs full onboarding workflow automatically.

---

# Example AI-Driven Workflow

AI agent performs autonomous onboarding:

Step 1: Creates employee record  
Step 2: Sends welcome email  
Step 3: Notifies manager  
Step 4: Creates onboarding tickets  
Step 5: Schedules introduction meeting  

All steps executed via MCP tools.

---

# Real-World Use Cases

Enterprise HR AI assistant

Autonomous onboarding agents

GenAI backend infrastructure

Tool calling system for AI agents

AI enterprise workflow automation

Portfolio project for AI Engineer, ML Engineer, and Data Scientist roles

---

# Scalability Roadmap

Add Postgres / Snowflake database integration

Add authentication and role-based access control

Deploy on AWS ECS / Kubernetes

Add REST API gateway

Add Slack and Teams integration

Add frontend dashboard

Add agent memory integration

---

# Why This Project Matters

This project demonstrates production-relevant AI system design patterns:

Agent tool calling architecture

Backend service modularization

Schema-validated structured tools

Enterprise workflow automation

AI-ready backend infrastructure

These patterns are used in real-world AI systems at companies like OpenAI, Microsoft, Google, and Amazon.

---

# Author

Mahesh Ponnam

GitHub  
https://github.com/MaheshPonnam6842

LinkedIn  
(Add your LinkedIn URL here)

---

# License

MIT License

---

# Support

If you found this useful, consider starring the repository.
