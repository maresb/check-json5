# check-json5

## Links

- [GitLab](https://gitlab.com/bmares/pre-commit-check-json5)
- [GitHub](https://github.com/maresb/pre-commit-check-json5)

## Introduction

This is a pre-commit hook which verifies that `.json` files in a repository are valid [JSON5](https://json5.org/). The JSON5 format is similar to JSON, but it permits comments, trailing commas, and more. It is similar to the so-called "JSONC" (JSON with Comments) format, but JSON5 has an actual specification.

This hook is a drop-in replacement for the `check-json` hook from the [official pre-commit-hooks repository](https://pre-commit.com/hooks.html). A file succeeds when it can be loaded by the [json5 library](https://pypi.org/project/json5/). (In contrast, `check-json` uses the built-in [json library](https://docs.python.org/3/library/json.html).)

## Usage

In `.pre-commit-config.yaml` under the `repos:` section, add the following:

```yaml
- repo: git://gitlab.com/bmares/pre-commit-check-json5
  rev: v1.0.0
  hooks:
  - id: check-json5
```

(The original `check-json` hook should probably be removed in case it is already included.)

## Credits

The actual code this hook was written by [@asottile and various contributors to the official pre-commit-hooks repository](https://github.com/pre-commit/pre-commit-hooks/commits/master/pre_commit_hooks/check_json.py). The current author (@maresb) replaced the `json` library with `json5` and published it as a separate hook.

## License

This hook is published under the [MIT license](LICENSE). The original pre-commit-hooks is also published under the MIT license, [included here](LICENSE.pre-commit-hooks).
