# Read and collate squirrel data

# Read in csv
import pandas
squirrel_data = pandas.read_csv("squirrel_data.csv")

# Summarize the data on Primary Fur Color
fur_color_series = squirrel_data["Primary Fur Color"]

# Create series of summary results
fur_summary_series = fur_color_series.value_counts(dropna=True)
print(fur_summary_series)
fur_summary_df = fur_summary_series.to_frame()
fur_summary_df.to_csv("squirrel_fur_types.csv")
