def solution(queries):
    from collections import defaultdict
    file_map = defaultdict(int)
    max_heap = []
    import heapq

    def file_exists(file):
        return file in file_map

    res = []

    for query in queries:
        if len(query) == 3:
            op, file, size = query
            size = int(size)
            if op == "ADD_FILE":
                if file_exists(file):
                    res.append("false")
                else:
                    res.append("true")
                    file_map[file] = size
            elif op == "GET_N_LARGEST":
                largest = size

                prefix = '/'.join(file.split('/'))
                for file_name, s in file_map.items():
                    # print('file_name', file_name, "looking for", file)
                    if file_name.startswith(prefix) and s > size:
                        max_heap.append((-s, file_name))

                if len(max_heap) == 0:
                    res.append("")
                    break

                heapq.heapify(max_heap)
                # n_largest = heapq.nlargest(largest, max_heap)
                out = ""
                count = 0
                out = ""
                while len(max_heap) != 0 and count < largest:
                    s, name = heapq.heappop(max_heap)
                    out += name + '(' + str(file_map[name]) + '), '
                    count = count + 1

                out = out.strip(', ')

                res.append(out)

        elif len(query) == 2:
            op, file = query
            if op == "GET_FILE_SIZE":
                if file_exists(file):
                    res.append(str(file_map[file]))
                else:
                    res.append("")
            elif op == "DELETE_FILE":
                if file_exists(file):
                    res.append(str(file_map[file]))
                    del file_map[file]
                else:
                    res.append("")

    return res


def test():
    queries = [
        ["ADD_FILE", "/dir/file1.csv", "5"],
        ["ADD_FILE", "/dirfile2csv", "5"],
        ["ADD_FILE", "/dir/file3.txt", "5"],
        ["GET_N_LARGEST", "/dir", "3"],
        ["ADD_FILE", "/dir/dir/dir/dirfile", "5"],
        ["GET_N_LARGEST", "/", "3"],
        ["ADD_FILE", "/dir/dir/dirfile", "5"],
        ["GET_N_LARGEST", "/dir", "2"],
        ["DELETE_FILE", "/dir/dir/dir/dirfile"],
        ["GET_N_LARGEST", "/dir", "5"]
    ]

    expected = ["true",
                "true",
                "true",
                "/dir/file1.csv(5), /dir/file3.txt(5), /dirfile2csv(5)",
                "true",
                "/dir/dir/dir/dirfile(5), /dir/file1.csv(5), /dir/file3.txt(5)",
                "true",
                "/dir/dir/dir/dirfile(5), /dir/dir/dirfile(5)",
                "5",
                "/dir/dir/dirfile(5), /dir/file1.csv(5), /dir/file3.txt(5), /dirfile2csv(5)"]

    output = solution(queries)
    print(queries)
    print(output)
    print(expected)

    return output == expected


print(test())


def test2():
    queries = [["ADD_FILE", "/file2.jpg", "6"],
               ["ADD_FILE", "/dir1/file3", "5"],
               ["ADD_FILE", "/dir2/file6.mp4", "50"],
               ["DELETE_FILE", "/dir2/file6.mp4"],
               ["GET_N_LARGEST", "/dir2", "3"],
               ["DELETE_FILE", "/dir1/file3"],
               ["GET_N_LARGEST", "/dir1", "1"],
               ["GET_N_LARGEST", "/", "15"]]
    expected = ["true",
                "true",
                "true",
                "50",
                "",
                "5",
                "",
                "/file2.jpg(6)"]


def test2():
    queries = [["GET_N_LARGEST", "/dir3", "2"],
               ["GET_N_LARGEST", "/", "3"],
               ["ADD_FILE", "/dir1/dir2/dir3/dir1/file", "100"],
               ["GET_FILE_SIZE", "/dir1/dir2/dir3/dir1/file"],
               ["GET_N_LARGEST", "/dir1", "3"],
               ["GET_N_LARGEST", "/dir2", "1"],
               ["GET_N_LARGEST", "/dir3", "1"]]

    expected = ["", "", "true", "100", "/dir1/dir2/dir3/dir1/file(100)", "", ""]


