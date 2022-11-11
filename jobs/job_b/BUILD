python_sources()

pex_binary(
    name="main",
    entry_point="main.py",
    output_path="pex-binaries/job_b",
)

docker_image(
    name="docker",
    repository="gbto/job_b",
    registries=["gbto"],
    image_tags=["1.0", "latest"],
)
