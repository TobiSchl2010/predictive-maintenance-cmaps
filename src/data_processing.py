from pathlib import Path
import pandas as pd


def load_fd001_train_data(data_dir: str = "data/raw") -> pd.DataFrame:

    index_names = ["engine_id", "time_cycle"]
    setting_names = ["setting_1", "setting_2", "setting_3"]
    sensor_names = [f"sensor_{i}" for i in range(1, 22)]
    col_names = index_names + setting_names + sensor_names

    file_path = Path(data_dir) / "train_FD001.txt"

    df = pd.read_csv(file_path, sep="\s+", header=None, names=col_names)

    df = df.sort_values(["engine_id", "time_cycle"])

    return df
