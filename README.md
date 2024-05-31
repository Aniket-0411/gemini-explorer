# Gemini Explorer

## Overview

Gemini Explorer is a project aimed at creating a user-friendly chat interface using Streamlit that connects with Google's state-of-the-art large language model, Gemini. This project serves as an educational and practical introduction to integrating large language models with intuitive interfaces.

## Mission Scenario

The goal is to provide an accessible platform for exploring and showcasing the capabilities of advanced language models. Follow the tasks outlined below to achieve this mission.

## Mission Workflow

### Task 1: 🌐 Enable Google Cloud

1. Go to the [Google Cloud Platform](https://cloud.google.com/) and select "Get Started for free".
2. Sign in using your Google Account and provide the necessary details to complete the billing requirements.
3. Accept the terms and conditions.
4. Complete the payment process to initialize your Google Cloud Account.
5. Create a new project (e.g., "RadicalX - Gemini Explorer").
6. Access the Google Cloud Console.
7. Navigate to Artificial Intelligence -> Vertex AI -> Enable All Recommended APIs.

### Task 2: 🧬 Google Cloud Initialization

1. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
2. Run the following command to initialize the SDK:
   ```sh
   gcloud init
   ```
3. Sign in using your Google Account credentials.
4. Select an existing project or create a new project.
5. (Optional) Set the default compute region and zone.

### Task 3: ☁️ Setting up Google Gemini

1. Install the Streamlit framework:
   ```sh
   pip install streamlit
   ```
2. Refer to the [Streamlit Documentation](https://docs.streamlit.io/) for implementation details.
3. Use the project ID instead of the project name to avoid permission issues in your code:
   ```python
   project = "project_id"
   ```

### Task 4: 📊 Streamlit Integration

1. Implement the steps outlined in the mission.
2. Run the Streamlit app:
   ```sh
   streamlit run filename.py
   ```

### Task 5: 🗣️ Adding Initial System Messages

Add initial system messages to guide users through the chat interface.

### Task 6: 📄 Preparing Submission

1. Create a GitHub repository for the project and include all project files.
2. Create a Loom video to represent the overall approach and provide the Loom link in the repository.

## Requirements

- Python 3.11x or above
- Streamlit
- Google Cloud account
- Vertex AI
