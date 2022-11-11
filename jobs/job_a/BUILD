python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
    output_path="pex-binaries/job_a",
)

docker_image(
    name="docker",
    repository="gbto/job_a",
    registries=["gbto/job_a"],
    image_tags=["1.0", "latest"]
)
