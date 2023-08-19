from collections import ChainMap


def test_all():
    cli_argument = {"a": "cli"}
    environment = {"a": "env", "b": "env"}
    config = {"a": "config", "b": "config", "c": "config"}
    chain = ChainMap(cli_argument, environment, config)
    assert chain["a"] == "cli"
    assert chain["b"] == "env"
    assert chain["c"] == "config"

    chain.update({"a": "overwrite"})
    assert chain["a"] == "overwrite"
