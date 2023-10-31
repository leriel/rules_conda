# rules_conda example

A python app demonstrating case of a conda package which needs full conda init/conda run to work as it includes own activate scripts. 

Some conda packages provide own activate scripts, which get processed on `source activate / conda init` (interactive environments) or `conda run` (non interactive environments). Often, without those scripts being processed, package will not fully function.

For example, tesseract requires `TESSDATA_PREFIX` env var to be pointing at its internal languages directory. Its activate script is

```sh
export TESSDATA_PREFIX=$CONDA_PREFIX/share/tessdata/
```

And so it also relies on conda being initialized via one of methods mentioned above.

## Usage

```sh
bazel run //app:main
```
