from parser import parse_product_basic, parse_availability

def test_parse_product_basic_extracts_id(valid_product):
    # Act
    result = parse_product_basic(valid_product)

    # Assert
    assert result["id"] == valid_product["id"]

def test_parse_product_basic_extracts_name(valid_product):
    # Act
    result = parse_product_basic(valid_product)

    # Assert
    assert result["name"] == valid_product["name"]

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    # Act
    result = parse_product_basic(valid_product)

    # Assert
    assert set(result.keys()) == {"id", "name"}