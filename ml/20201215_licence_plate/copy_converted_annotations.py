#!/usr/bin/env python3
import shutil
import sys
from pathlib import Path
import argparse
from tqdm import tqdm


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=str, required=True)
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args(sys.argv[1:])

    dir_in = Path(args.input_dir)
    dir_out = Path(args.output_dir)

    if not dir_in.exists():
        raise ValueError(f"directory '{dir_in}' doesn't exist")

    paths = sorted(dir_in.glob("*/*"))
    cnt_copied = 0
    for path in tqdm(paths):
        if not path.is_file():
            print(f"skipped {path}")
            continue
        path_out = dir_out.joinpath(*path.parts[-2:])
        path_out.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy(path, path_out)
        cnt_copied += 1

    print(f"Copied {cnt_copied} files")
    exit(0)





