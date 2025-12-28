Timestamp: 2025-12-28 21:55:22

# Repository Inventory

## Directory Structure

```text
D:\DEV\projects\dbl-ingress
├── README.md
├── pyproject.toml
├── LICENSE
├── CHANGELOG.md
├── src
├── tests
```

## File Contents

### D:\DEV\projects\dbl-ingress\CHANGELOG.md

```
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-12-28
### Added
- Initial release of `dbl-ingress`.
- Strict `AdmissionRecord` validation logic.
- `shape_input` factory function.
- Strict JSON type enforcement (invariants).
- CI configuration.

```

### D:\DEV\projects\dbl-ingress\LICENSE

```
MIT License

Copyright (c) 2025 Lukas Pfister

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### D:\DEV\projects\dbl-ingress\pyproject.toml

```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "dbl-ingress"
version = "0.1.0"
description = "Admission and shaping layer for dbl-core"
readme = "README.md"
requires-python = ">=3.11"
license = { text = "MIT" }
authors = [
  { name = "Lukas Pfister" },
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Typing :: Typed",
]
dependencies = [
    "dbl-core==0.3.1",
    "kl-kernel-logic>=0.5.0,<0.6.0",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
    "mypy",
]

[project.urls]
"Homepage" = "https://github.com/lukaspfister/dbl-ingress"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
dbl_ingress = ["py.typed"]

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-q --strict-markers"
testpaths = [
    "tests",
]

[tool.ruff]
target-version = "py311"
line-length = 100
fix = true

[tool.ruff.lint]
extend-select = ["I"]

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

```

### D:\DEV\projects\dbl-ingress\README.md

```
# dbl-ingress

`dbl-ingress` serves as the admission and shaping layer for the Deterministic Boundary Layer (DBL). Its primary purpose is to strictly validate and shape external inputs into `AdmissionRecord` structures before they are processed by the core system, ensuring that no invalid or non-deterministic data enters the boundary event stream.

## Scope

- **Admission**: strict validation of incoming data payloads.
- **Shaping**: converting raw inputs into typed, immutable records.
- **Invariants**: enforcing data types (e.g., rejecting floats in deterministic fields) early in the pipeline.

## Non-Goals

- Execution logic or side effects.
- Policy decisions or complex business rules.
- Network transport or service runtime concerns.
- CLI tools.

## Relation to dbl-core

This library acts as a precursor to `dbl-core`. While `dbl-core` manages the deterministic event log and state reconstruction, `dbl-ingress` ensures that the data fed into `dbl-core` is well-formed and safe for deterministic processing.

## Status

**Experimental**: This project is in early development.

```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress.egg-info\dependency_links.txt

```


```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress.egg-info\PKG-INFO

```
Metadata-Version: 2.4
Name: dbl-ingress
Version: 0.1.0
Summary: Admission and shaping layer for dbl-core
Author: Lukas Pfister
License: MIT
Project-URL: Homepage, https://github.com/lukaspfister/dbl-ingress
Classifier: Programming Language :: Python :: 3
Classifier: License :: OSI Approved :: MIT License
Classifier: Operating System :: OS Independent
Classifier: Typing :: Typed
Requires-Python: >=3.11
Description-Content-Type: text/markdown
License-File: LICENSE
Requires-Dist: dbl-core==0.3.1
Requires-Dist: kl-kernel-logic<0.6.0,>=0.5.0
Provides-Extra: dev
Requires-Dist: pytest; extra == "dev"
Requires-Dist: ruff; extra == "dev"
Requires-Dist: mypy; extra == "dev"
Dynamic: license-file

# dbl-ingress

`dbl-ingress` serves as the admission and shaping layer for the Deterministic Boundary Layer (DBL). Its primary purpose is to strictly validate and shape external inputs into `AdmissionRecord` structures before they are processed by the core system, ensuring that no invalid or non-deterministic data enters the boundary event stream.

## Scope

- **Admission**: strict validation of incoming data payloads.
- **Shaping**: converting raw inputs into typed, immutable records.
- **Invariants**: enforcing data types (e.g., rejecting floats in deterministic fields) early in the pipeline.

## Non-Goals

