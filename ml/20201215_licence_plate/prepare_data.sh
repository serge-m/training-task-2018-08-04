#!/usr/bin/env sh
set -x
set -e

git clone https://github.com/theAIGuysCode/OIDv4_ToolKit OIDv4_ToolKit
(cd OIDv4_ToolKit && git checkout -b "36d5" "36d500d20e22e01904e672b8e96ed50b15e39aea")
(cd OIDv4_ToolKit && pip install -r requirements.txt)

## download data
(cd OIDv4_ToolKit && python main.py downloader --classes "Vehicle registration plate" --type_csv train --limit 5000 --n_threads 20)
(cd OIDv4_ToolKit && python main.py downloader --classes "Vehicle registration plate" --type_csv validation --limit 5000 --n_threads 20)
## in case you need more classes:
#(cd OIDv4_ToolKit && python main.py downloader --classes "Vehicle registration plate" Car Bus Truck Person Bicycle Motorcycle --type_csv train --limit 5000 --n_threads 20)
#(cd OIDv4_ToolKit && python main.py downloader --classes "Vehicle registration plate" Car Bus Truck Person Bicycle Motorcycle --type_csv validation --limit 5000 --n_threads 20)

(cd OIDv4_ToolKit && echo "Vehicle registration plate" > classes.txt)
(cd OIDv4_ToolKit && python convert_annotations.py)

./copy_converted_annotations.py --input-dir OIDv4_ToolKit/OID/Dataset/train --output-dir data/obj
./copy_converted_annotations.py --input-dir OIDv4_ToolKit/OID/Dataset/validation --output-dir data/test


7z a data.zip ./data/obj/ ./data/test/
