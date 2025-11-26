import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simple Data Explorer", layout="wide")

st.title("📊 Simple Data Explorer")

st.write(
    "Upload a CSV file to explore it with Pandas and interactive charts."
)

# 1. File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # 2. Read into pandas DataFrame
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading the file: {e}")
    else:
        st.success("File uploaded and read successfully!")

        # 3. Show first 5 rows
        st.subheader("👀 First 5 rows")
        st.dataframe(df.head())

        # 4. Descriptive statistics
        st.subheader("📐 Descriptive statistics (numeric columns)")
        st.dataframe(df.describe())

        # 5. Interactive graph view
        st.subheader("📈 Interactive chart")

        # Let user choose x and y columns
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        all_cols = df.columns.tolist()

        if len(numeric_cols) == 0:
            st.warning("No numeric columns found for plotting.")
        else:
            x_col = st.selectbox(
                "X-axis column",
                options=all_cols,
                index=0
            )
            y_col = st.selectbox(
                "Y-axis column (numeric)",
                options=numeric_cols,
                index=0
            )

            chart_type = st.radio(
                "Chart type",
                ["Line", "Bar", "Area"],
                horizontal=True,
            )

            plot_df = df[[x_col, y_col]].dropna()

            if chart_type == "Line":
                st.line_chart(plot_df, x=x_col, y=y_col)
            elif chart_type == "Bar":
                st.bar_chart(plot_df, x=x_col, y=y_col)
            elif chart_type == "Area":
                st.area_chart(plot_df, x=x_col, y=y_col)
else:
    st.info("👆 Upload a CSV file to get started.")
