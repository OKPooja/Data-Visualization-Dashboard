# Data Visualization Dashboard

Data Visualization Dashboard is a web application developed using Django as the backend framework and D3.js for creating interactive and visually appealing charts. This dashboard allows users to gain valuable insights from visualized data and customize their views with multiple filters.

## Features

- **Django Backend**: Developed using Django to handle backend functionalities and data management.
- **Data Storage**: Utilized SQLite database to store data provided in JSON format.
- **Interactive Charts**: Incorporated D3.js library to create dynamic and interactive charts.
- **Customizable Filters**: Implemented multiple filters to enable users to customize and refine data according to their preferences.
- **User Insights**: Users can gain valuable insights from the visualized data.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JS
- **Charts**: D3.js
- **Database**: SQLite

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/OKPooja/DataVisualizationDashboard.git
    ```

2. Navigate to the project directory:
    ```bash
    cd DataVisualizationDashboard
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Access the dashboard by navigating to `http://127.0.0.1:8000` in your web browser.
2. Dummy json data is present in home\views.py. You just have to uncomment save_data() function once to enter the data in your database.
3. Use the interactive filters to customize and refine your data view.
4. Explore various charts and visualizations to gain insights.
   
(Note: Don't forget to comment the save_data() function after you have called it once. Otherwise, your database will have redundant entries)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

