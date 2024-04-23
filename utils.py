import os

def walk_directory(directory, formatList=[]):
    files_path = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.strip().split('.')[-1] not in formatList:
                continue
            filepath = os.path.join(root, file)
            # print(filepath)
            files_path.append(filepath)
    return files_path


def main():
    print("This is utils module")

if __name__ == "__main__":
    main()
