from fpdf import FPDF

# Create a PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Feasibility Study & Proposal", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 11)
        self.set_text_color(0)
        self.cell(0, 10, f"{title}", ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, body)
        self.ln()

# Create the document
pdf = PDF()
pdf.add_page()

pdf.chapter_title("Project Title:")
pdf.chapter_body("Dynamic Optimization of RO Plant Energy Consumption using Machine Learning")

pdf.chapter_title("Objective:")
pdf.chapter_body(
    "To develop a machine learning-based soft sensor that dynamically minimizes energy consumption (Ec) "
    "while maintaining target water quality and water production levels by adapting to influent and membrane "
    "conditions over time."
)

pdf.chapter_title("Problem Context & Business Case:")
pdf.chapter_body(
    "- Current fixed set-points lead to suboptimal energy use.\n"
    "- Human error and lack of tuning time lead to outages and inefficiencies.\n"
    "- A dynamic ML model will provide decision support and reduce unplanned downtime."
)

pdf.chapter_title("Dataset Overview:")
pdf.chapter_body(
    "Features include:\n"
    "- Operational: Qin, Qout, Ec\n"
    "- Water Quality: Turbidity (Feed/Product), TOC (Feed/Product), EC, NH4, BOD, COD, TN\n"
    "- Temporal: Year, Month, Day, Temperature"
)

pdf.chapter_title("Feasibility Highlights:")
pdf.chapter_body(
    "1. Energy Consumption Prediction\n"
    "2. Feature Importance Insights using RF & XGBoost\n"
    "3. Operational Guidance via scenario classification"
)

pdf.chapter_title("Proposed Methodology:")
pdf.chapter_body(
    "1. EDA: Visual patterns, outlier detection\n"
    "2. Feature Engineering: Lag features, deltas\n"
    "3. Feature Selection: RF, XGBoost\n"
    "4. Modeling: KNN, XGBoost, LightGBM, GPR, SVR\n"
    "5. Evaluation: RMSE, MAE, MAPE, J2\n"
    "6. Insights: Feature trends over time"
)

pdf.chapter_title("Key Deliverables:")
pdf.chapter_body(
    "- Dynamic energy prediction models\n"
    "- Feature importance & impact reports\n"
    "- Temporal analytics (seasonal impacts)\n"
    "- Recommendations for dynamic tuning\n"
    "- Optional dashboard integration"
)

pdf.chapter_title("Tools & Stack:")
pdf.chapter_body(
    "- Python (pandas, scikit-learn, xgboost, lightgbm)\n"
    "- Jupyter or Streamlit for visualization\n"
    "- Plotly/Matplotlib for charts\n"
    "- Optional: Flask for API integration"
)

pdf.chapter_title("Why This Approach?")
pdf.chapter_body(
    "- Builds on proven research (e.g., Melbourne WWTP)\n"
    "- Fast models like KNN/RF suitable for real-time ops\n"
    "- Tight focus on actionable insights in a 2-day window"
)

# Save the PDF
output_path = "/mnt/data/RO_Energy_Optimization_Feasibility.pdf"
pdf.output(output_path)
output_path
