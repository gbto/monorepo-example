python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
    output_path="pex-binaries/task_a",
)

docker_image(
    name="docker",
    repository="task_a",
    registries=["ghcr.io/gbto"],
    image_tags=["1.0", "latest"]
)
