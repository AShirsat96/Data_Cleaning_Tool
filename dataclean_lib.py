class mydataclean:

    import pandas as pd
    import numpy as np

    def _init_(self):
        print("my library initiaklised")
        
    def transform_numeric_to_text(df):
        # Code to transform numeric columns to text
        """
        Transform numeric columns to text in a pandas DataFrame.
        
        Parameters:
            df (pd.DataFrame): The DataFrame to transform.
        
            
        Returns:
            pd.DataFrame: Transformed DataFrame with numeric columns converted to text.
            
        """
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].astype(str)
        return df
    
    def remove_duplicates_latest_year(df, year_column='YearBuilt'):
        # Code to remove duplicate rows keeping the latest year
        """
        Remove duplicate rows keeping the latest year.
        
        Parameters:
            df (pd.DataFrame): The DataFrame to process.
            year_column (str): The column that contains the year.
            
        Returns:
            pd.DataFrame: DataFrame with duplicates removed.
        """
        # Sort DataFrame by 'YearBuilt' in descending order
        df.sort_values(by='YearBuilt', ascending=False, inplace=True)
        # Keep only the first occurrence of each 'Id' (latest year)
        df.drop_duplicates(subset='Id', keep='first', inplace=True)
        # Sort DataFrame by index to revert to the original order
        df.sort_index(inplace=True)
        return df
    
    def remove_outliers(df, column_name, z_score_threshold=1.5):
        """
        Remove outliers from a DataFrame using z-scores.
        
        Parameters:
            df (pd.DataFrame): The DataFrame to process.
            column_name (str): The column containing the values to check for outliers.
            z_score_threshold (float): The z-score threshold for outlier detection.
            
        Returns:
            pd.DataFrame: DataFrame with outliers removed.
        """
        q1 = df[column_name].quantile(0.25)
        q3 = df[column_name].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - z_score_threshold * iqr
        upper_bound = q3 + z_score_threshold * iqr
        df = df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
        return df
    
    
    def handle_missing_values(df):
        # Code to handle missing values by filling with appropriate values
        # Fill numeric columns with average value
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        
        # Fill categorical columns with most frequent value
        categorical_cols = df.select_dtypes(include=['object']).columns
        df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
        return df
        
    
    def handle_multiple_lotfrontage(df, lot_area_column, lot_frontage_column):
        # Code to keep rows with largest LotFrontage for each LotArea
        # Create a DataFrame with the largest LotFrontage for each unique LotArea
        largest_lotfrontage_df = df.groupby(lot_area_column)[lot_frontage_column].max().reset_index()
        
        # Merge the largest LotFrontage values back into the original DataFrame
        result_df = df.merge(largest_lotfrontage_df, on=[lot_area_column, lot_frontage_column], how='inner')
        return result_df
    
    def check_saleprice_trend(df, year_column, class_column, price_column):
        # Code to check SalePrice trend over the years for each MSSubClass
        df_sorted = df.sort_values(by=[class_column, year_column])
        df_sorted['PriceTrend'] = df_sorted.groupby(class_column)[price_column].diff().gt(0).astype(int)
        df_sorted['PriceReversed'] = df_sorted.groupby(class_column)['PriceTrend'].diff().lt(0)
        
        reversed_years = df_sorted[df_sorted['PriceReversed']].groupby(class_column).agg({year_column: 'min'}).reset_index()
        
        result_df = df_sorted.merge(reversed_years, on=class_column, how='left')
        
        return result_df
        
    
    # Add code for displaying progress bar, error messages, etc.
