Poverty and Community Support in Washington State

Overview
In this project, we are attempting to identify the top three counties in Washington that could benefit from a community support hub. We will use data from the IRS, Census, and a HUD ZIP Code-to-County crosswalk to evaluate poverty and the variables that contribute to it, identify where nonprofits are in Washington, and gather background information about the community needs of Washington State. An ML clustering model will be used to cluster counties based on similar characteristics and help determine which counties could benefit from additional support.

Business Problem
ABC Community Support is a nationwide nonprofit organization looking to expand its services into Washington State. The board has asked the Data Team to recommend the top three counties that could benefit most from adding community support hubs. They are also seeking background information on Washington, its community needs, and its current community support.

Project Question
What three counties in Washington State could potentially benefit from the addition of a community support hub?

Data Sources
•	IRS Exempt Organizations Business Master File Extractor (EO BMF) – Washington (Publicly Accessible) – This dataset provides nonprofit information used to help determine what nonprofit support exists in Washington and where it is located.
•	U.S. Census Bureau American Community Survey (ACS) S1701 Poverty Status in the Past 12 Months (Publicly Accessible) – This dataset provides community-level information and demographic measures used to help identify counties that may benefit from additional support.
•	HUD-USPS ZIP Code Crosswalk Files (Free access through a created account) – This dataset provides the crosswalk needed to connect nonprofit ZIP Codes to Washington State counties.

Data Preparation
Data Cleaning
•	Cleaned the IRS nonprofit data.
•	Standardized ZIP Code formatting so it could be joined with the HUD crosswalk.
•	Removed or excluded records and columns that were not needed for the analysis.
•	Cleaned the Census data and selected the county-level variables needed for the project.
•	Extracted the county FIPS/County_ID from the HUD GEOID.
•	Renamed columns were needed to make the datasets consistent.
Data Integration
•	Joined the IRS nonprofit data with the HUD ZIP-to-county crosswalk to associate nonprofits with Washington counties.
•	Aggregated nonprofit records to determine nonprofit support at the county level.
•	Combined the nonprofit information with the Census community-need data using County_ID.
Preparation for Machine Learning
•	Selected the three community-need variables used by the K-Means model:
o	Poverty_Percent
o	Unemployment_percent
o	Did_Not_Graduate_percent
•	Standardized these variables using StandardScaler before applying K-Means.

Machine Learning Approach
For this project, I used a K-Means unsupervised clustering algorithm. Originally, I planned to use a Random Forest Regression model, but this was changed after reviewing the available data. Because I was working with counties within a single state, I only had 39 counties of data to use. If I were to divide this data into training and testing sets, the resulting sets would be very small and may not yield reliable results given the limited data available. By switching to an unsupervised clustering model, I was able to use all 39 counties to identify groups with similar characteristics.

The clustering model used variables associated with community needs to group counties with similar characteristics. The variables used were poverty, educational attainment, and unemployment percentages. Before the clusters were formed, StandardScaler was applied to the selected variables to ensure that each feature had a comparable influence on the model. After evaluating the model using different numbers of clusters and comparing the Silhouette scores, I ultimately selected four clusters because they produced the highest Silhouette score.
Model Evaluation

To evaluate the model used in this project, I used the Silhouette Score, Davies-Bouldin Index, and Calinski-Harabasz Index. All three measures were used to evaluate models with 2, 3, 4, 5, and 6 clusters.

The Silhouette Score was originally used to help determine how many clusters to use for the model and was later used as one of the measures to evaluate the final clustering. Four clusters performed the best according to the Silhouette Score, with a score of 0.421. This was the highest Silhouette Score among the tested cluster sizes.

The Davies-Bouldin Index was used to compare each cluster with its most similar counterpart. Lower scores indicate better separation between clusters. The Davies-Bouldin evaluation showed that 6 clusters yielded the best score of 0.573, while 4 clusters had a score of 0.758. This indicates that 6 clusters performed better according to this evaluation measure.

Lastly, the Calinski-Harabasz Index was used to assess the separation and compactness of the clusters. The index showed that 6 clusters had the highest score at 41.053, while 4 clusters had a score of 40.365. Although 6 clusters performed better on this measure, the difference between the scores for the 4- and 6-cluster cases was relatively small.

After reviewing the results from all three evaluation methods, I decided that 4 clusters were the best option for this project. While the Davies-Bouldin and Calinski-Harabasz measures suggested that 6 clusters would yield stronger clustering, 6 clusters resulted in a lower Silhouette Score. Selecting 4 clusters also provided a more manageable number of groups for interpreting and communicating the results to the board. Therefore, 4 clusters provided the best overall balance between the evaluation measures and the project's goal of identifying counties with similar community-need characteristics.

Results
After running the model, the counties were divided into four clusters. The clusters were then examined and compared using the counties' community-need variables to determine which characteristics each cluster represented. To do this, the community needs variables averaged for each cluster to provide an overall view of what each cluster represents. Based on these averages, the clusters were ordered from highest to lowest community need as follows: Cluster 0, Cluster 3, Cluster 2, and Cluster 1.

To more formally compare the counties across the three community-need variables, a Needs Score was created by combining the standardized community-need measures. This provided a single score that could be used to compare overall community need across the counties rather than evaluating each variable separately.

