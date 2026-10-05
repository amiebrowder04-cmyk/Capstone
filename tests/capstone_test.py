import pandas as pd

# Test that all the columns exixt in the final combined  table 
def test_required_columns_exist():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    required_columns = [
        "County_ID",
        "County",
        "Total_Population",
        "Below_Poverty",
        "Unemployed",
        "Less_Than_High_School",
        "Poverty_Percent",
    ]

    for column in required_columns:
        assert column in df.columns

# Test that the scoring columns exist (Needs_Score, Support_Gap_Score, Final_Score)
def test_scoring_columns_exist():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    scoring_columns = [
        "Needs_Score",
        "Support_Gap_Score",
        "Final_Score",
    ]

    for column in scoring_columns:
        assert column in df.columns 

# Test for missing values in the variables used in the final data set 
def test_for_missing_values():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    analysis_columns = [
        "County_ID",
        "County",
        "Total_Population",
        "Below_Poverty",
        "Unemployed",
        "Less_Than_High_School",
        "Poverty_Percent",
        "Needs_Score",
        "Support_Gap_Score",
        "Final_Score",
    ]
    assert df[analysis_columns].isna().sum().sum() == 0

# Check that each county only appears once 
def test_counties_are_unique():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    assert df["County_ID"].is_unique

# Check that the scoring columns only contain valid numeric values 
def test_scores_are_valid():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    scoring_columns = [
            "Needs_Score",
            "Support_Gap_Score",
            "Final_Score",
        ]

    for column in scoring_columns:
        assert pd.api.types.is_numeric_dtype(df[column])
        assert df[column].notna().all()
        assert df[column].apply(lambda x: x != float("inf") and x != float("-inf")).all()

# Check that the final score calculation is accurate 
def test_final_score_calculation():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    expected_score = (
        (df["Needs_Score"] * 0.50)
        + (df["Support_Gap_Score"] * 0.50)
    )

    assert (df["Final_Score"]- expected_score).abs().max() < 0.000001

# Check that the top 3 coutnies have the highest scores
def test_top_3_counties():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    ranked_df = df.sort_values("Final_Score", ascending = False)
    top_3 = ranked_df.head(3)

    assert len(top_3) == 3
    assert top_3["Final_Score"].tolist() == sorted(
        top_3["Final_Score"].tolist(),
        reverse = True
    )

# Check that the top 3 are actually the highest scored 
def test_top_3_are_highest_scores():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    ranked_df = df.sort_values("Final_Score", ascending = False)
    top_3 = ranked_df.head(3)

    expected_scores = ranked_df["Final_Score"].head(3).tolist()
    actual_scores = top_3["Final_Score"].tolist()

    assert actual_scores == expected_scores

# Test that the top 3 counties have complete infomration 
def test_top_3_have_complete_information():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    ranked_df = df.sort_values("Final_Score", ascending = False)
    top_3 = ranked_df.head(3)

    required_columns = [
        "County",
        "Needs_Score",
        "Support_Gap_Score",
        "Final_Score",
    ]

    assert top_3[required_columns].notna().all().all()

    #Check that we have the correct number of counties 
def test_county_count():
    df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

    assert len(df) == 39