- Execution logic or side effects.
- Policy decisions or complex business rules.
- Network transport or service runtime concerns.
- CLI tools.

## Relation to dbl-core

This library acts as a precursor to `dbl-core`. While `dbl-core` manages the deterministic event log and state reconstruction, `dbl-ingress` ensures that the data fed into `dbl-core` is well-formed and safe for deterministic processing.

## Status

**Experimental**: This project is in early development.

```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress.egg-info\requires.txt

```
dbl-core==0.3.1
kl-kernel-logic<0.6.0,>=0.5.0

[dev]
pytest
ruff
mypy

```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress.egg-info\SOURCES.txt

```
LICENSE
README.md
pyproject.toml
src/dbl_ingress/__init__.py
src/dbl_ingress/py.typed
src/dbl_ingress.egg-info/PKG-INFO
src/dbl_ingress.egg-info/SOURCES.txt
src/dbl_ingress.egg-info/dependency_links.txt
src/dbl_ingress.egg-info/requires.txt
src/dbl_ingress.egg-info/top_level.txt
src/dbl_ingress/admission/__init__.py
src/dbl_ingress/admission/errors.py
src/dbl_ingress/admission/json_types.py
src/dbl_ingress/admission/model.py
src/dbl_ingress/shaping/__init__.py
src/dbl_ingress/shaping/shape.py
tests/test_immutability.py
tests/test_imports.py
tests/test_validation.py
```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress.egg-info\top_level.txt

```
dbl_ingress

```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\__init__.py

```
__version__ = "0.1.0"

from .admission.errors import AdmissionError, InvalidInputError
from .admission.model import AdmissionRecord
from .shaping.shape import shape_input

__all__ = [
    "AdmissionRecord",
    "AdmissionError",
    "InvalidInputError",
    "shape_input",
]

```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\admission\__init__.py

```
```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\admission\errors.py

```
class AdmissionError(Exception):
    """Base exception for all admission-related errors."""


class InvalidInputError(AdmissionError):
    """Raised when input data fails validation."""

```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\admission\json_types.py

```
from types import MappingProxyType
from typing import Dict, Mapping, TypeAlias, Union, cast

# Recursive type alias for JSON-safe values
# Note: mypy has trouble with recursive aliases, so we simplify slightly or use Any if needed,
# but for documentation and runtime enforcement this is the goal.
JsonValue: TypeAlias = Union[str, int, bool, None, "JsonSequence", "JsonMapping"]
JsonSequence: TypeAlias = tuple["JsonValue", ...]
JsonMapping: TypeAlias = Mapping[str, "JsonValue"]

def deep_freeze(value: object, path: str) -> JsonValue:
    """
    recursively strict-validates and deep-freezes the input.
    
    Returns an immutable copy of the data:
    - Lists -> tuples
    - Dicts -> MappingProxyType (wrapping a frozen dict)
    
    Invariants:
    - No floats.
    - No sets, objects, etc.
    - Keys must be strings.
    """
    if value is None:
        return None
        
    if isinstance(value, str):
        return value
        
    if isinstance(value, bool):
        return value
        
    if isinstance(value, int):
        return value
        
    if isinstance(value, float):
        raise TypeError(f"Floats are not allowed in admission records at {path}: {value}")
        
    if isinstance(value, Mapping):
        # We construct a new dict to ensure no reference to original mutable dict remains,
        # then wrap it in MappingProxyType
        frozen_dict: Dict[str, JsonValue] = {}
        for k, v in value.items():
            if not isinstance(k, str):
                 raise TypeError(f"Dictionary keys must be strings at {path}: {k}")
            frozen_dict[k] = deep_freeze(v, f"{path}.{k}")
        return cast(JsonValue, MappingProxyType(frozen_dict))
        
    if isinstance(value, list):
        # Convert list to tuple
        return tuple(deep_freeze(item, f"{path}[{i}]") for i, item in enumerate(value))

    # Reject everything else
    raise TypeError(f"Invalid type at {path}: {type(value)}")

def validate_json_safe(value: object, path: str) -> None:
    """
    Legacy validator wrapper for backward compatibility if needed, 
    but for hardening we prefer deep_freeze.
    """
    deep_freeze(value, path)


