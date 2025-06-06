

📊 COVID-19 Tracker
A Python-based data analysis project that tracks COVID-19 cases, deaths, and trends across selected countries using real-world data from Our World in Data (OWID).

🎯 Objectives
Load and explore the OWID COVID-19 dataset.

Clean and preprocess the data for analysis.

Visualize trends in total cases and deaths over time.

Compare COVID-19 progression across different countries.

🛠 Tools & Libraries Used
Python 3

Pandas (Data manipulation & analysis)

Matplotlib (Basic plotting)

Seaborn (Enhanced visualizations)

Jupyter Notebook / VS Code (Development environment)

🚀 How to Run the Project
Clone the repository:

bash
git clone https://github.com/your-username/covid-19-tracker.git
cd covid-19-tracker
Install dependencies:

bash
pip install pandas matplotlib seaborn
Download the dataset (if not using automatic download):

Manually download owid-covid-data.csv and place it in the project folder.

Run the script:

bash
python Tracker.py
(Alternatively, use jupyter notebook to run interactively.)

📈 Key Features
Data Loading: Fetches and loads the latest COVID-19 dataset.

Data Cleaning: Handles missing values, filters countries, and converts data types.

Visualizations:

Line plots comparing total cases over time.

(Extendable to include deaths, vaccinations, etc.)

🔍 Example Output
Total COVID-19 Cases Over Time
(Screenshot of the generated Matplotlib plot)

🤔 Insights & Reflections
The dataset requires careful handling of missing values.

Trends vary significantly between countries due to testing policies, population density, and government responses.

Future improvements:

Add interactive Dash/Plotly visualizations.

Include vaccination data.

Deploy as a web app (Streamlit/Flask).

📂 File Structure
covid-19-tracker/
├── Tracker.py          # Main Python script
├── README.md           # Project documentation
├── owid-covid-data.csv # Dataset (manually downloaded)
└── requirements.txt    # Dependencies (optional)