queries = [["ADD_FILE", "/dir/file1", "7"],
           ["ADD_FILE", "/dir/file2", "7"],
           ["ADD_FILE", "/file3", "8"],
           ["GET_FILE_SIZE", "/dir/file1"],
           ["GET_N_LARGEST", "/", "5"],
           ["GET_N_LARGEST", "/dir", "3"],
           ["GET_FILE_SIZE", "/dir/file2"],
           ["GET_N_LARGEST", "/dir", "3"],
           ["DELETE_FILE", "/dir/file1"],
           ["GET_N_LARGEST", "/dir", "2"],
           ["DELETE_FILE", "/file3"],
           ["GET_N_LARGEST", "/", "2"],
           ["DELETE_FILE", "/dir/file1"],
           ["DELETE_FILE", "/dir/file2"],
           ["GET_N_LARGEST", "/", "2"]]

expected = ["true",
            "true",
            "true",
            "7",
            "/file3(8), /dir/file1(7), /dir/file2(7)",
            "/dir/file1(7), /dir/file2(7)",
            "7",
            "/dir/file1(7), /dir/file2(7)",
            "7",
            "/dir/file2(7)",
            "8",
            "/dir/file2(7)",
            "",
            "7",
            ""]

queries = [["GET_N_LARGEST", "/", "4"],
           ["ADD_FILE", "/dir/file.mp4", "100"],
           ["GET_FILE_SIZE", "/dir/file.mp4"],
           ["ADD_FILE", "/dir/file.mp4", "150"],
           ["ADD_FILE", "/file.mp4", "100"],
           ["GET_FILE_SIZE", "/dir/file.mp4"],
           ["GET_N_LARGEST", "/", "1"],
           ["GET_N_LARGEST", "/", "2"],
           ["GET_N_LARGEST", "/", "3"],
           ["ADD_FILE", "/dirfile.mp4", "100"],
           ["ADD_FILE", "/dir/library/package/exec", "1"],
           ["DELETE_FILE", "/dir/file.mp4"],
           ["GET_N_LARGEST", "/dir", "3"],
           ["GET_N_LARGEST", "/dir", "2"],
           ["GET_N_LARGEST", "/dir", "1"],
           ["GET_N_LARGEST", "/", "10"]]

expeced = ["", "true", "100", "false", "true", "100", "/dir/file.mp4(100)", "/dir/file.mp4(100), /file.mp4(100)",
           "/dir/file.mp4(100), /file.mp4(100)", "true", "true", "100",
           "/dirfile.mp4(100), /dir/library/package/exec(1)", "/dirfile.mp4(100), /dir/library/package/exec(1)",
           "/dirfile.mp4(100)", "/dirfile.mp4(100), /file.mp4(100), /dir/library/package/exec(1)"]

queries = [["ADD_FILE", "/lib/bin/exec.sh", "34"],
           ["ADD_FILE", "/lib/bin/py3", "78"],
           ["ADD_FILE", "/lib/bin/py3.9", "79"],
           ["ADD_FILE", "/lib/bin/python3", "78"],
           ["ADD_FILE", "/lib/bin/python3.9", "79"],
           ["ADD_FILE", "/lib/bin/python2", "50"],
           ["DELETE_FILE", "/lib/bin/py3"],
           ["GET_N_LARGEST", "/", "10"],
           ["ADD_FILE", "/lib/bin/exec.sh", "60"],
           ["ADD_FILE", "/lib/bin/exec.sh", "300"],
           ["ADD_FILE", "/lib/exec/exec.sh", "300"],
           ["GET_N_LARGEST", "/lib/bin", "4"],
           ["GET_N_LARGEST", "/lib/bingo", "9"],
           ["GET_N_LARGEST", "/lib/bi", "9"],
           ["GET_N_LARGEST", "/lib", "4"],
           ["DELETE_FILE", "/lib/bin/py3"],
           ["GET_FILE_SIZE", "/lib/bin/exec.sh"],
           ["GET_FILE_SIZE", "/exec.sh"],
           ["GET_FILE_SIZE", "/lib/exec/exec.sh"],
           ["GET_FILE_SIZE", "/library/exec/exec.sh"],
           ["DELETE_FILE", "/lib/bin/py3"],
           ["GET_N_LARGEST", "/", "5"],
           ["GET_N_LARGEST", "/lib", "6"],
           ["GET_N_LARGEST", "/lib/exec", "2"]]

