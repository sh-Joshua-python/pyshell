'''
将result 目录下子目录指定文件
将新目录打包压缩 xxx.tar.gz
'''

import os
import time
import shutil
import tarfile


def product_simple(file_list, base_path):
    '''
    根据file_list 生成想保留的文件
    '''
    simple_path = base_path + '_simple'

    if os.path.isdir(simple_path):
        shutil.rmtree(simple_path)
    shutil.copytree(base_path, simple_path)

    content = os.walk(simple_path)
    for path, dirs, files in content:
        for file in files:
            file_path = os.path.join(path, file)
            if file not in file_list:
                # print(f'{time.strftime("%F %T")}  {file}')
                os.unlink(file_path)

    # print(f'{time.strftime("%F %T")} {simple_path} 创建完成！')
    return simple_path

def dir2tar_gz(source_dir):
    '''
    将source_dir 打包为 tar.gz
    '''
    output_filename = source_dir + '.tar.gz'
    print(f'{time.strftime("%F %T")} 文件保存位置:{output_filename}')
    output_filepath = os.path.join(source_dir, '.tar.gz')
    if os.path.exists(output_filepath):
        os.unlink(simple_path)

    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(output_filepath))

    shutil.rmtree(source_dir)
    print(f'{time.strftime("%F %T")} 完成创建:{output_filename.split("/")[-1]}')


if __name__ == "__main__":
    t_start = time.time()
    file_list = ['aa.txt', 'bb.txt']
    base_path = os.path.dirname(os.path.abspath(__file__))
    simple_path = product_simple(file_list, base_path)
    dir2tar_gz(simple_path)
    t_end = time.time()
    print(f'{time.strftime("%F %T")} 总用时:{t_end - t_start}')
    