Next, a Support Gap Score was developed to identify counties with fewer nonprofits per capita. This was calculated using the People_Per_Nonprofit variable. People_Per_Nonprofit was created to compare the number of nonprofits relative to county population and reduce the effects of differences in county population sizes. StandardScaler was then used to standardize this measure so it could be combined with the Needs Score. A higher Support Gap Score represents a larger number of people per nonprofit and, therefore, a greater potential gap in nonprofit support.
Lastly, the Final Score was created by combining the Needs Score and Support Gap Score. Both scores were given equal weight at 50% because neither was considered more important than the other. Counties were then ranked from highest to lowest by Final Score. A higher Final Score indicates that a county has higher community-need indicators combined with a larger potential gap in nonprofit support.

After calculating the Final Score, the three counties identified as potentially benefiting from additional community support hubs were Yakima County, Grant County, and Franklin County.

Tableau Dashboard
The Tableau dashboard will present the project findings and provide the board with an interactive way to explore community needs and nonprofit support across Washington State.

Tools and Technologies
Programming/Development
•	Python – Used to access data, run the ML model, analyze the data, and evaluate the model results.
•	VS Code – Used to organize and manage the project files and code.
•	Jupyter Notebook – Used to clean, combine, and explore the data in preparation for analysis and modeling.
Python Libraries
•	Pandas – Used for data manipulation, cleaning, and analysis of the datasets in Jupyter Notebook and for reading datasets in the main programs.
•	NumPy – Used to support data manipulation, cleaning, and analysis in Jupyter Notebook.
•	Scikit-learn – Used to run the K-Means clustering model and StandardScaler.
•	Pytest – Used to test the data and analysis results for accuracy and completeness.
•	YData Profiling – Used to support exploratory data analysis (EDA) of the three datasets.
Machine Learning
•	K-Means – The unsupervised machine learning model used to group counties based on similar community-need characteristics.
•	StandardScaler – Used to standardize the variables passed into the model and to standardize the Support Gap Score.
•	Weights & Biases (W&B) – Used to track the machine learning experiment and model artifacts.
Data/Visualization
•	Tableau – Used to create visualizations and a dashboard for presenting the findings to the board.
Version Control
•	GitHub – Used to save and share code and perform version control.

Project Structure

Capstone project/
│
├── Analysis/
│   └── analyze_counties.py
│
├── Capstone Project Docs/
│   ├── Capstone_Displays.twb
│   ├── Data Dictionary.xlsx
│   ├── Project tracking.xlsx
│   └── Approval and release documents
│
├── Final_combined_data/
│   ├── final_combined_data.csv
│   ├── county_ml_results.csv
│   └── final_county_analysis.csv
│
├── ML/
│   ├── train_model.py
│   └── evaluate_model.py
│
├── Non-forprofit Data/
│   └── eo_wa.csv
│
├── Poverty Data/
│   ├── ACSST5Y2023.S1701-Column-Metadata.csv
│   ├── ACSST5Y2023.S1701-Data.csv
│   └── ACSST5Y2023.S1701-Table-Notes.txt
│
├── Zip-county cross walk/
│   └── hud_crosswalk.csv
│
├── tests/
│   └── capstone_test.py
│
├── .gitignore
├── app.py
├── capstone.ipynb
└── README.md

Folder Descriptions
•	Analysis/ – Contains the Python script used to analyze the county-level data and calculate the project metrics.
•	Capstone Project Docs/ – Contains project documentation, the data dictionary, proposal and approval documents, Tableau workbook, and project tracking files.
•	Final_combined_data/ – Contains the processed county-level datasets, machine learning results, final analysis, and top three county results.
•	ML/ – Contains the scripts used to train and evaluate the K-Means clustering model.
•	Non profit Data/ – Contains the original IRS nonprofit data used to identify nonprofit organizations and their locations in Washington State.
•	Poverty Data/ – Contains the original Census poverty dataset and supporting metadata used to identify county-level measures of community need.
•	Zip-county cross walk/ – Contains the HUD ZIP Code-to-county crosswalk used to connect nonprofit ZIP Codes to Washington State counties.
•	tests/ – Contains automated tests used to verify the completeness, accuracy, and consistency of the final county-level analysis and scoring results.
•	app.py – Contains the code used to retrieve the HUD ZIP Code-to-county crosswalk data.
•	capstone.ipynb – Contains exploratory data analysis and data preparation performed during the project.

Limitations
In this project, a few limitations should be kept in mind when reviewing the results and using them to make business decisions. First, there are only 39 counties in Washington State, which limits the amount of data available for machine learning and analysis, and makes more complex models less appropriate.

The next limiting factor is that the machine learning model uses the community-need variables available in the Census data. These include the percentage of individuals below the poverty line, the percentage of individuals in the workforce who are unemployed, and the percentage of adults age 25 and older who did not obtain a high school diploma or equivalent. While these are useful indicators of community need, many other variables that may contribute to poverty or community need were not available in the provided datasets. Therefore, the model indicates which counties may be experiencing greater need, but does not provide a complete picture of community need.

Another limiting factor is that the IRS provides data on the number of nonprofits in each county, their names, and their types. However, it does not specify the scope or amount of support that the nonprofits provide to the community. Therefore, the number of nonprofits in a county is not an exact measure of the amount of community support available.

A fourth limitation to keep in mind is that ZIP Codes can cross county boundaries. Nonprofit organizations were therefore assigned to counties based on the available HUD crosswalk rather than their exact service locations. This provides an estimate of where nonprofit organizations are located but does not identify their exact service locations or the geographic area they serve.

Understanding the limitations of this project is important when interpreting the results and using them to make business decisions. While there are limitations in the data sets and methodology, the analysis can still be used for its intended purpose. This project should be used to identify counties that may guarantee further consideration for additional support. It is intended to provide a starting point for the board when making decisions, rather than serving as the sole basis for selecting new community support hub locations.




