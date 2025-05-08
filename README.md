# agentic-test-automation
Agentic Test Automation Codebase

A next-generation test automation framework powered by LLM agents. This project allows QA teams to define business workflows in plain English, and automatically generates, executes, and maintains browser-based end-to-end tests.

---

## 🚀 Features

- 🧠 LLM Agents for planning, generating, and fixing tests
- 🌐 Playwright for browser automation
- 🧪 Pytest for validating outcomes
- 📦 PDM for reproducible Python environments
- ✅ GitHub Actions for CI
- 💡 Simple Makefile to run everything

---

This template integrates:

- **LangChain**: For building LLM-powered agents.  
- **Playwright**: For browser automation and E2E testing.  
- **OpenAI GPT-4**: As the language model for generating test scripts.  
- **LangGraph**: For orchestrating agent workflows.

Important: This project is set up for development with MacOS. You will need pip 25.0+ installed locally!

## 🖥️ Getting Started (macOS)
Here's how to get started with the codebase if you're on a mac:
## 1. Clone the Repository
Get started on your local machine by cloning the repository:
```shell
git clone https://github.com/nickbaynham/agentic-test-automation.git
cd agentic-test-automation.git
```

## 2. Run the entire setup (installs PDM if missing)
This workflow will install any tools and dependencies needed. You will at least need to have Python 3.10+ and the pip package manager installed.
```shell
make all
```

This will:
- Install Python dependencies
- Install Playwright browsers
- Run the test agent system
- Lint and validate the codebase

# 📜 Example Workflow
Create a user story like:
```shell
As a user, I want to log in with a valid password and see the dashboard.
```

### Run the agents to automatically:

- Break down test steps
- Generate Playwright test code
- Run and validate the test
- Heal itself if UI elements break

# 🧪 Run Individual Steps
A reference of the individual steps you can run in the shell
```shell
make init               # Install dependencies
make install_browsers   # Install Playwright browser binaries
make run_agents         # Run LLM-powered agents
make test               # Run test suite
make lint               # Check style
make clean              # Clear cache
```

# 🛠️ Tools Used
| Tool       | Purpose                |
| ---------- | ---------------------- |
| PDM        | Python package manager |
| Playwright | E2E browser automation |
| LangChain  | LLM agent framework    |
| Pytest     | Test runner            |
| Ruff       | Python linter          |
| GitHub CI  | Continuous integration |

🧑‍💻 Contributing
Pull requests are welcome. Please lint your code before pushing:

```shell
make lint
```

# 🛠️ Setting up a Repository Similar to this one
These steps are not necessary for this repo, but are provided in case you want to create a repository and need the steps to initialize the settings with the package manager.

## 1. Perform the Init Step
For this, you will run the pdm command and answer the prompts which will result in the init of the environment for this project directory:

```shell
pdm init
```

## 2. Add the dependencies
Add the dependencies needed for the application:

```shell
pdm add langchain openai playwright langgraph
```

## 3. Add dev/test dependencies:

```shell
pdm add --dev pytest ruff
pdm add --dev black mypy
pdm add typer rich
```

## 4. Verify dependencies

```shell
pdm list
```
# 📄 License
MIT © NickBaynham