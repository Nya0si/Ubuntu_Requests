# Task: Data Analysis and Visualization with Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def main():
    print("🌸 Iris Dataset Analysis & Visualization\n")

    try:
        # ---------------- Task 1: Load and Explore ----------------
        # Load Iris dataset from sklearn and convert to DataFrame
        iris = load_iris(as_frame=True)
        df = iris.frame  # Includes both features and target

        # Rename target column for clarity
        df.rename(columns={"target": "species"}, inplace=True)
        df["species"] = df["species"].map(dict(enumerate(iris.target_names)))

        print("✅ Dataset loaded successfully!\n")

        # Display first few rows
        print("🔹 First 5 rows:")
        print(df.head(), "\n")

        # Info about dataset
        print("🔹 Dataset info:")
        print(df.info(), "\n")

        # Check for missing values
        print("🔹 Missing values:")
        print(df.isnull().sum(), "\n")

        # Clean dataset (not needed for Iris, but we’ll show the step)
        df = df.dropna()

        # ---------------- Task 2: Basic Data Analysis ----------------
        print("📊 Basic Statistics:")
        print(df.describe(), "\n")

        # Group by species and calculate mean of numerical features
        print("🔹 Mean values grouped by species:")
        grouped = df.groupby("species").mean()
        print(grouped, "\n")

        # ---------------- Task 3: Data Visualization ----------------
        sns.set_style("whitegrid")  # Nicer plot style

        # 1. Line chart (simulate time-series using row index)
        plt.figure(figsize=(8, 5))
        plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
        plt.title("Line Chart: Sepal Length Over Samples")
        plt.xlabel("Sample Index")
        plt.ylabel("Sepal Length (cm)")
        plt.legend()
        plt.show()

        # 2. Bar chart (average petal length per species)
        plt.figure(figsize=(8, 5))
        sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="viridis")
        plt.title("Bar Chart: Average Petal Length per Species")
        plt.xlabel("Species")
        plt.ylabel("Average Petal Length (cm)")
        plt.show()

        # 3. Histogram (distribution of sepal width)
        plt.figure(figsize=(8, 5))
        plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
        plt.title("Histogram: Sepal Width Distribution")
        plt.xlabel("Sepal Width (cm)")
        plt.ylabel("Frequency")
        plt.show()

        # 4. Scatter plot (sepal length vs petal length)
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
        plt.title("Scatter Plot: Sepal Length vs Petal Length")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Petal Length (cm)")
        plt.legend(title="Species")
        plt.show()

        print("✅ Visualizations created successfully!")

    except FileNotFoundError:
        print("❌ Error: Dataset file not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
