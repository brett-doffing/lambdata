import unittest
import pandas as pd
from helper_df import HelperDataFrame
from pandas.testing import assert_frame_equal

class TestHelperDataFrameClass(unittest.TestCase):
    """Testing the Helper Data Frame."""

    def setUp(self):
        test_df = { 'name': ['Tendulkar', 'Sangakkara', 'Ponting', 
                            'Jayasurya', 'Jayawardene', 'Kohli', 
                            'Haq', 'Kallis', 'Ganguly', 'Dravid'], 
                    'runs': [18426, 14234, 13704, 13430, 12650, 
                            11867, 11739, 11579, 11363, 10889]} 

        self.df = pd.DataFrame(test_df)

    def test_randomize(self):
        """Tests randomizing the rows of a data frame"""
        hdf = HelperDataFrame(self.df)

        randomized_data = { 'name': ['Ganguly', 'Sangakkara', 'Kohli', 
                                    'Tendulkar', 'Kallis', 'Ponting', 
                                    'Dravid', 'Jayawardene', 'Jayasurya', 'Haq'], 
                            'runs': [11363, 14234, 11867, 18426, 11579, 
                                    13704, 10889, 12650, 13430, 11739]}
        
        # Randomized data frame from randomized_df with a seed of 42
        randomized_df = pd.DataFrame(randomized_data, index=[8,1,5,0,7,2,9,4,3,6])

        assert_frame_equal(hdf.randomize(), randomized_df)


if __name__ == "__main__":
    unittest.main()