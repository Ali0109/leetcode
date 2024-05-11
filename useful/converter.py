from moviepy.editor import VideoFileClip


def convert_mov_to_mp4(input_file, output_file):
    try:
        clip = VideoFileClip(input_file)
        clip.write_videofile(output_file)
        print("Конвертация завершена успешно.")
    except Exception as e:
        print(f"Произошла ошибка при конвертации: {e}")


if __name__ == "__main__":
    input_file = "../test.mov"
    output_file = "../output.mp4"
    convert_mov_to_mp4(input_file, output_file)
