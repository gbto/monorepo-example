"""A utils example for pants build testing purposes."""
import pandas as pd


def action_2() -> None:
    """An example action to execute within job_a."""
    df = pd.DataFrame()
    print(df)
    print("Doing stuff from package 2")
    return
