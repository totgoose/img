import os
from rembg import remove
from PIL import Image

def process_images():
    # Получаем текущую папку, где лежит скрипт
    current_dir = os.getcwd()
    
    # Список расширений, которые будем обрабатывать
    target_extensions = ('.webp',)
    
    print(f"Поиск файлов .webp в папке: {current_dir}...")
    
    files_processed = 0

    # Проходим по всем файлам в папке
    for filename in os.listdir(current_dir):
        if filename.lower().endswith(target_extensions):
            input_path = os.path.join(current_dir, filename)
            
            print(f"Обработка: {filename}")
            
            try:
                # Открываем изображение
                input_image = Image.open(input_path)
                
                # Удаляем фон
                output_image = remove(input_image)
                
                # Сохраняем изображение с тем же именем и расширением
                # Важно: сохраняем именно в WEBP, чтобы сохранить прозрачность
                output_image.save(input_path, format='WEBP')
                
                print(f"Успешно: {filename}")
                files_processed += 1
                
            except Exception as e:
                print(f"Ошибка при обработке {filename}: {e}")

    print(f"\nГотово! Обработано файлов: {files_processed}")

if __name__ == "__main__":
    process_images()