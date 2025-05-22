import os

def get_csv_path():
    base_dir = os.path.dirname(os.path.abspath(__file__)) 
    storage_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'Storage', 'Database'))
    return storage_path

'''if __name__ == "__main__":
    print(get_parquet_path())
    '''