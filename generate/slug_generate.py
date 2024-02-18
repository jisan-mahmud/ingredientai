def slug(name_str):
    slug_str = '_'.join(word for word in name_str.split(' '))
    return slug_str.lower()