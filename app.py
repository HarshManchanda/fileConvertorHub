import streamlit as st
import pandas as pd
import json
import xml.etree.ElementTree as ET
from io import StringIO, BytesIO
import openpyxl
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Smart File Converter Hub",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .converter-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Helper Functions
def csv_to_json(file):
    """Convert CSV to JSON"""
    try:
        df = pd.read_csv(file)
        json_data = df.to_json(orient='records', indent=2)
        return json_data, None
    except Exception as e:
        return None, str(e)

def json_to_csv(file):
    """Convert JSON to CSV"""
    try:
        json_data = json.load(file)
        df = pd.DataFrame(json_data)
        csv_data = df.to_csv(index=False)
        return csv_data, None
    except Exception as e:
        return None, str(e)

def excel_to_json(file):
    """Convert Excel to JSON"""
    try:
        df = pd.read_excel(file)
        json_data = df.to_json(orient='records', indent=2)
        return json_data, None
    except Exception as e:
        return None, str(e)

def xml_to_json(file):
    """Convert XML to JSON"""
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        
        def element_to_dict(element):
            result = {}
            # Add attributes
            if element.attrib:
                result['@attributes'] = element.attrib
            
            # Add text content
            if element.text and element.text.strip():
                if len(element) == 0:  # No children
                    return element.text.strip()
                else:
                    result['#text'] = element.text.strip()
            
            # Add children
            children = {}
            for child in element:
                child_data = element_to_dict(child)
                if child.tag in children:
                    if not isinstance(children[child.tag], list):
                        children[child.tag] = [children[child.tag]]
                    children[child.tag].append(child_data)
                else:
                    children[child.tag] = child_data
            
            result.update(children)
            return result if result else None
        
        data = {root.tag: element_to_dict(root)}
        json_data = json.dumps(data, indent=2)
        return json_data, None
    except Exception as e:
        return None, str(e)

def csv_to_sql(file, table_name="my_table"):
    """Convert CSV to SQL INSERT statements"""
    try:
        df = pd.read_csv(file)
        
        # Generate CREATE TABLE statement
        sql_statements = []
        columns = []
        for col, dtype in df.dtypes.items():
            if dtype == 'int64':
                col_type = 'INTEGER'
            elif dtype == 'float64':
                col_type = 'DECIMAL(10,2)'
            else:
                col_type = 'VARCHAR(255)'
            columns.append(f"    {col} {col_type}")
        
        create_table = f"CREATE TABLE {table_name} (\n" + ",\n".join(columns) + "\n);\n\n"
        sql_statements.append(create_table)
        
        # Generate INSERT statements
        for _, row in df.iterrows():
            values = []
            for val in row:
                if pd.isna(val):
                    values.append('NULL')
                elif isinstance(val, str):
                    # Escape single quotes
                    escaped_val = str(val).replace("'", "''")
                    values.append(f"'{escaped_val}'")
                else:
                    values.append(str(val))
            
            insert_stmt = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(values)});"
            sql_statements.append(insert_stmt)
        
        return '\n'.join(sql_statements), None
    except Exception as e:
        return None, str(e)

