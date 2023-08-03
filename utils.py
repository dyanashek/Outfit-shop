def validate_size(size):
    try:
        return float(size.replace(' ', '').replace(',', '.'))
    
    except:
        return False