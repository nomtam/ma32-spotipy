def main():
    from Core.IO.Dir import read_all_json_files_from_directory
    data = read_all_json_files_from_directory()
    print(data)


if __name__ == "__main__":
    main()
