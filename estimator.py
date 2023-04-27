import argparse
import gpu_estimation
import sys 

name = "gpu-estimator"
version = "0.0.1"
description = "script to estimate gpu usage"

def main():
    parser = argparse.ArgumentParser(
        prog="GPU estimation",
        description="Script to estimate GPU usage of ML model"
    )
    parser.add_argument(
        "-v","--version",
        action="store_true",
        help="Print the version and exit."
    )
    subparsers = parser.add_subparsers(title="Commands")
    gpu_estimation.register_command(subparsers)
    args = parser.parse_args()

    if args.version:
        print("GPU estimator","v" + version)
        sys.exit(0)
    
    if 'func' not in args:
        parser.print_help()
        sys.exit(1)

    # Run the specified command
    args.func(args)   


if __name__ == "__main__":
    main()