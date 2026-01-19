from sliderbox import sliderbox


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("size")
    parser.add_argument("spaces")
    args = parser.parse_args()

    x = sliderbox(int(args.size), int(args.spaces))
