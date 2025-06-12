from faker import Faker

def get_data():
    ...

def parse_data(*args):
    ...

def save_parsed_data(*args):
    ...

def main():
    data = get_data()
    parsed_data = parse_data(data)
    save_parsed_data(parsed_data)
    ...

if __name__ == "__main__":
    main()