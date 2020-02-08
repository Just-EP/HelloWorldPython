# 使用ffmpeg将脚本所在目录下的wav音频转换为mp3
if __name__ == '__main__':
    import os
    # 获取脚本所在路径
    # ffmpeg -i input.wav -f mp3 -acodec libmp3lame -y output.mp3
    path = os.getcwd()
    suffixWav = '.wav'
    suffixMP3 = '.mp3'
    # os.walk(path) 路径 路径下所有子文件夹 路径下所有所有文件
    ftd = []
    for p, d, files in os.walk(path):
        for file in files:
            if file[file.index('.'):] == suffixWav:
                # ftd.append(path+os.sep+file)
                ftd.append(file)
    for name in ftd:
        mp3name = name.replace(suffixWav, suffixMP3)
        cmd = 'ffmpeg -i '+name+' -f mp3 -acodec libmp3lame -y '+mp3name
        os.system(cmd)
