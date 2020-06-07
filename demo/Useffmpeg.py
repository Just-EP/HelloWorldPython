#!/usr/bin/python3
# 使用ffmpeg将脚本所在目录下的wav音频转换为其他占用磁盘空间较小的格式


def main():
    import os
    # 获取脚本所在路径
    # ffmpeg -i input.wav -f mp3 -acodec libmp3lame -y output.mp3
    path = os.getcwd()
    suffix_input = '.wav'
    suffix_output = '.flac'
    # os.walk(path) 路径 路径下所有子文件夹 路径下所有所有文件
    ftd = []
    for p, d, files in os.walk(path):
        for file in files:
            if file[file.rfind('.'):] == suffix_input:
                # ftd.append(path+os.sep+file)
                ftd.append(file)
    for name in ftd:
        output_name = name.replace(suffix_input, suffix_output)
        cmd = 'ffmpeg -i ' + name + ' ' + output_name
        # cmd = 'ffmpeg -i ' + name + ' -c:a aac ' + output_name
        # cmd = 'ffmpeg -i ' + name + ' -f mp3 -acodec libmp3lame -y ' + output_name
        # ffmpeg -i a.wav  -c:a aac a.aac
        # ffmpeg -i a.wav a.flac
        os.system(cmd)


if __name__ == '__main__':
    main()
