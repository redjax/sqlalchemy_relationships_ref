from dynaconf import settings

if __name__ == "__main__":
    print(f"[TEST] Settings: {settings.as_dict()}")