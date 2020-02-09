#!/usr/bin/python3
# 使用ffmpeg将脚本所在目录下的wav音频转换为mp3


def main():
    import os
    # 获取脚本所在路径
    # ffmpeg -i input.wav -f mp3 -acodec libmp3lame -y output.mp3
    path = os.getcwd()
    suffix_wav = '.wav'
    suffix_mp3 = '.mp3'
    # os.walk(path) 路径 路径下所有子文件夹 路径下所有所有文件
    ftd = []
    for p, d, files in os.walk(path):
        for file in files:
            if file[file.index('.'):] == suffix_wav:
                # ftd.append(path+os.sep+file)
                ftd.append(file)
    for name in ftd:
        mp3_name = name.replace(suffix_wav, suffix_mp3)
        cmd = 'ffmpeg -i ' + name + ' -f mp3 -acodec libmp3lame -y ' + mp3_name
        os.system(cmd)


if __name__ == '__main__':
    main()
