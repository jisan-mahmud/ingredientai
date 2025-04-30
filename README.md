# IngredientAI: Personalized Recipe Generator

**IngredientAI** is a web application that generates personalized recipe suggestions based on user preferences using the **Gemini API**. Built with **Django** for the backend and **Tailwind CSS** for the frontend, IngredientAI offers a seamless, responsive, and visually appealing experience.

---

## Features

- **Personalized Recipe Suggestions**: Powered by the **Gemini API**, IngredientAI provides recipe ideas based on user input.
- **User-friendly Interface**: Built with **Tailwind CSS** for a clean, responsive design.
- **Easy Search**: Users can search for recipes based on ingredients, cuisine, or dietary preferences.
- **Dynamic Content**: Real-time recipe suggestions based on the latest data from the Gemini API.

---

## Technologies Used

- **Django**: Backend framework for building the web application.
- **Tailwind CSS**: For responsive, modern, and customizable frontend design.
- **Gemini API**: API for fetching recipe data based on user input.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/IngredientAI.git
   cd IngredientAI
   ```

2. **Set up a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Gemini API**:
   - Obtain an API key from the [Gemini API](https://geminiapi.com/).
   - Add the key to your environment variables or Django settings.

5. **Run the application**:
   ```bash
   python manage.py runserver
   ```
