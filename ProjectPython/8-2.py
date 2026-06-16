import os
import threading
import time
import requests


class Downloader:

    def __init__(self, save_dir="./download", max_threads=3):
        self.save_dir = save_dir
        self.max_threads = max_threads
        self.lock = threading.Lock()
        self.completed_bytes = 0
        os.makedirs(self.save_dir, exist_ok=True)

    def download_file(self, url):
        filename = url.split("/")[-1] or "downloaded_file"
        if "." not in filename:
            filename = "downloaded_file"
        filepath = os.path.join(self.save_dir, filename)

        existing_size = 0
        if os.path.exists(filepath):
            existing_size = os.path.getsize(filepath)
            if existing_size > 0:
                print("断点续传: {} 已有{}字节".format(filename, existing_size))

        headers = {}
        if existing_size > 0:
            headers["Range"] = "bytes={}-".format(existing_size)

        try:
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            response.raise_for_status()
            content_length = response.headers.get("Content-Length")
            total_size = None
            if content_length:
                total_size = int(content_length) + existing_size

            mode = "ab" if existing_size > 0 else "wb"
            downloaded = existing_size
            start_time = time.time()
            last_update = time.time()
            last_bytes = downloaded

            with open(filepath, mode) as f:
                while True:
                    chunk = response.iter_content(8192)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)

                    with self.lock:
                        self.completed_bytes += len(chunk)
                        if total_size:
                            percent = downloaded / total_size * 100
                            now = time.time()
                            if now - last_update > 0.5:
                                speed = (downloaded - last_bytes) / (now - last_update)
                                speed_kb = speed / 1024
                                print("\r{}: {:.1f}% {:.1f}KB/s".format(
                                    filename, percent, speed_kb), end="")
                                last_update = now
                                last_bytes = downloaded

            elapsed = time.time() - start_time
            avg_speed = 0
            if elapsed > 0:
                avg_speed = (downloaded - existing_size) / elapsed / 1024
            print("\n文件{}下载完成，保存路径：{} 平均速度:{:.1f}KB/s".format(
                filename, filepath, avg_speed))
            return True

        except requests.exceptions.RequestException as e:
            print("下载失败：{} 网络异常 {}".format(filename, e))
            return False
        except Exception as e:
            print("文件保存失败：{} {}".format(filename, e))
            return False

    def batch_download(self, urls):
        threads = []
        for url in urls:
            while threading.active_count() - 1 >= self.max_threads:
                time.sleep(0.1)
            t = threading.Thread(target=self.download_file, args=(url,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("\n批量下载完成")


def test():
    print("=== 多线程下载实验 ===")
    print("多线程适用场景: I/O密集型任务(网络下载/文件读写)")
    print("多进程适用场景: CPU密集型任务(计算/图像处理)")
    print()

    downloader = Downloader(max_threads=3)

    test_urls = [
        "https://www.python.org/static/img/python-logo.png",
        "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    ]

    print("可用测试URL:")
    for u in test_urls:
        print(" ", u)
    print()

    urls = []
    print("输入下载链接(每行一个,空行结束):")
    while True:
        u = input()
        if not u.strip():
            break
        urls.append(u.strip())

    if not urls:
        print("使用默认测试链接")
        urls = test_urls

    if urls:
        downloader.batch_download(urls)


if __name__ == "__main__":
    test()