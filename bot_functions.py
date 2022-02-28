import urbandictionary as ud

def define(word)->list:
    data = ud.define(word)
    data.sort(reverse=True, key = rated)
    data = data[:3]  # Top 3 definitions are used
    new_data = [str(x.definition) for x in data]  # For convinient representation
    return new_data

def random_word()->list:
    rand = ud.random()
    x = rand[0]
    return x

def rated(definition)->int:
    return definition.upvotes
    
