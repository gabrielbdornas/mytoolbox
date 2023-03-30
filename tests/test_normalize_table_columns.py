import pytest
from mytoolbox.normalize_table_columns import snake_small_case

@pytest.mark.parametrize("input, output", [
    ('My Column', 'my_column'),
    ('MY_COLUMN', 'my_column'),
    ('My/COLUMN_ÇAU', 'my_column_cau'),
    ('my_column', 'my_column'),
    ('my?column*', 'my_column'),
    ('my-column', 'my_column'),
    ('my_**column()', 'my_column'),
])
def test_snake_small_case(input, output):
	assert snake_small_case(input) == output