# using pandas
def analyze_dataframe(df):
    # Prepare the DataFrame for the analysis results
    analysis_df = pd.DataFrame(index=df.columns, columns=[
        'Data Type', 'Column Type', 'Missing Data Count', 'Distinct Values Count', 'First 5 Distinct Values'
    ])
    
    # Fill in the analysis results
    for column in df.columns:
        data_type = df[column].dtype.name
        distinct_values = df[column].dropna().unique()
        distinct_values_count = len(distinct_values)
        first_5_values = ', '.join([str(v) for v in distinct_values[:5]])
        
        analysis_df.loc[column, 'Data Type'] = data_type
        analysis_df.loc[column, 'Missing Data Count'] = df[column].isnull().sum()
        analysis_df.loc[column, 'Distinct Values Count'] = distinct_values_count
        analysis_df.loc[column, 'First 5 Distinct Values'] = first_5_values
        
        # Determine column type
        if data_type in ['object', 'category', 'bool']:
            analysis_df.loc[column, 'Column Type'] = 'Categorical'
        else:
            if distinct_values_count == 2:
                analysis_df.loc[column, 'Column Type'] = 'Binary'
            else:
                analysis_df.loc[column, 'Column Type'] = 'Numerical'
    
    return analysis_df
