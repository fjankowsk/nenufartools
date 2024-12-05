#
#   2024 Fabian Jankowski
#   Check the mini-arrays active in a NenuFAR observation.
#

import argparse
import os.path
import sys

import pandas as pd


def parse_args():
    """
    Parse the commandline arguments.

    Returns
    -------
    args: populated namespace
        The commandline arguments.
    """

    parser = argparse.ArgumentParser(
        description="Check the mini-arrays active in a NenuFAR observations.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "prefix",
        type=str,
        help="The prefix of the meta data files to process (e.g. 20241202_110000_20241202_130000_MULTIFREQUENCY).",
    )

    parser.add_argument(
        "-p",
        "--pulsar",
        dest="pulsarobs",
        action="store_true",
        default=False,
        help="Exclude the distant mini-arrays for pulsar observations, which use the core only.",
    )

    args = parser.parse_args()

    return args


#
# MAIN
#


def main():
    args = parse_args()

    prefix = args.prefix

    poifile = f"{prefix}.poi"
    if not os.path.isfile(poifile):
        print("The POI file does not exist.")
        sys.exit(1)

    names = [
        "date",
        "type",
        "ma",
        "xdelay",
        "ydelay",
        "filter",
        "attenuation",
        "function_code",
        "antnumber",
    ]
    df = pd.read_csv(poifile, comment=";", sep=" ", names=names)
    mas = set(df["ma"].unique())

    disabledfile = f"{prefix}.disabled"
    if not os.path.isfile(disabledfile):
        print("The disabled file does not exist.")
        sys.exit(1)

    disabled = pd.read_csv(disabledfile, sep=" ", names=["text1", "number", "text2"])
    disabled = set(disabled["number"])

    print(f"Disabled mini-arrays: {disabled}")
    print("Number of disabled mini-arrays: {0}".format(len(disabled)))

    active = mas.difference(disabled)

    if args.pulsarobs:
        active = [item for item in active if item < 100]

    print("Active mini-arrays: {0}".format(active))
    print("Number of active mini-arrays: {0}".format(len(active)))

    print("All done.")


if __name__ == "__main__":
    main()