expected = ["true",
            "true",
            "true",
            "true",
            "true",
            "true",
            "78",
            "/lib/bin/py3.9(79), /lib/bin/python3.9(79), /lib/bin/python3(78), /lib/bin/python2(50), /lib/bin/exec.sh(34)",
            "false",
            "false",
            "true",
            "/lib/bin/py3.9(79), /lib/bin/python3.9(79), /lib/bin/python3(78), /lib/bin/python2(50)",
            "",
            "/lib/bin/py3.9(79), /lib/bin/python3.9(79), /lib/bin/python3(78), /lib/bin/python2(50), /lib/bin/exec.sh(34)",
            "/lib/exec/exec.sh(300), /lib/bin/py3.9(79), /lib/bin/python3.9(79), /lib/bin/python3(78)",
            "",
            "34",
            "",
            "300",
            "",
            "",
            "/lib/exec/exec.sh(300), /lib/bin/py3.9(79), /lib/bin/python3.9(79), /lib/bin/python3(78), /lib/bin/python2(50)",
            "/lib/exec/exec.sh(300), /lib/bin/py3.9(79), /lib/bin/python3.9(79), /lib/bin/python3(78), /lib/bin/python2(50), /lib/bin/exec.sh(34)",
            "/lib/exec/exec.sh(300)"]

queries = [["ADD_FILE", "/index.html", "252"],
           ["ADD_FILE", "/collection/images/filename", "106"],
           ["ADD_FILE", "/trash/img.img", "18"],
           ["ADD_FILE", "/library/bin/containers/filename", "43"],
           ["ADD_FILE", "/library/bin/containers/video3435.mp4", "146"],
           ["ADD_FILE", "/collection/video3435.mp4", "84"],
           ["ADD_FILE", "/trash/filename", "12"],
           ["ADD_FILE", "/collection/img.img", "113"],
           ["ADD_FILE", "/trash/img.img", "29"],
           ["ADD_FILE", "/library/main.cpp", "154"],
           ["ADD_FILE", "/collection/pic_pic.png", "172"],
           ["ADD_FILE", "/trash/script.js", "79"],
           ["ADD_FILE", "/video3435.mp4", "285"],
           ["ADD_FILE", "/collection/images/pic_pic.png", "85"],
           ["ADD_FILE", "/collection/images/filename", "65"],
           ["ADD_FILE", "/trash/exec.exec", "177"],
           ["ADD_FILE", "/library/bin/containers/filename", "27"],
           ["ADD_FILE", "/collection/audio/img.img", "224"],
           ["ADD_FILE", "/library/bin/packages/pic_pic.png", "42"],
           ["ADD_FILE", "/library/bin/video3435.mp4", "2"],
           ["GET_N_LARGEST", "/collection", "13"],
           ["GET_N_LARGEST", "/library", "17"],
           ["GET_N_LARGEST", "/", "6"],
           ["GET_N_LARGEST", "/", "15"],
           ["GET_N_LARGEST", "/collection", "1"],
           ["GET_N_LARGEST", "/", "19"]]

expected = ["true",
            "true",
            "true",
            "true",
            "true",
            "true",
            "true",
            "true",
            "false",
            "true",
            "true",
            "true",
            "true",
            "true",
            "false",
            "true",
            "false",
            "true",
            "true",
            "true",
            "/collection/audio/img.img(224), /collection/pic_pic.png(172), /collection/img.img(113), /collection/images/filename(106), /collection/images/pic_pic.png(85), /collection/video3435.mp4(84)",
            "/library/main.cpp(154), /library/bin/containers/video3435.mp4(146), /library/bin/containers/filename(43), /library/bin/packages/pic_pic.png(42), /library/bin/video3435.mp4(2)",
            "/video3435.mp4(285), /index.html(252), /collection/audio/img.img(224), /trash/exec.exec(177), /collection/pic_pic.png(172), /library/main.cpp(154)",
            "/video3435.mp4(285), /index.html(252), /collection/audio/img.img(224), /trash/exec.exec(177), /collection/pic_pic.png(172), /library/main.cpp(154), /library/bin/containers/video3435.mp4(146), /collection/img.img(113), /collection/images/filename(106), /collection/images/pic_pic.png(85), /collection/video3435.mp4(84), /trash/script.js(79), /library/bin/containers/filename(43), /library/bin/packages/pic_pic.png(42), /trash/img.img(18)",
            "/collection/audio/img.img(224)",
            "/video3435.mp4(285), /index.html(252), /collection/audio/img.img(224), /trash/exec.exec(177), /collection/pic_pic.png(172), /library/main.cpp(154), /library/bin/containers/video3435.mp4(146), /collection/img.img(113), /collection/images/filename(106), /collection/images/pic_pic.png(85), /collection/video3435.mp4(84), /trash/script.js(79), /library/bin/containers/filename(43), /library/bin/packages/pic_pic.png(42), /trash/img.img(18), /trash/filename(12), /library/bin/video3435.mp4(2)"]
