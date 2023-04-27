import gpu_estimation
import sys 

name = "gpu-estimator"
version = "0.0.1"
description = "script to estimate gpu usage"

def main():
    gpu_function_args = {}
    if len(sys.argv) == 1:
        print("Please provide the path to your file")
        sys.exit(1)
    path = sys.argv[1]
    gpu_function_args["path_to_file"] = path
    gpu_estimation.main(gpu_function_args)

if __name__ == "__main__":
    main()