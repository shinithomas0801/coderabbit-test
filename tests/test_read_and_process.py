import importlib.util
from pathlib import Path


def _load_refactor_example_module():
    repo_root = Path(__file__).resolve().parents[1]
    target = repo_root / "refactor-example.py"
    spec = importlib.util.spec_from_file_location("refactor_example", str(target))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader, "Unable to load refactor-example.py"
    spec.loader.exec_module(module)
    return module


def test_read_and_process_happy_path(tmp_path):
    module = _load_refactor_example_module()
    sample = "  Hello, World!  \n\nThis   is  A test.\n"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(sample, encoding="utf-8")

    captured = {"error": None, "result": None}

    def cb(err, result):
        captured["error"] = err
        captured["result"] = result

    module.read_and_process(str(file_path), cb)

    assert captured["error"] is None
    # Expect: lowercase, punctuation stripped, words joined by underscore, empty lines skipped, trailing newline
    assert captured["result"] == "hello_world\nthis_is_a_test\n"


def test_read_and_process_file_error(tmp_path):
    module = _load_refactor_example_module()
    missing_file = tmp_path / "does_not_exist.txt"

    captured = {"error": None, "result": "not-reset"}

    def cb(err, result):
        captured["error"] = err
        captured["result"] = result

    module.read_and_process(str(missing_file), cb)

    assert captured["error"] is not None
    assert captured["result"] is None


