python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
)

docker_image(
    name="docker",
    repository="job_b",
    registries=["ghcr.io/gbto"],
    image_tags=["1.0", "latest"],
)
