import pandas as pd

class HelperDataFrame(pd.DataFrame):
    """Inherits from a Pandas Data Frame and adds a couple methods."""
    def __init__(self, df):
        super().__init__(data=df)
        # self.random_state = 42

    def randomize(self):
        """Shuffles observations of a dataframe"""
        return self.sample(frac=1, random_state=42)

    def null_count(self):
        """Get total null cells"""
        return self.isnull().sum().sum()


if __name__ == "__main__":
    print("HelperDataFrame")


