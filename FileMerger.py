class FileMerger:
    def __init__(self, input_files):
        self.input_files = input_files

    def merge_files(self, output_filename='result.txt'):
        files_info = []

        for filename in self.input_files:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    files_info.append({
                        'name': filename.split('/')[-1],
                        'line_count': len(lines),
                        'content': lines
                    })
            except FileNotFoundError:
                print(f"Файл {filename} не найден")
                continue

        files_info.sort(key=lambda x: x['line_count'])

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for file_info in files_info:
                output_file.write(f"{file_info['name']}\n")
                output_file.write(f"{file_info['line_count']}\n")
                output_file.writelines(file_info['content'])
                output_file.write("\n")

        print(f"Файлы объединены в {output_filename}")

merger = FileMerger(['sorted/1.txt', 'sorted/2.txt', 'sorted/3.txt'])
merger.merge_files()