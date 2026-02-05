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

def test_parse_availability_when_in_stock(valid_product):
    # Act
    result = parse_availability(valid_product)

    # Assert 
    assert result is True

def test_parse_availability_when_out_of_stock(product_out_of_stock):
    # Act
    result = parse_availability(product_out_of_stock)

    # Assert
    assert result is False 

def test_parse_availability_when_field_missing(minimal_product):
    # Act
    result = parse_availability(minimal_product)

    # Assert
    assert result is False