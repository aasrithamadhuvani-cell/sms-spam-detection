try:
    from src.train_mlflow import run
except ModuleNotFoundError:
    from train_mlflow import run
if __name__ == "__main__":
    run()
