import argparse
from pathlib import Path
from oead.aamp import ParameterIO

from . import convert


def main() -> None:
    parser = argparse.ArgumentParser(description="Tool for converting CookData in LoZ:BotW")
    parser.add_argument(
        "file", help="Filename to be converted (accepts wildcards for converting multiple files)",
    )
    parser.add_argument("output", help="Output type: bas or yml")
    parser.add_argument(
        "-n", "--names", help="Output with human-readable names", action="store_true"
    )
    parser.add_argument(
        "-d", "--digits", help="Output with machine-readable values", action="store_true"
    )

    args = parser.parse_args()

    if not args.names and not args.digits:
        raise RuntimeError("-n or -d must be specified!")
    if args.names and args.digits:
        raise RuntimeError("Only one of -n and -d must be specified!")

    output_str: str = str.lower(args.output)
    output_yaml: bool = True if output_str == "yml" or output_str == "yaml" else False
    output_aamp: bool = True if output_str == "bas" or output_str == "aamp" else False
    if not output_yaml and not output_aamp:
        raise RuntimeError("Output type must be one of: 'yml', 'yaml', 'bas', or 'aamp'")

    folder = Path(args.file).parent.resolve()
    filename = Path(args.file).name

    for file in folder.glob(filename):
        ext: str = file.suffix
        pio: ParameterIO = ParameterIO()
        if ext == ".bas":
            pio = ParameterIO.from_binary(file.read_bytes())
        elif ext == ".yml":
            pio = ParameterIO.from_text(file.read_text())

        try:
            if args.names:
                convert.to_names(pio)
            else:
                convert.to_numbers(pio)
        except:
            output_type: str = "names" if args.names else "numbers"
            print(f"{file.name} already had {output_type}! Skipping...")
            continue

        new_file: Path = Path()
        if output_yaml:
            new_file = file.with_suffix(".yml")
            to_write = ParameterIO.to_text(pio)
            new_file.write_text(to_write)
        else:
            new_file = file.with_suffix(".bas")
            to_write = ParameterIO.to_binary(pio)
            new_file.write_bytes(to_write)
