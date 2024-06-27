#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_assessment_value(value):
    assessment_value = (value*.60)

    return assessment_value

def get_tax_assessed(assessment_value):
    property_tax = round(assessment_value*(.72/100), 2)

    return property_tax
    