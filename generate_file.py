import os


def generate_file(filename, size_bytes):
    """
    生成指定大小的文件

    Args:
        filename (str): 要生成的文件名
        size_bytes (int): 文件大小(字节)
    """
    # 确保size_bytes是正整数
    size_bytes = abs(int(size_bytes))

    # 使用更大的块大小 (10MB)
    chunk_size = 10 * 1024 * 1024

    # 预生成一个随机数据块，重复使用以提高性能
    data_chunk = os.urandom(chunk_size)

    # 使用缓冲写入
    with open(filename, 'wb', buffering=8388608) as f:  # 8MB buffer
        remaining = size_bytes

        while remaining > 0:
            current_chunk = min(chunk_size, remaining)
            if current_chunk == chunk_size:
                f.write(data_chunk)
            else:
                f.write(data_chunk[:current_chunk])
            remaining -= current_chunk


if __name__ == '__main__':
    generate_file('test-990.img', 990 * 1024 * 1024)
