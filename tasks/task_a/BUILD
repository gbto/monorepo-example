python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
    output_path="pex-binaries/job_a",
)

docker_image(
    name="docker",
    repository="job_a",
    registries=["ghcr.io/gbto"],
    image_tags=["1.0", "latest"]
)
