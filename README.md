# Data Visualization using Python

### How to create your own Jupyter Book

1. `conda env create -f environment.yml`
2. `conda activate dsn-template`

### Building a Jupyter Book

Run the following command in your terminal: `jb build book/`.
If you would like to work with a clean build, you can empty the build folder by running `jb clean book/`. If the jupyter execution is cached, this command will not delete the cached folder. To remove the build folder, you can run `jb clean --all book/`.

### Publishing this Jupyter Book

Run `ghp-import -n -p -f book/_build/html`
