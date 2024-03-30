# using pandas
def analyze_dataframe(df):
    # Initialize the result dictionary
    results = {
        'missing_data_per_row': {},
        'columns_analysis': {}
    }
    
    # Identify missing data per row
    results['missing_data_per_row'] = df.isnull().sum(axis=1).to_dict()
    
    # Analyze each column
    for column in df.columns:
        column_data = df[column]
        column_info = {
            'data_type': column_data.dtype.name,
            'distinct_values': column_data.dropna().unique().tolist()
        }
        
        # Determine if categorical or numerical
        if column_data.dtype.name in ['object', 'category', 'bool']:
            column_info['type'] = 'Categorical'
        else:
            # For numerical data, further identify binary or other types
            distinct_vals = column_info['distinct_values']
            if len(distinct_vals) == 2:
                column_info['type'] = 'Binary'
            else:
                column_info['type'] = 'Numerical'
        
        results['columns_analysis'][column] = column_info
    
    return results
