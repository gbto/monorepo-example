python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
    output_path="pex-binaries/task_b",
)

docker_image(
    name="docker",
    repository="task_b",
    registries=["ghcr.io/gbto"],
    image_tags=["1.0", "latest"],
)
