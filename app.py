# healthcare_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# APPLICATION CLASS
# ----------------------------------------
class PatientInsightsDashboard:

    def __init__(self):
        self.dataset = None
        self.numeric_columns = []
        self.filtered_data = None

    # ----------------------------------------
    # PAGE CONFIGURATION
    # ----------------------------------------
    def configure_application(self):
        st.set_page_config(
            page_title="Healthcare Analytics System",
            layout="wide"
        )
        st.title("🏥 Healthcare Analytics Dashboard")
        st.markdown("Analyze patient health metrics dynamically.")

    # ----------------------------------------
    # DATA LOADING
    # ----------------------------------------
    def load_dataset(self):
        file = st.file_uploader(
            "Upload Patient Dataset (Excel Format)",
            type=["xlsx"]
        )

        if file:
            self.dataset = pd.read_excel(file)
            return True
        return False

    # ----------------------------------------
    # DATA PREVIEW
    # ----------------------------------------
    def show_dataset_preview(self):
        st.subheader("📄 Dataset Overview")
        st.dataframe(self.dataset, use_container_width=True)
        st.write("Dataset Shape:", self.dataset.shape)

    # ----------------------------------------
    # IDENTIFY NUMERIC COLUMNS
    # ----------------------------------------
    def extract_numeric_columns(self):
        self.numeric_columns = self.dataset.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

    # ----------------------------------------
    # SIDEBAR FILTERS (40% COMPLETED)
    # ----------------------------------------
    def apply_basic_filters(self):

        st.sidebar.header("🔎 Filter Panel")

        self.filtered_data = self.dataset.copy()

        # Age Filter (if exists)
        if "Age" in self.dataset.columns:
            min_age = int(self.dataset["Age"].min())
            max_age = int(self.dataset["Age"].max())

            age_range = st.sidebar.slider(
                "Select Age Range",
                min_age,
                max_age,
                (min_age, max_age)
            )

            self.filtered_data = self.filtered_data[
                (self.filtered_data["Age"] >= age_range[0]) &
                (self.filtered_data["Age"] <= age_range[1])
            ]

        # Gender Filter (if exists)
        if "Gender" in self.dataset.columns:
            gender_options = self.dataset["Gender"].unique()
            selected_gender = st.sidebar.multiselect(
                "Select Gender",
                gender_options
            )

            if selected_gender:
                self.filtered_data = self.filtered_data[
                    self.filtered_data["Gender"].isin(selected_gender)
                ]

        st.sidebar.write("Filtered Records:", self.filtered_data.shape[0])

    # ----------------------------------------
    # METRIC SELECTION
    # ----------------------------------------
    def select_health_metric(self):
        if len(self.numeric_columns) > 0:
            return st.selectbox(
                "Select Health Metric for Analysis",
                self.numeric_columns
            )
        else:
            st.warning("No numeric columns available.")
            return None

    # ----------------------------------------
    # MAIN DASHBOARD SECTION
    # ----------------------------------------
    def build_dashboard(self):

        selected_metric = self.select_health_metric()

        if selected_metric:

            st.markdown("## 📊 Analytical Dashboard")

            # ----------------------------------------
            # STUDENTS COMPLETE FROM HERE (60%)
            # --------------------------------------
            col1,col2=st.columns(2)
            col3,col4=st.columns(2)
            col5,col6=st.columns(2)
            #bar chart
            with col1:
                x=self.filtered_data["Gender"]
                y=self.filtered_data[selected_metric]
                plt.figure()
                plt.bar(x,y)
                plt.title("Bar Chart")
                st.pyplot(plt)
            #pie chart
            with col2:
                labels=["Low Risk","Medium Risk","High Risk"]
                values=[30,20,20]
                plt.figure()
                plt.pie(values,labels=labels,autopct="%1.1f%%")
                st.pyplot(plt)
            #Histogram with kDE
            with col3:
                plt.figure()
                sns.histplot(self.filtered_data,kde=True)
                plt.title("Histogram Plot")
                st.pyplot(plt)
            #Box plot for outlier ditection
            with col4:
                plt.figure()
                sns.boxplot(x="Gender",y="Sugar_Level",data=self.filtered_data)
                plt.title("Box plot")
                st.pyplot(plt)
            with col5:
                x=["Heart_Rate"]
                y=["Risk_Category"]
                plt.figure()
                plt.scatter(x,y,data=self.filtered_data)
                plt.title("scatter plot")
                plt.xlabel("HeartRate")
                plt.ylabel("RiskCategory")
                st.pyplot(plt)
            with col6:
                x=self.filtered_data["Gender"]
                y=self.filtered_data["Cholesterol"]
                plt.figure()
                plt.plot(x,y,data=self.filtered_data)
                plt.xlabel("Gender")
                plt.ylabel("Cholesterol")
                st.pyplot(plt)
                #KPI Metric Section
                st.subheader("KPI Matrix")
                mean=self.filtered_data[selected_metric].mean()
                max=self.filtered_data[selected_metric].max()
                min=self.filtered_data[selected_metric].min()
                standard_value=self.filtered_data[selected_metric].std()
                k1,k2,k3,k4=st.columns(4)
                k1.metric("Mean",round(mean,2))
                k2.metric("Maximum",round(max,2))
                k3.metric("Minimum",round(mean,2))
                k4.metric("std Deviation",round(standard_value,2))
                #correlation Heatmap
                fig,x=plt.subplots(figsize=(8,5))
                correlation=self.filtered_data[self.numeric_columns].corr()
                sns.heatmap(correlation,annot=True,cmap="coolwarm")
                st.pyplot(plt)
                #Health Insights
                high_risk=self.filtered_data[self.filtered_data["Risk_Category"]=="High"].shape[0]
                total=self.filtered_data.shape[0]
               
               # st.write(f"1] Total Patients Analyzed:{total}")
                # st.write(f"2] High Risk Patients:{high_risk}")
               # st.write(f"3] Average{selected_metric}:{round(mean,2)}")
                # st.write(f"4] Boxplot shows presence of possible outliers.")
               # st.write(f"5] Heatmap shows relationship among BMI,Sugar,BP,etc.")




            



                
                
            # TASK 1:
            # Create a 2x2 layout using st.columns()

            # Example:
            # col1, col2 = st.columns(2)

            # TASK 2:
            # Build Bar Chart (Matplotlib)
            # Use self.filtered_data

            # TASK 3:
            # Build Pie Chart

            # TASK 4:
            # Build Histogram with KDE (Seaborn)

            # TASK 5:
            # Build Boxplot for Outlier Detection

            # TASK 6:
            # Add KPI Metrics:
            # - Mean
            # - Max
            # - Min
            # - Standard Deviation

            # TASK 7:
            # Add Correlation Heatmap (Bonus)

            # TASK 8:
            # Add Health Insight Summary Section
            # Write 3–5 observations based on filtered data

            pass


# ----------------------------------------
# APPLICATION EXECUTION
# ----------------------------------------
def main():

    dashboard = PatientInsightsDashboard()
    dashboard.configure_application()

    if dashboard.load_dataset():
        dashboard.show_dataset_preview()
        dashboard.extract_numeric_columns()
        dashboard.apply_basic_filters()
        dashboard.build_dashboard()
    else:
        st.info("Please upload an Excel dataset to begin analysis.")


if __name__ == "__main__":
    main()
    