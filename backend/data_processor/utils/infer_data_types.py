import pandas as pd
import numpy as np


def infer_and_convert_data_types(df):
    # Convert 'Birthdate' to datetime; no change in bit length as pandas uses datetime64[ns]
    df["Birthdate"] = pd.to_datetime(
        df["Birthdate"], errors="coerce", format="%d/%m/%Y"
    )

    # Convert 'Score' to numeric, specifying float bit length as float32 for memory efficiency
    df["Score"] = pd.to_numeric(
        df["Score"].replace("Not Available", np.nan), errors="coerce"
    ).astype("float32")

    # Convert 'Grade' to categorical since it likely has a limited set of values
    df["Grade"] = pd.Categorical(df["Grade"])

    return df


if __name__ == "__main__":
    # Specify columns to load using usecols for memory efficiency
    columns_to_use = ["Name", "Birthdate", "Score", "Grade"]
    chunk_size = 5000  # Memory capacity and the size of the dataset
    df_final = pd.DataFrame()

    for chunk in pd.read_csv(
        "../../../sample_data.csv", chunksize=chunk_size, usecols=columns_to_use
    ):
        chunk_processed = infer_and_convert_data_types(chunk)
        df_final = pd.concat([df_final, chunk_processed], ignore_index=True)

    print("\nData types after inference:")
    print(df_final.dtypes)

    # Display data
    print("\nData after inference:")
    print(df_final.head())  # Display the first few rows to check the conversion
