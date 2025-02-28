"""Test input file calculate.FiniteDifference grid-related parsing."""
import logging
import pytest
from apbs.input_file.calculate.finite_difference import (
    GridDimensions,
    GridCenter,
)


_LOGGER = logging.getLogger(__name__)


GOOD_ADJUST_GRID = [
    [(33, 33, 33), (33, 33, 33), 5],
    [(34, 35, 36), (33, 33, 33), 5],
    [(65, 65, 65), (65, 65, 65), 6],
    [(97, 97, 97), (97, 97, 97), 5],
    [(129, 129, 129), (129, 129, 129), 7],
    [(161, 172, 166), (161, 161, 161), 5],
    [(225, 225, 225), (225, 225, 225), 5],
    [(257, 257, 257), (257, 257, 257), 8],
    [(321, 321, 321), (321, 321, 321), 6],
]


GOOD_GRID_DIMENSIONS = [
    {
        "counts": [65, 97, 449],
        "lengths": [32, 48, 224],
        "spacings": [0.5, 0.5, 0.5],
    },
    {
        "counts": [145, 289, 577],
        "lengths": [14.4, 14.4, 57.6],
        "spacings": [0.1, 0.05, 0.1],
    },
]


GOOD_GRID_CENTER = [
    {"molecule": "foo", "position": [1, 2, 3.14]},
    {"position": [1, 2, 3.14]},
    {"molecule": "foo",},
]


BAD_GRID_CENTER = [
    {"empty": True},
    {"molecule": 42},
    {"position": "not a tuple or list"},
]

BAD_GRID_COUNTS = [(97, 161, -1), (0, 0, 65), (9, 33, 129)]


BAD_GRID_SPACINGS_LENGTHS = [(1.0, 1.2, 0.0), (3.14, -22, 1.5)]


def id_function(value):
    if isinstance(value, (int, float, tuple)):
        return str(value)


@pytest.mark.parametrize(
    "input_counts, counts, levels", GOOD_ADJUST_GRID, ids=id_function
)
def test_adjust_grid_good(input_counts, counts, levels):
    """Test the counts property of :class:`GridDimensions`."""
    dict_ = {"counts": input_counts, "lengths": [1, 1, 1]}
    grid = GridDimensions(dict_=dict_)
    assert tuple(grid.counts) == counts
    assert grid.levels == levels


@pytest.mark.parametrize("input_dict", GOOD_GRID_DIMENSIONS)
def test_good_grid_dimensions(input_dict):
    """Test property imputation for :class:`GridDimensions`."""
    dict_ = {
        "spacings": input_dict["spacings"],
        "lengths": input_dict["lengths"],
    }
    grid = GridDimensions(dict_=dict_)
    grid = GridDimensions(yaml=grid.to_yaml())
    grid = GridDimensions(json=grid.to_json())
    grid.validate()
    assert grid.counts == input_dict["counts"]
    assert grid.spacings == input_dict["spacings"]
    assert grid.lengths == input_dict["lengths"]
    dict_ = {"counts": input_dict["counts"], "lengths": input_dict["lengths"]}
    grid = GridDimensions(dict_=dict_)
    grid = GridDimensions(yaml=grid.to_yaml())
    grid = GridDimensions(json=grid.to_json())
    grid.validate()
    assert grid.counts == input_dict["counts"]
    assert grid.spacings == input_dict["spacings"]
    assert grid.lengths == input_dict["lengths"]
    dict_ = {
        "counts": input_dict["counts"],
        "spacings": input_dict["spacings"],
    }
    grid = GridDimensions(dict_=dict_)
    grid = GridDimensions(yaml=grid.to_yaml())
    grid = GridDimensions(json=grid.to_json())
    grid.validate()
    assert grid.counts == input_dict["counts"]
    assert grid.spacings == input_dict["spacings"]
    assert grid.lengths == input_dict["lengths"]


@pytest.mark.parametrize("counts", BAD_GRID_COUNTS, ids=id_function)
def test_bad_grid_counts(counts):
    """Test the counts property of :class:`GridDimensions`."""
    dict_ = {"counts": counts, "lengths": [1, 1, 1]}
    with pytest.raises(TypeError):
        GridDimensions(dict_=dict_)


@pytest.mark.parametrize(
    "spacings", BAD_GRID_SPACINGS_LENGTHS, ids=id_function
)
def test_bad_grid_spacings(spacings):
    """Test the spacings property of :class:`GridDimensions`."""
    dict_ = {"spacings": spacings, "lengths": [1, 1, 1]}
    with pytest.raises(TypeError):
        GridDimensions(dict_=dict_)


@pytest.mark.parametrize("lengths", BAD_GRID_SPACINGS_LENGTHS, ids=id_function)
def test_bad_grid_lengths(lengths):
    """Test the lengths property of :class:`GridDimensions`."""
    dict_ = {"spacings": [1, 1, 1], "lengths": lengths}
    with pytest.raises(TypeError):
        GridDimensions(dict_=dict_)


@pytest.mark.parametrize("dict_", GOOD_GRID_CENTER, ids=id_function)
def test_good_grid_centers(dict_):
    """Test the :class:`GridCenter` class."""
    center = GridCenter(dict_=dict_)
    center.validate()
    center = GridCenter(yaml=center.to_yaml())
    center.validate()
    center = GridCenter(json=center.to_json())
    center.validate()


@pytest.mark.parametrize("dict_", BAD_GRID_CENTER, ids=id_function)
def test_bad_grid_centers(dict_):
    """Test the :class:`GridCenter` class."""
    with pytest.raises((TypeError, IndexError, ValueError)):
        center = GridCenter(dict_=dict_)
        center.validate()
