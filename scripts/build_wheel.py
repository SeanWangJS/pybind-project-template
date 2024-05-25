from pathlib import Path
from subprocess import run
from functools import partial

def main(args):

    PROJECT_DIR = Path(__file__).parent.resolve().parent

    
    print(PROJECT_DIR)
    source_dir = PROJECT_DIR / "csrc"

    build_run = partial(run, shell=True, check=True)

    build_run(f"cmake -S {source_dir} -B {source_dir}/build")

    # build_run()
if __name__ == "__main__":
    args = None
    main(args)