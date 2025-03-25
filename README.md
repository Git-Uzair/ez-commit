
# ez-commit

A Python-based CLI tool that  generates commit messages using an LLM (gemma3:1b) based on the staged files in your Git repository. 

## Motivation
Writing clear and concise commit messages is essential for tracking changes and maintaining code quality and developers would rather spend more time producing value than thinking of ways to minify and write a concise commit message, especially when the changes are complex. To solve this, we propose an AI-powered tool that uses LLMs to analyze git diff output and generate meaningful, concise commit messages. Also, this project would help me gain some hands on experience with Ollama and LLMs in general!

# Installation
- Have Docker and Python (3.6+) installed
- Clone the repo
- Navigate to the root of this repo

```bash
  $ docker-compose up -d
```
- After the Ollama container is up, run
```bash
  $ pip install --editable .
```
## Usage

```bash
my_dir/x_project$ git add .
my_dir/x_project$ ez-commit
Refactor: Improved code redeability (y/n) |
```

## Limitations/Potential Improvements
- For large diffs, the model may hallucinate and get overwhelmed by the input and give irrelevant commit message
- Could have a better system message or the model could have been modified using a custom Modelfile
- Add support to use any other LLM already in use by a potential user
- Refactor / Add better error and edge case handling
- Implement chat history to enable model to give more commit message suggestions if the first one wasn't chosen
- Use Langchain to have more control over message templates
## Feedback
- Tinker with context sizes to reduce hallucinations on larger input
- Smaller models require pretty explicit system messages, spend time fine tuning that
- 
