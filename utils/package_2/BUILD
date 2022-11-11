python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[":config"],
    output_path="pex-binaries/package_2"
)

file(
    name="config",
    source="config.yaml",
)
