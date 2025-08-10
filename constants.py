#all folder and filepaths and train size
from pathlib import Path

#Data Directory
DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "iris.csv"

#Model Directory
MODEL_DIR = Path("models")
MODEL_FILE = MODEL_DIR / "iris_model.joblib"

#Training_Configation
TEST_SIZE = 0.33
RANDOM_STATE = 21
TARGET = "species"