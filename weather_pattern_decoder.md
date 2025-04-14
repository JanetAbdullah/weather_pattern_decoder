# Weather Pattern Decoder (Extended)

This project presents a fully custom and unique data analysis workflow simulating weather pattern detection using the built-in `flights` dataset from the seaborn library. Passenger counts are interpreted as a proxy for monthly temperature, allowing us to extract and visualize temporal patterns, seasonal shifts, and statistical anomalies.

## Project Goals
- Simulate seasonal weather data using normalized monthly values
- Analyze central tendency and spread per month
- Visualize smoothed trends and inter-year differences
- Detect statistical outliers using IQR
- Compare temperature dynamics across four seasons

## Tools Used
- Python 3.x
- pandas
- matplotlib
- seaborn
- numpy
- scipy (for skewness)

## How to Run
```bash
pip install pandas matplotlib seaborn numpy scipy
python weather_pattern_decoder.py
```

## File Structure
```
weather_pattern_decoder/
├── weather_pattern_decoder.py   # Complete analysis script
├── README.md                    # Project overview and instructions
```

## Analysis Breakdown
### Normalization and Trend Extraction
- Standardization of monthly temperatures per year
- Rolling 3-month average for smoothed seasonal shifts

### Statistical Summary
- Mean, Median, Std, Variance, Skewness per month
- Boxplot and histogram to observe distributions

### Outlier Detection
- Interquartile Range (IQR)-based method
- Identification of extreme temperature months

### Heatmap and Temporal Visuals
- Heatmap of temperature by month/year
- Line plot of normalized patterns across all years

### Annual Delta Calculation
- Compute difference between warmest and coldest month each year
- Track changes and magnitude over time

### Seasonal Analysis
- Categorization of months into Winter, Spring, Summer, Autumn
- Average temperature by season
- Bar plot comparison of seasonal dynamics

## Key Insights
- Simulated summer months consistently show higher average values
- Yearly warm-cold delta reveals volatility in pattern intensity
- Outliers mostly occur in early 1950s and late 1950s
- Autumn appears more stable in variance compared to Winter

## License
This project is open-source and created from scratch to demonstrate analytical thinking, statistical reasoning, and data storytelling.

---

**Author:** Janet Abdullah  
**GitHub:** [https://github.com/JanetAbdullah]  
Feel free to fork and adapt this analysis to your own use!

