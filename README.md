# agentic-test-automation
Agentic Test Automation Codebase

This template integrates:

- **LangChain**: For building LLM-powered agents.  
- **Playwright**: For browser automation and E2E testing.  
- **OpenAI GPT-4**: As the language model for generating test scripts.  
- **LangGraph**: For orchestrating agent workflows.

Important: This project is set up for development with MacOS. You will need pip 25.0+ installed locally!

## Clone the Repository
Get started on your local machine by cloning the repository:
```shell
git clone https://github.com/nickbaynham/agentic-test-automation.git
cd agentic-test-automation.git
```

## Running the Application
This workflow will install any tools and dependencies needed. You will at least need to have Python 3.10+ and the pip package manager installed.
```shell
make
```
# Setting up a Repository Similar to this one
These steps are not necessary for this repo, but are provided in case you want to create a repository and need the steps to initialize the settings with the package manager.
## Perform the Init Step
For this, you will run the pdm command and answer the prompts which will result in the init of the environment for this project directory:
```shell
pdm init
```

## Add the dependencies
Add the dependencies needed for the application:
```shell
pdm add langchain openai playwright langgraph
```
Add dev/test dependencies:
```shell
pdm add --dev pytest ruff
pdm add --dev black mypy
pdm add typer rich
```
Verify with:
```shell
pdm list
```
