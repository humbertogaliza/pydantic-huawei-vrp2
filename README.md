# Pydantic models for Nokia SR Linux

> [!IMPORTANT]
> This is an experimental project that may graduate to a proper set of Pydantic models for SR Linux in the future.
>
> Limitations:
>
> - system module is not yet supported
> - models are generated without if-features flag set, this means all if-features are implicitly enabled. Note, that this will render models for features that your hardware might not have.
> - if you found additional limitations, please open an issue or reach out in [Discord](https://discord.gg/tZvgjQ6PZf).

The repo comes with a `yang_map.yml` file that contains a map of the Nokia SR Linux YANG models. For the sake of the pydantic model generation the important bits in this map is what YANG modules are augmented by what other modules. This information is used to figure out the modules that need to be provided to pydantify when generating the Pydantic models for a target (usually top level) yang module.

For example, the top level `srl_nokia-interfaces` module that contains the `/interface[]` list is augmented by many other modules, and we need to provide all of them to pydantify so that the tree can be built in full.

The map file is generated by the `yang_map.py` script, which takes the SR Linux YANG models directory path and SR Linux version as inputs and generates the map file.

## Generate YANG mapping file

Clone the [nokia/srlinux-yang-models](https://github.com/nokia/srlinux-yang-models) repo.

```bash
git clone https://github.com/nokia/srlinux-yang-models.git
```

Generate the YANG map file:

```bash
./yang_map.py --dir {path to a dir where you cloned nokia/srlinux-yang-models} --version v24.10.1
```

The script will navigate to the directory with the yang modules identified by the `--dir` argument and checkout the tag specified by the `--version` argument.

Create an environment variable `${SRL_YANG_REPO_DIR}` with the path to the cloned repo as this env var is used in the YANG map file to keep it generically applicable.

```
export SRL_YANG_REPO_DIR=~/path/to/srlinux-yang-models
```

## Generate Pydantic models (automatic)

To manually regenerate the Pydantic models for a given module, run the following command:

```bash
# generate_models.py --module <model name>
./generate_models.py --module srl_nokia-acl
```

The full list of the top level modules:

```
./generate_models.py --module srl_nokia-acl
./generate_models.py --module srl_nokia-bfd
./generate_models.py --module srl_nokia-interfaces
./generate_models.py --module srl_nokia-network-instance
./generate_models.py --module srl_nokia-platform
./generate_models.py --module srl_nokia-qos
./generate_models.py --module srl_nokia-routing-policy
./generate_models.py --module srl_nokia-system (not yet supported)
./generate_models.py --module srl_nokia-tunnel-interfaces
./generate_models.py --module srl_nokia-tunnel
```

This will generate the `tunnel.py` file in the `pydantic_srlinux/models` directory. The script will also create the CLI command used to generate the Pydantic models and store it in the `./temp` directory.