```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\admission\model.py

```
from dataclasses import dataclass
from typing import Mapping

from .errors import InvalidInputError
from .json_types import JsonMapping, deep_freeze


@dataclass(frozen=True)
class AdmissionRecord:
    correlation_id: str
    deterministic: JsonMapping
    observational: JsonMapping | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.correlation_id, str) or not self.correlation_id:
            raise InvalidInputError("correlation_id must be a non-empty string")
        
        # Validate and freeze deterministic data
        if not isinstance(self.deterministic, Mapping):
            raise InvalidInputError("deterministic must be a dictionary or mapping")

        try:
            # Enforce immutability / validation
            # We must use object.__setattr__ because the dataclass is frozen
            object.__setattr__(
                self, 
                'deterministic', 
                deep_freeze(self.deterministic, "deterministic")
            )
            
            # Validate and freeze observational data if present
            if self.observational is not None:
                if not isinstance(self.observational, Mapping):
                    raise InvalidInputError("observational must be a dictionary or mapping if provided")
                
                object.__setattr__(
                    self, 
                    'observational', 
                    deep_freeze(self.observational, "observational")
                )

        except TypeError as e:
            raise InvalidInputError(str(e)) from e


```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\py.typed

```
```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\shaping\__init__.py

```
```

### D:\DEV\projects\dbl-ingress\src\dbl_ingress\shaping\shape.py

```
from typing import Mapping

from ..admission.json_types import JsonValue
from ..admission.model import AdmissionRecord


def shape_input(
    *, 
    correlation_id: str, 
    deterministic: Mapping[str, JsonValue], 
    observational: Mapping[str, JsonValue] | None = None
) -> AdmissionRecord:
    """
    Constructs an AdmissionRecord from inputs.
    
    This function acts as the primary entry point for creating strictly validated
    records for the dbl-core system. It enforces type constraints and data
    integrity.

    Args:
        correlation_id: A unique identifier for tracking this input.
        deterministic: A dictionary of deterministic data (JSON-safe, no floats).
        observational: Optional dictionary of observational data (JSON-safe, no floats).

    Returns:
        A validated AdmissionRecord.

    Raises:
        InvalidInputError: If validation fails (e.g. invalid types, floats present).
    """
    return AdmissionRecord(
        correlation_id=correlation_id,
        deterministic=deterministic,
        observational=observational
    )

```

### D:\DEV\projects\dbl-ingress\tests\test_immutability.py

```
from types import MappingProxyType

import pytest

from dbl_ingress import shape_input


def test_immutability_of_lists():
    """Verify that lists are converted to tuples."""
    record = shape_input(
        correlation_id="immut-list",
        deterministic={"list": [1, 2, 3]}
    )
    # The value inside the record should be a tuple
    assert isinstance(record.deterministic["list"], tuple)
    assert record.deterministic["list"] == (1, 2, 3)

def test_immutability_of_dicts():
    """Verify that dicts are wrapped in MappingProxyType."""
    record = shape_input(
        correlation_id="immut-dict",
        deterministic={"data": {"nested": "val"}}
    )
    # The top level deterministic is a MappingProxyType (because deep_freeze wraps dicts)
    assert isinstance(record.deterministic, MappingProxyType)
    
    # Nested dict should also be MappingProxyType
    assert isinstance(record.deterministic["data"], MappingProxyType)
    
    # Attempting to mutate should fail
    with pytest.raises(TypeError):
        record.deterministic["data"]["new"] = 1 # type: ignore

def test_external_mutation_safety():
    """Verify that mutating the input dict does not affect the record."""
    input_data = {"key": "value"}
    record = shape_input(
        correlation_id="safety-test",
        deterministic=input_data
    )
    
    # Mutate external
    input_data["key"] = "changed"
    
    # Record should remain "value"
    assert record.deterministic["key"] == "value"

def test_frozen_dataclass_mutation():
    """Verify that the dataclass itself is frozen."""
    record = shape_input(correlation_id="frozen", deterministic={})
    with pytest.raises(AttributeError): # FrozenInstanceError is AttributeError subclass
        record.correlation_id = "new-id" 

