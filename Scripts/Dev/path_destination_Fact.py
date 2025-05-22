import os

def get_fact_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    storage_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'Storage', 'Fact'))
    return storage_path

'''if __name__ == "__main__":
    print(get_dim_path())'''
