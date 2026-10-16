Health Pal 🩺

A personal health companion that grows with you.

Health Pal is a personal health tracking application designed to help people manage their health and fitness through everyday conversations, structured tracking, and personalized progress insights.

The goal is to build an application that feels like a supportive companion rather than a collection of forms.

This project is also a hands-on learning journey in Python, application development, databases, AI, and eventually agentic AI.

🎯 Vision

Health Pal aims to:

* Turn everyday conversations into structured health records.
* Track workouts, nutrition, medication, and menstrual cycles.
* Understand personal goals and encourage accountability.
* Identify trends and highlight areas that need attention.
* Adapt its conversational personality to the user’s preferences.
* Provide personalized insights based on recorded information.

Core idea: Conversation is the primary interface, structured data is the memory, and progress insights provide the intelligence.

✨ Planned Features

1. Home — Conversational Companion

* Daily check-ins.
* Discuss goals and challenges.
* Plan the next day.
* Capture relevant health information from conversations.

2. Workout Tracking

* Exercise names, sets, repetitions, and weights.
* Workout duration and cardio.
* Workout history and exercise progression.

3. Nutrition Tracking

* Meals, foods, and portion sizes.
* Calories and protein.
* Daily nutrition summaries.
* Food and drink logging.

4. Medication Tracking

* Medication names, doses, and schedules.
* Medication history.
* Reminders and taken/not-taken records.

5. Menstrual Cycle Tracking

* Period dates and cycle history.
* Symptoms, energy, mood, and cravings.
* Connections between recorded cycle information and personal trends, without assuming every symptom has the same cause.

6. Progress and Insights

* Weight and fitness trends.
* Workout consistency.
* Nutrition summaries.
* Achievements and areas for improvement.
* Suggested next steps based on recorded information.

7. Personalization

* Profile and preferences.
* Configurable conversational styles, such as supportive friend, witty companion, or strict gym trainer.
* Relevant features based on the user’s preferences.

🛠️ Technology Stack

Technology	Purpose
Python	Application logic
Streamlit	User interface
SQLite	Local database
Git	Version control
GitHub	Source code hosting
LLMs and agentic AI	Planned future capabilities

🏗️ Architecture

The initial architecture is intentionally simple:

              Health Pal
                  |
              Streamlit UI
                  |
          Application Logic
                  |
             Database Layer
                  |
                SQLite
                  |
       Local Health Information

The architecture will evolve as the application grows.

Future versions may introduce an AI conversation layer, structured health-data extraction, planning capabilities, APIs, and multi-user support.

🚧 Development Roadmap

* Create the initial project.
* Set up Python and a virtual environment.
* Install and run Streamlit.
* Create the initial Health Pal interface.
* Add navigation between the main feature pages.
* Create the initial profile form.
* Introduce Streamlit session state for profile data.
* Create database.py.
* Add an initial SQLite connection function.
* Create database tables.
* Save and retrieve profile information from SQLite.
* Make profile information persist after browser refreshes and app restarts.
* Implement workout tracking.
* Implement nutrition tracking.
* Implement medication tracking.
* Implement menstrual cycle tracking.
* Build the progress dashboard.
* Add configurable conversation styles.
* Introduce AI-powered conversation and health-data extraction.
* Explore agentic AI capabilities.
* Prepare the architecture for future multi-user support.

The roadmap reflects planned work, not a claim that unfinished features already exist.

📂 Current Project Structure

health_tracker_agent/
├── app.py
├── database.py
└── README.md

Additional files will be added as the project develops.

🚀 Running the Application

Prerequisites

* Python 3.12 or a compatible Python version.
* Streamlit installed in your Python environment.

Start the application

Activate the project’s virtual environment, then run:

streamlit run app.py

Streamlit will provide a local address where the application can be opened in your browser.

🔒 Privacy

The initial version is designed to run locally.

As the application develops, care will be taken to keep personal health records, database files, credentials, and other private information out of the public source repository.

AI integrations and any future data-sharing features will require additional privacy considerations.

📚 Learning Objectives

This project provides practical experience with:

* Python application development.
* Modular code organization.
* Database design and SQL.
* Data persistence and CRUD operations.
* Git and GitHub workflows.
* AI-assisted application development.
* LLM integration and structured data extraction.
* Agentic AI architecture.
* Privacy-conscious software design.

📈 Development Log

Phase 1 — Application Foundation

Status: In progress

Completed:

* Created the project and Python virtual environment.
* Installed Streamlit.
* Built the initial application interface.
* Added navigation for the main health-tracking modules.
* Created a profile form with name and gender fields.
* Introduced session state for temporary profile storage.
* Created the initial database connection function.

Current limitation:

* Profile data is still stored in session state rather than permanently in the database.
* SQLite tables and database-backed profile storage have not yet been implemented.

Next milestone: Build the database schema and connect profile creation and retrieval to SQLite.

⸻

Health Pal is a work in progress. The aim is to build the foundation carefully, learn at every stage, and add more advanced capabilities as the application matures.