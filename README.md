# Data_Cleaning_Tool
This Data cleaning tool is a library of python function used to for data cleaning and transformation.

transform_numeric_to_text(df) - This function Transform numeric columns to text in any pandas DataFrame.

remove_duplicates_latest_year(df, year_column) - This functionn will remove duplicate rows keeping the latest year. You need
to assign pandas dataframe and also mention the year.

remove_outliers(df, column_name, z_score_threshold=1.5) - This function will remove outliers from a DataFrame using z-scores. You can assign your own z score threshold, the Z score threshold = 1.5 is not a default value

handle_missing_values(df) - For any dataframe, you can handle the missing values by replacing them with the appropriate. In this function currently, missing values in numeric columns are replaced with average value of the other values within the column and for
case of categorical column, the missing values are replaced with the most frequent value(mode) in the column

I have also added to more functions in this library which can be used to find out sale price trend and a function to keep to keep rows with largest LotFrontage for each LotArea.