def test_tuple_conversion_deep():
    """Verify recursive list-to-tuple conversion."""
    record = shape_input(
        correlation_id="deep-tuple",
        deterministic={"matrix": [[1, 2], [3, 4]]}
    )
    matrix = record.deterministic["matrix"]
    assert isinstance(matrix, tuple)
    assert isinstance(matrix[0], tuple)
    assert matrix[0] == (1, 2)

```

### D:\DEV\projects\dbl-ingress\tests\test_imports.py

```
import pytest

from dbl_ingress import AdmissionError, AdmissionRecord, InvalidInputError, __version__, shape_input


def test_imports():
    """Verify that expected symbols are exported."""
    assert __version__ == "0.1.0"
    assert AdmissionRecord
    assert AdmissionError
    assert InvalidInputError
    assert shape_input

def test_valid_admission_record():
    """Verify creation of a valid AdmissionRecord."""
    record = shape_input(
        correlation_id="test-123",
        deterministic={"key": "value", "num": 123, "bool": True, "none": None},
        observational={"obs": "data"}
    )
    assert record.correlation_id == "test-123"
    assert record.deterministic["num"] == 123
    assert record.observational["obs"] == "data"

def test_invalid_correlation_id():
    """Verify rejection of invalid correlation_id."""
    with pytest.raises(InvalidInputError, match="non-empty string"):
        shape_input(correlation_id="", deterministic={})

def test_reject_floats_deterministic():
    """Verify that floats are rejected in deterministic data."""
    with pytest.raises(InvalidInputError, match="Floats are not allowed"):
        shape_input(
            correlation_id="test-float",
            deterministic={"bad": 1.5}
        )

def test_reject_floats_observational():
    """Verify that floats are rejected in observational data."""
    with pytest.raises(InvalidInputError, match="Floats are not allowed"):
        shape_input(
            correlation_id="test-float-obs",
            deterministic={},
            observational={"bad": 3.14}
        )

def test_reject_non_string_keys():
    """Verify that dictionary keys must be strings."""
    with pytest.raises(InvalidInputError, match="keys must be strings"):
        shape_input(
            correlation_id="test-keys",
            deterministic={1: "bad_key"} # type: ignore
        )

def test_nested_validation():
    """Verify validation recurses into lists and nested dicts."""
    with pytest.raises(InvalidInputError, match="Floats are not allowed"):
        shape_input(
            correlation_id="test-nested",
            deterministic={"list": [1, 2, {"nested": 1.1}]}
        )

```

### D:\DEV\projects\dbl-ingress\tests\test_validation.py

```
import pytest

from dbl_ingress import InvalidInputError, shape_input


class CustomObj:
    def to_dict(self):
        return {"a": 1}

def test_deep_validation_rejection():
    """Verify that validation fails deeply inside a structure."""
    with pytest.raises(InvalidInputError, match="Floats are not allowed"):
        shape_input(
            correlation_id="deep-test",
            deterministic={
                "level1": {
                    "level2": [
                        {"level3": 1.1}
                    ]
                }
            }
        )

def test_observational_is_validated():
    """Verify that observational data is strictly validated just like deterministic."""
    with pytest.raises(InvalidInputError, match="Floats are not allowed"):
        shape_input(
            correlation_id="obs-test",
            deterministic={"ok": 1},
            observational={"bad": 1.1}
        )

def test_reject_sets():
    """Verify that sets are rejected (JSON requires lists)."""
    with pytest.raises(InvalidInputError, match="Invalid type"):
        shape_input(
            correlation_id="set-test",
            deterministic={"bad": {1, 2, 3}}
        )

def test_reject_tuples():
    """Verify that tuples are rejected (should use lists)."""
    with pytest.raises(InvalidInputError, match="Invalid type"):
        shape_input(
            correlation_id="tuple-test",
            deterministic={"bad": (1, 2)}
        )

def test_reject_custom_objects():
    """Verify that custom objects are rejected, even with to_dict."""
    obj = CustomObj()
    with pytest.raises(InvalidInputError, match="Invalid type"):
        shape_input(
            correlation_id="obj-test",
            deterministic={"bad": obj}
        )

```

