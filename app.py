import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(file_path):
    """Load a CSV file and return a DataFrame."""
    try:
        data = pd.read_csv(file_path, encoding="utf-8")
        print("CSV file loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def analyze_data(df):
    """Perform basic data analysis and return insights."""
    try:
        insights = {
            "Total Rows": df.shape[0],
            "Total Columns": df.shape[1],
            "Column Names": df.columns.tolist(),
            "Data Types": df.dtypes.to_dict(),
            "Missing Values": df.isnull().sum().to_dict(),
        }
        return insights
    except Exception as e:
        print(f"Error analyzing data: {e}")
        return None

def generate_visualizations(df, output_folder):
    """Generate visualizations and save them as PNG files."""
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Example Visualization: Histogram for numeric columns
        numeric_cols = df.select_dtypes(include=["number"]).columns
        for col in numeric_cols:
            plt.figure()
            df[col].hist(bins=20)
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            file_name = os.path.join(output_folder, f"{col}_histogram.png")
            plt.savefig(file_name)
            print(f"Saved: {file_name}")
        plt.close("all")
    except Exception as e:
        print(f"Error generating visualizations: {e}")

def save_insights(insights, output_file):
    """Save insights as a text file."""
    try:
        with open(output_file, "w") as f:
            for key, value in insights.items():
                f.write(f"{key}: {value}\n")
        print(f"Insights saved to {output_file}")
    except Exception as e:
        print(f"Error saving insights: {e}")

if __name__ == "__main__":
    # Input: Path to CSV file
    csv_file_path = "data/sample.csv"

    # Load CSV file
    data = load_csv(csv_file_path)

    if data is not None:
        # Analyze Data
        insights = analyze_data(data)
        print("\n--- Data Insights ---")
        for key, value in insights.items():
            print(f"{key}: {value}")

        # Save Insights to a Text File
        save_insights(insights, "outputs/insights.txt")

        # Generate Visualizations
        generate_visualizations(data, "outputs/")
