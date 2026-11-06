try:
    from src.preprocess import preprocess
except ModuleNotFoundError:
    from preprocess import preprocess
if __name__ == "__main__":
    preprocess()
