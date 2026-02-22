from datetime import datetime, timezone


def main() -> None:
    print("real-time-misinformation-detection-network initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
