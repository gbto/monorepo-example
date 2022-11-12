"""A utils example for pants build testing purposes."""
import random
import string

import numpy as np
import pandas as pd


def action_2() -> None:
    """An example action to execute within job_a."""
    print("Doing stuff from package 2")
    # Generate a dataframe
    df = pd.DataFrame(
        {
            "date": pd.date_range("2021-09-25", periods=8, freq="D"),
            "id": [np.int8(x) for x in range(8)],
            "values": [
                "".join(random.choices(string.ascii_lowercase, k=5)) for x in range(8)
            ],
        }
    )

    print(df)
    return
