import pandas as pd
import streamlit as st
from validator import SalesSpreadsheet
from pydantic import ValidationError

def validate_data(df):
    errors = []
    validated_data = []
    
    for index, row in df.iterrows():
        try:
            # Convert the DataFrame row to a dictionary
            data = row.to_dict()
            
            # Validate the data using the SalesSpreadsheet model
            validated_user = SalesSpreadsheet(**data)
            validated_data.append(validated_user)
            
        except ValidationError as e:
            errors.append(f"Error in row {index + 2}: {str(e)}")
    
    return validated_data, errors

def main():
    st.set_page_config(layout="wide", page_title="Campaign Data Validator", initial_sidebar_state="expanded")

    # Aplicar dark mode via CSS
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Table Data Validator")
    st.write("Upload the CSV file for validation")
    
    uploaded_file = st.file_uploader("Choose a data", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        try:
            # Read the CSV file
            df = pd.read_csv(uploaded_file)
            
            st.write("Data preview:")
            st.dataframe(df.head())
            
            if st.button("Validate Data"):
                with st.spinner("Validating data..."):
                    validated_data, errors = validate_data(df)
                    
                    if errors:
                        st.error("Errors found during validation:")
                        for error in errors:
                            st.write(error)
                    else:
                        st.success("All data has been successfully validated!")
                        
                        # Show the number of validated records
                        st.write(f"Total validated records: {len(validated_data)}")
                        
                        # Option to download validated data
                        validated_df = pd.DataFrame([data.dict() for data in validated_data])
                        st.download_button(
                            label="Download validated data",
                            data=validated_df.to_csv(index=False),
                            file_name="validated_data.csv",
                            mime="text/csv"
                        )
                    
        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")

if __name__ == "__main__":
    main()