# Main App
def main():
    # Header
    st.markdown('<p class="main-header">🔄 Smart File Converter Hub</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Convert your files between multiple formats instantly</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("⚙️ Conversion Options")
    st.sidebar.markdown("---")
    
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type",
        [
            "CSV → JSON",
            "JSON → CSV",
            "Excel → JSON",
            "XML → JSON",
            "CSV → SQL"
        ]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📋 Supported Formats")
    st.sidebar.markdown("""
    - **CSV**: Comma-separated values
    - **JSON**: JavaScript Object Notation
    - **Excel**: .xlsx, .xls files
    - **XML**: Extensible Markup Language
    - **SQL**: SQL INSERT statements
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.info("Built with Streamlit • Python • Pandas")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 Upload File")
        
        # File uploader based on conversion type
        if conversion_type == "CSV → JSON":
            uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
            if uploaded_file:
                result, error = csv_to_json(uploaded_file)
                if error:
                    st.error(f"Error: {error}")
                else:
                    with col2:
                        st.markdown("### 📥 Download Result")
                        st.success("✅ Conversion successful!")
                        st.download_button(
                            label="📥 Download JSON",
                            data=result,
                            file_name=f"{uploaded_file.name.split('.')[0]}.json",
                            mime="application/json"
                        )
                        with st.expander("👁️ Preview Output"):
                            st.code(result, language='json')
        
        elif conversion_type == "JSON → CSV":
            uploaded_file = st.file_uploader("Choose a JSON file", type=['json'])
            if uploaded_file:
                result, error = json_to_csv(uploaded_file)
                if error:
                    st.error(f"Error: {error}")
                else:
                    with col2:
                        st.markdown("### 📥 Download Result")
                        st.success("✅ Conversion successful!")
                        st.download_button(
                            label="📥 Download CSV",
                            data=result,
                            file_name=f"{uploaded_file.name.split('.')[0]}.csv",
                            mime="text/csv"
                        )
                        with st.expander("👁️ Preview Output"):
                            st.code(result, language='text')
        
        elif conversion_type == "Excel → JSON":
            uploaded_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
            if uploaded_file:
                result, error = excel_to_json(uploaded_file)
                if error:
                    st.error(f"Error: {error}")
                else:
                    with col2:
                        st.markdown("### 📥 Download Result")
                        st.success("✅ Conversion successful!")
                        st.download_button(
                            label="📥 Download JSON",
                            data=result,
                            file_name=f"{uploaded_file.name.split('.')[0]}.json",
                            mime="application/json"
                        )
                        with st.expander("👁️ Preview Output"):
                            st.code(result, language='json')
        
        elif conversion_type == "XML → JSON":
            uploaded_file = st.file_uploader("Choose an XML file", type=['xml'])
            if uploaded_file:
                result, error = xml_to_json(uploaded_file)
                if error:
                    st.error(f"Error: {error}")
                else:
                    with col2:
                        st.markdown("### 📥 Download Result")
                        st.success("✅ Conversion successful!")
                        st.download_button(
                            label="📥 Download JSON",
                            data=result,
                            file_name=f"{uploaded_file.name.split('.')[0]}.json",
                            mime="application/json"
                        )
                        with st.expander("👁️ Preview Output"):
                            st.code(result, language='json')
        
        elif conversion_type == "CSV → SQL":
            uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
            table_name = st.text_input("Table Name", value="my_table", help="Enter the SQL table name")
            
            if uploaded_file and table_name:
                result, error = csv_to_sql(uploaded_file, table_name)
                if error:
                    st.error(f"Error: {error}")
                else:
                    with col2:
                        st.markdown("### 📥 Download Result")
                        st.success("✅ Conversion successful!")
                        st.download_button(
                            label="📥 Download SQL",
                            data=result,
                            file_name=f"{uploaded_file.name.split('.')[0]}.sql",
                            mime="text/plain"
                        )
                        with st.expander("👁️ Preview Output (First 20 lines)"):
                            preview_lines = '\n'.join(result.split('\n')[:20])
                            st.code(preview_lines, language='sql')
    
    # Instructions section
    st.markdown("---")
    st.markdown("### 📖 How to Use")
    
    instructions_col1, instructions_col2, instructions_col3 = st.columns(3)
    
    with instructions_col1:
        st.markdown("""
        #### Step 1: Select
        Choose your desired conversion type from the sidebar dropdown menu.
        """)
    
    with instructions_col2:
        st.markdown("""
        #### Step 2: Upload
        Upload your file using the file uploader. Supported formats are shown.
        """)
    
    with instructions_col3:
        st.markdown("""
        #### Step 3: Download
        Preview and download your converted file instantly!
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit | © 2025</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
